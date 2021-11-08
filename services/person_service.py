import csv
import os
from typing import Optional
from fastapi import HTTPException,status
from models.person import Person

class Person_src:


    def save_person(self,dict_person : Person):
        """This method save the new user on csv file"""

        mode = "a"
        its_empty = False
        file = 'data_person.csv'
        
        if os.stat(file).st_size == 0:
            mode = "w"
            its_empty = True
        
        fields = list(dict_person.keys())
        
        with open(file,mode,encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames = fields)
            print(its_empty)
            if its_empty:
                writer.writeheader()

            writer.writerow(dict_person)
    

    def read_person(self,personto:Optional[str] = None):

        """This method return the person by name if the name
         is none return all of the persons"""
        dict_items = {}
        with open("data_person.csv",mode="r",encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                i.pop("password")
                if i["first_name"] == personto:
                    return i
                dict_items[i["first_name"]] = i
                
        
        if not personto:
            return dict_items
    
        return {personto:"Not found"}      

    
    def format_topics_str(self,string):

        list_topics = string[2:-2].split(",")

        list_topics = [char.replace("'","") for char in list_topics]

        return list_topics  

    
    def intersection_sets(self,set01,set02):
        total = set01 & set02
        return total


    def recomend_who_follow(self,name : str):

        """This method will allows  get a list of users that like several topics that our user"""

        users = []
        my_user = {}
        with open("data_person.csv",mode="r",encoding="utf-8") as csvfile:
            writer = csv.DictReader(csvfile)
            for user in writer:
                user.pop("password")
                if user["first_name"].upper() == name.upper():
                    my_user = user
                else:
                    users.append(user)
        
        if not my_user:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "This person does not exist!") 

        topics_my_user = self.format_topics_str(my_user["topics"])

        recomended_user = []
        for user in users:
            topics_str = user["topics"]
            topics_list = self.format_topics_str(topics_str)
            if len(self.intersection_sets(set(topics_my_user),set(topics_list)))>=2:
                recomended_user.append(user)
        
        return recomended_user

            



            
          
        
                
            
                
        
        

            
        


        