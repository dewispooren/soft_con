from flask import request, Blueprint,  make_response
from ...models.BlogModel import Blog, BlogSchema

panel_blog_api = Blueprint('panel_blog_api', __name__)
blog_schema = BlogSchema()



@panel_blog_api.route('/', methods=['POST'])
def create():
  """
  Create User Function
  """
  req_data = request.get_json()
  data = blog_schema.load(req_data)
  blog = Blog(data)
  blog.save()
  ser_data = blog_schema.dump(blog)
  print(ser_data)

  return make_response(ser_data,200)

@panel_blog_api.route('/', methods=['GET'])

def get_all():
  """
  Get all users
  """
  blogs = Blog.get_all_blog()
  ser_blogs = blog_schema.dump(blogs, many=True)
  blogs_dict = {"blogs":ser_blogs}
  return make_response(blogs_dict)


@panel_blog_api.route('/<int:id>', methods=['GET'])
def get_by_id(id):
  """
  Get a single user
  """
  blog = Blog.get_blog_by_id(id)
  if not blog:
    return make_response({'error': 'Blog not found'}, 404)
  
  ser_blog = blog_schema.dump(blog)
  return make_response(ser_blog)


@panel_blog_api.route('/<int:id>', methods=['PUT'])

def update(id):
  """
  Update user
  """
  req_data = request.get_json()
  data = blog_schema.load(req_data, partial=True)

  blog = Blog.get_blog_category_by_id(id)
  blog.update(data)
  ser_blog = blog_schema.dump(blog)
  return make_response(ser_blog)

@panel_blog_api.route('/<int:id>', methods=['DELETE'])

def delete(id):
  """
  Delete a user
  """
  blog = Blog.get_blog_by_id(id)
  blog.delete()
  return make_response({'message': 'deleted'},200)


@panel_blog_api.route('/switch-publish/<int:id>', methods=['GET'])

def switch_publish(id):
  """
  Delete a user
  """
  blog = Blog.switch_publish(id)
  return make_response({'message': 'success'},200)



@panel_blog_api.route('/switch-feature/<int:id>', methods=['GET'])

def switch_feature(id):
  """
  Delete a user
  """
  blog = Blog.switch_feature(id)
  return make_response({'message': 'success'},200)

