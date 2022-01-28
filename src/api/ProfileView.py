from flask import request, json, Response, Blueprint, g, make_response
from ..models.UserModel import UserModel, UserSchema
from ..models.BlogReadsModel import BlogRead, ReadBlogsSchema
from ..models.SavedBlogModel import SavedBlog, ListSavedBlogSchema
from ..shared.Authentication import Auth

profile_api = Blueprint('profile_api', __name__)
user_schema = UserSchema()

@profile_api.route('/', methods=['POST'])
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


@profile_api.route('/', methods=['PUT'])
@Auth.auth_required
def update():
  """
  Update me
  """
  req_data = request.get_json()
  data, error = user_schema.load(req_data, partial=True)
  if error:
    return make_response(error, 400)

  user = UserModel.get_one_user(g.user.get('id'))
  user.update(data)
  ser_user = user_schema.dump(user)
  return make_response(ser_user, 200)


@profile_api.route('/', methods=['GET'])
@Auth.auth_required
def get_me():
  """
  Get me
  """
  user = UserModel.get_one_user(g.user.get('id'))
  ser_user = user_schema.dump(user)
  return make_response(ser_user, 200)


@profile_api.route('/read-blogs', methods=['GET'])
@Auth.auth_required
def read_blogs():
  """
  Get me
  """
  read_blog_schema = ReadBlogsSchema()
  print(g.user.get('id'))
  read_blogs = BlogRead.read_blogs_by_user_id(g.user.get('id'))
  print(read_blogs)
  ser_blogs = read_blog_schema.dump(read_blogs, many=True)
  blogs_dict = {"blogs":ser_blogs}
  return make_response(blogs_dict, 200)


@profile_api.route('/saved-blogs', methods=['GET'])
@Auth.auth_required
def saved_blogs():
  """
  Get me
  """
  saved_blog_schema = ListSavedBlogSchema()
  saved_blogs = SavedBlog.saved_blogs_by_user_id(g.user.get('id'))
  ser_blogs = saved_blog_schema.dump(saved_blogs, many=True)
  blogs_dict = {"blogs":ser_blogs}
  return make_response(blogs_dict, 200)



@profile_api.route('/login', methods=['POST'])
def login():
  """
  User Login Function
  """
  req_data = request.get_json()

  data = user_schema.load(req_data)
  if not data.get('email') or not data.get('password'):
    return make_response({'error': 'you need email and password to sign in'}, 400)
  user = UserModel.get_user_by_email(data.get('email'))
  if not user:
    return make_response({'error': 'invalid credentials'}, 400)
  if not user.check_hash(data.get('password')):
    return make_response({'error': 'invalid credentials'}, 400)
  ser_data = user_schema.dump(user)
  token = Auth.generate_token(ser_data.get('id'))
  print(token)
  return make_response({'jwt_token': token}, 200)


@profile_api.route('/register', methods=['POST'])
def register():
  """
  User Register Function
  """
  req_data = request.get_json()
  

  data = user_schema.load(req_data)
  if not data.get('email') or not data.get('password'):
    return make_response({'error': 'you need email and password to sign in'}, 400)
  user_in_db = UserModel.get_user_by_email(data.get('email'))
  if user_in_db:
    message = {'error': 'User already exist, please supply another email address'}
    return make_response(message, 400)
  user = UserModel(data)
  user.save()
  ser_data = user_schema.dump(user)
  token = Auth.generate_token(ser_data.get('id'))
  return make_response({'jwt_token': token}, 200)

