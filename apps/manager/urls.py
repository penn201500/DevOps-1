# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 10 15:38
# Author Yo
# Email YoLoveLife@outlook.com
from django.conf.urls import url

import views

urlpatterns = [
    url(r'^group$', views.ManagerGroupView.as_view(), name='group'),
]