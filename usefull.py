#-*- encoding:utf8 -*-
from weibo import APIClient
import time
import json

APP_KEY = "3302956248"
APP_SECRET="a3d8968cc21fd8115ad6e90994755cfc"
CALLBACK_URL = "https://api.weibo.com/oauth2/default.html"


client = APIClient(APP_KEY, APP_SECRET, CALLBACK_URL);
access_token = '2.00FvIAQCsnrWbDc7db4866c97ItrJD'
expires_in = 1343932574
client.set_access_token(access_token, expires_in)
#print client.get.statuses__user_timeline(uid = 2068721331)
#client.get.friendships__followers(uid = 2068721331)
#data =  client.get.friendships__followers(uid = 1771925961, count = 199)
"""
data =  client.get.friendships__followers(screen_name = u"秦韬",count = 150)
print data["total_number"]
next_cursor = data["next_cursor"]
while   next_cursor :
    for uid  in data["users"]:
        print uid["id"]
    next_cursor = data["next_cursor"]
    print next_cursor
    print data["total_number"]
    data =  client.get.friendships__followers(screen_name = u"秦韬", count = 150, cursor=next_cursor)
"""

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
        next_cursor = fans_id_result["next_cursor"]
        fans_id_result = client.get.friendships__followers__ids(uid = user_id)
    return fans_id_list

def get_two_fans_net(user_id):
    """
   按照需求一生成json格式文档
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

def get_fans_and_fans_list(node_net):
    """
    实现需求二中的功能
    """
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



def get_edges(json_file_by_fans):
    """
    需求三中的要求
    """
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

def get_weibo_ids(user_id):
    weibo_id_result = client.get.statuses__user_timeline__ids(uid = user_id, feature = 0,count = 100,base_app= 0)
    print  weibo_id_result['total_number']
    print weibo_id_result['statuses']
    print len(weibo_id_result['statuses'])



if __name__ == "__main__":
    #data =  get_two_fans_net(2068721331)
    get_weibo_ids(2068721331)
