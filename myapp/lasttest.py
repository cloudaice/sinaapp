#-*- encoding:utf8 -*-
from weibo import APIClient
import time
import json

APP_KEY = "3302956248"
APP_SECRET="a3d8968cc21fd8115ad6e90994755cfc"
CALLBACK_URL = "https://api.weibo.com/oauth2/default.html"


client = APIClient(APP_KEY, APP_SECRET, CALLBACK_URL);
access_token = '2.00FvIAQCsnrWbD081ec68b1eRsj_lB'
expires_in = 1544932574
client.set_access_token(access_token, expires_in)

def get_fans(user_id):
    """获得用户的粉丝的详细信息"""
    fans_list = []
    fans_result = client.get.friendships__followers(uid = user_id, count = 150)
    next_cursor = 1
    while next_cursor:
        for fan in fans_result["users"]:
            fans_list.append(fan["id"])
            print fan["screen_name"]
        next_cursor = fans_result["next_cursor"]
        fans_result = client.get.friendships__followers(uid = user_id, count = 150, cursor = next_cursor)
    return fans_list

def get_fans_id(user_id):
    """
    获取用户的粉丝的uid列表
    """
    fans_id_list = []
    fans_id_result = client.get.friendships__followers__ids(uid =  user_id)
    next_cursor = 1
    while next_cursor:
        fans_id_list.extend(fans_id_result["ids"])
        print fans_id_result['ids'][0]
        next_cursor = fans_id_result["next_cursor"]
        fans_id_result = client.get.friendships__followers__ids(uid = user_id)
    return fans_id_list

def get_two_fans_net(user_id):
    """
   按照需求一生成json格式文档
   this has test
    """
    json_file_by_id = {}
    first_node_fans_list =[]
    json_file_by_id['id'] = user_id
    json_file_by_id['fans'] = first_node_fans_list
    first_fans_list = get_fans_id(user_id)
    for fan in first_fans_list:
        node = {}
        node['id'] = fan
        node['fans']=get_fans_id(fan)
        first_node_fans_list.append(node)
    return json_file_by_id

def get_fans_and_fans_list(json_net_file_name):
    """
    实现需求二中的功能
    """
    fd = open(json_net_file_name,'r')
    node_net  = json.loads(fd.read())
    json_file_by_fans = {}
    all_fans_list = []
    json_file_by_fans['all_fans']=all_fans_list
    first_fans_list = []
    for node in node_net['fans']:
        first_fans_list.append(node['id'])
    json_file_by_fans['id']=node_net['id']
    json_file_by_fans['fans_number']=len(first_fans_list)
    json_file_by_fans['fans_list'] = first_fans_list
    for node in node_net['fans']:
        node['fans_list'] = node['fans']
        node['fans_number']=len(node['fans'])
        del node['fans']
        all_fans_list.append(node)
    return  json_file_by_fans



def get_edges(json_file_name):
    """
    需求三中的要求
    """
    json_file_by_fans = json.loads(open(json_file_name,'r').read())
    count=0
    old_list = []
    old_list.append(json_file_by_fans['id'])
    count +=json_file_by_fans['fans_number']
    for node in json_file_by_fans['all_fans']:
        old_list.append(node['id'])
        for fan in node['fans_list']:
            if not fan in old_list:
                count+=1
    return count

def get_last_weibo_id(user_id):
    return client.get.statuses__user_timeline__ids(uid = user_id,count =1)['statuses'][0]

def get_weibo_ids_since(user_id,since_id):
    result_data = {}
    result_data['weibo']=[]
    total_weibo_ids = []
    weibo_ids_result = client.get.statuses__user_timeline__ids(uid = user_id,since_id=since_id,count = 1,page=1)
    total_weibo_num = weibo_ids_result['total_number']
    total_pages = total_weibo_num/100  if not total_weibo_num % 100  else total_weibo_num/100 +1 
    for page in range(1,total_pages+1):
        weibo_ids_result = client.get.statuses__user_timeline__ids(uid = user_id,since_id = since_id,count = 100,page = page)
        total_weibo_ids.extend(weibo_ids_result['statuses'])
    result_data['weibo_num']=total_weibo_num
    for weibo_id in total_weibo_ids:
        node = {}
        node['id']=weibo_id
        result_re_co = client.get.statuses__count(ids = weibo_id)
        node['reposts'] = result_re_co[0]['reposts']
        node['comments'] = result_re_co[0]['comments']
        result_data['weibo'].append(node)
    return result_data


def get_user_fans_num(user_id):
    result_data = client.get.users__counts(user_id)
    return result_data[0]['followers_count']


def get_nnet_ode_num(net):
    count=1
    all_ids=[net['id']]
    for node in net['fans']:
        if node['id'] not in all_ids:
            all_ids.append(node['id'])
            count+=1
        for fan in node['fans']:
            if fan not in all_ids:
                all_ids.append(fan)
                count+=1
    return count

if __name__ == "__main__":
    #print get_last_weibo_id(2068721331)
    #result = get_two_fans_net(2068721331)
    #result = get_two_fans_net(1865922131)
    #t = json.dumps(result)
    #fd = open('first.json','w')
    #fd.write(t)
    #result = get_fans_and_fans_list('first.json')
    #t = json.dumps(result)
    #fd = open('first1.json','w')
    #fd.write(t)
    print get_edges("first1.json")



