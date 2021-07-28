from flask_sqlalchemy import SQLAlchemy
from random import randint
import os

# db = SQLAlchemy()

class FamilyTree:
    def __init__(self, lastname):
        self.lastname = lastname

        self.members=[{
            'id' : 1,
            'firstname' : 'Ada',
            'lastname' : self.lastname,
            'age' : '35',
            'parent' : None,
            'children' : [3,4,5,6],
            'url' : os.environ.get('BACKEND_URL')      
        },
        {
            'id' : 2,
            'firstname' : 'Javier',
            'lastname' : self.lastname,
            'age' : '39',
            'parent' : None,
            'children' : [3,4,5,6]         
        },
        {
            'id' : 3,
            'firstname' : 'Hagen',
            'lastname' : self.lastname,
            'age' : '2',
            'parent' : [2,3] ,
            'children' : None        
        },
        {
            'id' : 4,
            'firstname' : 'Polaris',
            'lastname' : self.lastname,
            'age' : '2',
            'parent' : [2,3] ,
            'children' : None        
        },
        {
            'id' : 5,
            'firstname' : 'Alba',
            'lastname' : self.lastname,
            'age' : '1',
            'parent' : [2,3] ,
            'children' : None        
        },
        {
            'id' : 6,
            'firstname' : 'Mime',
            'lastname' : self.lastname,
            'age' : '1',
            'parent' : [2,3] ,
            'children' : None        
        },
        {
            'id' : 7,
            'firstname' : 'cactus',
            'lastname' : self.lastname,
            'age' : '1',
            'parent' : [4] ,
            'children' : None        
        }
        ]
    def generateId(self):
        return randint(0,99999999)
    
    def idMember(self, id):
        for i in self.members:
            if i['id']==int(id):
                return i
        return None
   