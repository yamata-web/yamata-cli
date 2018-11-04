# -*- coding: utf-8 -*-
from yamata.router.router_group import RouterGroup

router = RouterGroup()

router.get('/home', 'HomeController@hello')
