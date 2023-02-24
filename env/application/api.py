from application.database import db
from application.models import registration,tweet
from flask_restful import Resource,fields,marshal_with,reqparse
from flask import current_app as application

create_registration_parser = reqparse.RequestParser()
create_registration_parser.add_argument('firstname')
create_registration_parser.add_argument('middlename')
create_registration_parser.add_argument('lastname')
create_registration_parser.add_argument('email')
create_registration_parser.add_argument('password')
create_registration_parser.add_argument('age')
create_registration_parser.add_argument('phonenumber')
create_registration_parser.add_argument('gender')
create_registration_parser.add_argument('userId')

registration_output_fields = {
    "firstname" : fields.String,
    "middlename" : fields.String,
    "lastname" : fields.String,
    "email" : fields.String,
    "password" : fields.String,
    "age" : fields.Integer,
    "phonenumber" : fields.Integer,
    "gender" : fields.String,
    "userId": fields.Strin
 } 

class registration_API(Resource):
    @marshal_with(registration_output_fields)
    def post(self):
        args = create_registration_parser.parse_args()
        firstname = args.get('firstname',None)
        middlename = args.get('middlename',None)
        lastname = args.get('lastname',None)
        email = args.get('email',None)
        password = args.get('password',None)
        age = args.get('age',None)
        phonenumber = args.get('phonenumber',None)
        gender = args.get('gender',None)
        userId = args.get('userId',None)

        if firstname is None:
            raise ValidationError(status code=400,error_code="F001",error_message="Firstname is required")
        if email is None:
            raise ValidationError(status code=400,error_code="E001",error_message="Email is required")
        if password is None:
            raise ValidationError(status code=400,error_code="P001",error_message="Password is required")
        if age is None:
            raise ValidationError(status code=400,error_code="A001",error_message="Age is required")  
        if phonenumber is None:
            raise ValidationError(status code=400,error_code="PH001",error_message="phoneNumber is required")   
        if gender is None:
            raise ValidationError(status code=400,error_code="G001",error_message="Gender is required")  
        if userId is None:
            raise ValidationError(status code=400,error_code="U001",error_message="UserId is required")            

        exists = db.session.query(registration).get(registration.userId==userId).first()

        if exists:
            raise ExistsError(status_code=409)

        user=registration(fname=firstname,mname=middlename,lname=lastname,e=email,pw=password,phn=phonenumber,g=gender,a=age,ui=userId)
        db.session.add(user)
        db.session.commit()
        return user    