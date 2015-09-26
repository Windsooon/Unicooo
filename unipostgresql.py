#! /usr/bin/env python
# coding=utf-8
from peewee import *
psql_db = PostgresqlDatabase('unicooo_postgre_sql', user='windson_postgre')


class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    uid = IntegerField()
    user_name = CharField(unique=True) 
    user_email = CharField(unique=True) 
    user_pass = CharField() 
    user_salt = CharField()
    user_registeredTime = DateTimeField()
    user_portrait_url = CharField()
    user_point = IntegerField()
    user_message = TextField()  


class Act(BaseModel):
    act_id =IntegerField()
    user_id = ForeignKeyField(User, related_name='users_id')  
    act_title = TextField()
    act_content = TextField()
    act_thumb_url = CharField()
    act_ident = CharField()
    act_type = IntegerField()
    act_star = IntegerField()
    act_alias = CharField()
    act_status = IntegerField() 
    act_url = CharField()
    act_date_gmt = TimeField()
    act_delete = CharField()
    update_by = CharField()
    update_time = TimeField()


class Post(BaseModel):
    post_id = BigIntegerField()
    user_id = ForeignKeyField(User, related_name='users_id2') 
    act_id = ForeignKeyField(Act, related_name='acts_id')
    post_privacy = CharField() 
    post_title = CharField()
    post_content = TextField()
    post_thumb_url = CharField()
    post_thumb_height = 
    post_date_gmt = DateTimeField()
    post_likes_count = IntegerField()
    post_comments_count = IntegerField()
    post_views_count = IntegerField()


class Comment(BaseModel):
    comment_id = BigIntegerField()
    post_id = ForeignKeyField(Post, related_name='posts_id')
    user_id = ForeignKeyField(User, related_name='users_id3')
    reply_id = BigIntegerField()
    comment_content = TextField()
    comment_date_gmt = DateTimeField()


class User_permi(BaseModel):
    id = IntegerField() 
    uid = ForeignKeyField(User, related_name='users_id4')     
    act_id = ForeignKeyField(Act, related_name='acts_id2') 
    user_per = IntegerField()


db.connect()

try:
    with db.transaction():
        user = User.create(
            user_name = 'w1ll' ,
            user_salt = 's1l' ,
            user_pass = 'l1s',
            user_email = '122',
            user_time = '1ws'
        )
            
except IntegrityError as e:
    print e


