# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 10:51:36 2018

"""

"""
0. From File to DB

1. E-R to Model
    
    (Entity) Stock (id, name, open, close, exchange, datetime)
    (Model) class Stock (int id, string name, double open, double close, string exchange, localdatetime datetime)
    -- getter and setter, tostring, hashcode / equals
    
    class stock:
        ...
    (DAO)    
    
2. Controller

    #(1). from file (csv? text? ???)
    #(2). to db (pgsql? mysql? mongodb? ...)
    
    class file_date_loader:
        - def load_txt(tile_name):
            return list[Exchange]
            
        - def load_csv(file_name): #test file
            return list[Stock]
        
        - 
        
    class stock_repo:
        - def insert_all(list[Stock]):
            return number # updater rows
        - def insert(Stock):
        
        - def get_all():
            return list[Stock]
        
        - def get_group_by(key):
            return "select name, count(*) from stock group by " + key
        
        ...
        
    class stock_updater:
        def __init__(self): #constructor
            self.loader = new file_data_loader(...)
            self.stock_repo = new stock_repo()
        
        - def update():
            return self.stock_repo.insert_all(self.loader.load())
            
    class stock_queryer:
        def __init__(self):
            self.stock_repo = new stock_repo()
        
        def get_group_by_stock_name():
            return self.stock_repo.get_group_by("name")
            
    
3. View ? -> Web UI, Console, Graph 
    # group by count -> user request

    class console_viewer:
        def print_group_by(result):
            print (result)


################################################################    
    class App: #test main class -> start()
        def __init__(self):        
            self.updater = new stock_updater()
            self.queryer = new stock_queryer()
            self.viewer = new console_viewer()
        
        def start():
            self.updater.update()
            self.viewer.print_group_by(
                    self.queryer.get_group_by_stock_name()
            )
################################################################
            
            
"""
