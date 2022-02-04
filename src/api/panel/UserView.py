#/src/views/UserView

from flask import request, Blueprint,  make_response
from flask_cors import cross_origin
from ...models.UserModel import UserModel, UserRoles, UserSchema, UserRoleSchema
from ...shared.Authentication import Auth

panel_user_api = Blueprint('panel_user_api', __name__)
user_schema = UserSchema()
user_role_schema = UserRoleSchema()



@panel_user_api.route('/', methods=['GET'])
@cross_origin()
@Auth.admin_auth_required
def get_all():
  users = UserModel.get_all_users()
  ser_users = user_schema.dump(users, many=True)
  users_dict = {"users":ser_users}
  return make_response(users_dict)

@panel_user_api.route('/<int:user_id>', methods=['GET'])
@cross_origin()
@Auth.admin_auth_required
def get_a_user(user_id):
  user = UserModel.get_one_user(user_id)
  if not user:
    return make_response({'error': 'user not found'}, 404)
  
  ser_user = user_schema.dump(user)
  return make_response(ser_user)

@panel_user_api.route('/<int:user_id>', methods=['PUT'])
@cross_origin()
@Auth.admin_auth_required
def update(user_id):
  req_data = request.get_json()
  data = user_schema.load(req_data, partial=True)

  user = UserModel.get_one_user(user_id)
  user.update(data)
  ser_user = user_schema.dump(user)
  return make_response(ser_user)

@panel_user_api.route('/<int:user_id>', methods=['DELETE'])
@cross_origin()
@Auth.admin_auth_required
def delete(user_id):
  user = UserModel.get_one_user(user_id)
  user.delete()
  return make_response({'message': 'deleted'},200)
  

@panel_user_api.route('/add-role', methods=['POST'])
@cross_origin()
@Auth.admin_auth_required
def add_admin_role(user_id):
  req_data = request.get_json()
  data = user_role_schema.load(req_data)
  user_role = UserRoles(data)
  user_role.save()
  ser_user_role = user_role_schema.dump(user_role)
  return make_response(ser_user_role)






  

