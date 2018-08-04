# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 00:12:04 2018

@author: steven

This is to introduce some numpy basic props.
"""

def get_connection(execute_sql):
    cur = 15
    execute_sql(cur)
    print("in foo: ", cur)

    
def select_sth(cur):
    print("select_sth", cur)
    
 
get_connection(select_sth)