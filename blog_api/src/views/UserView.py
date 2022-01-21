#/src/views/UserView

from flask import request, Blueprint,  make_response
from ..models.UserModel import UserModel, UserSchema

user_api = Blueprint('user_api', __name__)
user_schema = UserSchema()

@user_api.route('/', methods=['POST'])
def create():
  """
  Create User Function
  """
  req_data = request.get_json()
  data = user_schema.load(req_data)
  
  # check if user already exist in the db
  user_in_db = UserModel.get_user_by_email(data.get('email'))
  if user_in_db:
    message = {'error': 'User already exist, please supply another email address'}
    return make_response(message, 400)
  
  user = UserModel(data)
  user.save()
  ser_data = user_schema.dump(user)
  print(ser_data)

  return make_response(ser_data,200)

@user_api.route('/', methods=['GET'])

def get_all():
  """
  Get all users
  """
  users = UserModel.get_all_users()
  ser_users = user_schema.dump(users, many=True)
  users_dict = {"users":ser_users}
  return make_response(users_dict)

@user_api.route('/<int:user_id>', methods=['GET'])
def get_a_user(user_id):
  """
  Get a single user
  """
  user = UserModel.get_one_user(user_id)
  if not user:
    return make_response({'error': 'user not found'}, 404)
  
  ser_user = user_schema.dump(user)
  return make_response(ser_user)

@user_api.route('/<int:user_id>', methods=['PUT'])

def update(user_id):
  """
  Update user
  """
  req_data = request.get_json()
  data = user_schema.load(req_data, partial=True)

  user = UserModel.get_one_user(user_id)
  user.update(data)
  ser_user = user_schema.dump(user)
  return make_response(ser_user)

@user_api.route('/<int:user_id>', methods=['DELETE'])

def delete(user_id):
  """
  Delete a user
  """
  user = UserModel.get_one_user(user_id)
  user.delete()
  return make_response({'message': 'deleted'},200)






  

