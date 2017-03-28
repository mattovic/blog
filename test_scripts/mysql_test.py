#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(user='root', password='rootroot', database='test', use_unicode=True)
cursor = conn.cursor()
cursor.execute('select * from user')
print cursor.description
#names = [x[0] for x in cursor.description]
#print names
#print cursor.fetchone()
#print cursor.fetchone()
print cursor.fetchall()
cursor.close()
conn.close()