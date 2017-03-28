#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from www.transwrap import db

db.create_engine('root', 'rootroot', 'test')
#x = dict(id=1, name='Matt', email='matt.mi@ericsson.com', passwd='Easy2get', last_modified=time.time())
#print x
#db.insert('user', **x)
print db.select('select * from user')
print db.select('select count(*) from user')
