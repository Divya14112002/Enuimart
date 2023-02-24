from application.database import db
from flask_login import UserMixin

class registration(db.model,UserMixin):
    __tablename__ = 'registration'
    UserId = db.Column(db.Integer(),primary_key=True,autoincrement=False)
    firstname = db.Column(db.String(),nullable=False)
    middlename = db.Column(db.String(),nullable=True)
    lastname = db.Column(db.String(),nullable=True)
    email = db.Column(db.String(),nullable=False)
    password = db.Column(db.String(255),nullable=False)
    phonenumber = db.Column(db.Integer(),nullable=False)
    gender = db.Column(db.String(),nullable=False)
    age = db.Column(db.Integer(),nullable=False)

    def __init__(self,fname,mname,lname,e,pw,phn,g,a,ui):
        self.firstname=fname
        self.middlename=mname
        self.lastname=lname
        self.email=e
        self.password=pw
        self.phonenumber=phn
        self.gender=g
        self.age=a 
        self.UserId=ui

class tweet(db.model,UserMixin):
    __tablename__ = 'tweet'
    tweetid = db.Column(db.Integer(),primary_key=True,autoincrement=False)
    tweetmessage = db.Column(db.String(),nullable=Flase)
    UserId = db.Column(db.Integer(),nullable=Flase)
    created = db.Column(db.String(),nullable=Flase)

    def __init__(self,tid,desc,c,uid,d):
        self.tweetid=tid
        self.tweetmessage=desc
        self.created=c
        self.userId=uid
    


