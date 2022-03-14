# mango数据库引擎
from mongoengine import connect,Document,StringField,IntField,ReferenceField
connect('test_mongo',host='localhost',port=27017)


class Users(Document):
    name = StringField(required=True,max_length=20)
    age = IntField(required=True)


class Paper(Document):
    title = StringField(required=True,max_length=50)
    user = ReferenceField(Users)