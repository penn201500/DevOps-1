# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 17 17:18
# Author Yo
# Email YoLoveLife@outlook.com
from models import Group
from django.core import serializers
from util import toJSON,str2dict
from anweb.models import Group,Host,Softlib,Soft
from django.forms.models import model_to_dict
import json
'''
PARM:null
RETURN:list
USE:返回所有组的列表
'''
def group9groupsearch():
    a = Group.objects.all()
    list = []
    for i in a:
        list.append(toJSON(i))
    return list

'''
PARM:group_id,group_name,group_remark
RETURN:TRUE/FALSE
USE:如果组不存在 则添加组；如果组存在 则修改组
'''
def group9modifygroup(group_id,group_name,group_remark):
    if group_id == "0":#ADD
        group=Group(group_name=unicode.encode(group_name),remark=unicode.encode(group_remark))
        group.save()
    else:#UPDATE
        Group.objects.filter(id=int(group_id)).update(group_name=unicode.encode(group_name),remark=unicode.encode(group_remark))

'''
PARM:group_id
RETURN:返回组相关的信息
USE:
'''
def host9hostsearch(group_id):
    hostlist = Host.objects.filter(group_id=int(group_id))#需要展示的用户列表
    #需要从用户列表中 添加app-type的数据
    type_list=Soft.objects.all()
    list=[]
    for host in hostlist:
        tmpdict=model_to_dict(host)
        tmpdict['app_type']=host.softlib.soft_type.soft_name
        list.append(json.dumps(tmpdict))
    return list
