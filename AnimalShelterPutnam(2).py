#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 20:47:47 2021

@author: miranda.putna_snhu
"""
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD Operations for Animal collection in MongoDB"""
    
    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections
        self.client = MongoClient('mongodb://%s:%s@localhost:37362/AAC' % ('aacuser', 'aacuserpassword'))
        self.database = self.client['AAC']
        
    # Method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            # insert data
            # crated a data dictionary with keys corresponding to AAC. I left the values empty because they are to be set
            self.database.animals.insert({'1': None, 'age_upon_outcome': None, 'animal_id': None, 'animal_type': None, 'breed':
                                          None, 'color': None, 'date_of_birth': None, 'datetime': None, 'monthyear': None, 
                                          'name': None, 'outcome_subtype': None, 'outcome_type': None, 'sex_upon_outcome': None,
                                          'location_lat': None, 'location_long': None, 'age_upon_outcome_in_weeks': None}) 
            return True
        else:
            # tell user if data is empty
            raise Exception("Nothing to insert because data parameter is empty")
            return False  
            
    # Method to implement R in CRUD
    def read(self, data):
        # return result that matches the search criteria
        if data is not None:
            return self.database.animals.find(data,{"_id": False})
        else:
            # let user know if invalid
            raise Exception("Nothing to search because data parameter is empty")
            return False
   
    # Method to implement the U in CRUD
    def update(self, data, dataUpdate):
        # update data if valid
        if data is not None:
            return self.database.animals.update(data, dataUpdate)
        else:
            # let the user know if invalid
            raise Exception("Nothing to update because data parameter is empty")
            return False
    
    # Method to implement the D in CRUD
    def delete(self, data):
        # delete data if valid
        if data is not None:
            return self.database.animals.remove(data)
        else:
            # let user know if invalid
            raise Exception("Nothing to delete because data parameter is empty")
            return False
        
        
        