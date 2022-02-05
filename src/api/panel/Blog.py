from flask import request, Blueprint,  make_response
from flask_cors import cross_origin
from ...models.BlogModel import Blog, BlogSchema, PanelListBlogSchema
from ...shared.Authentication import Auth

panel_blog_api = Blueprint('panel_blog_api', __name__)
blog_schema = BlogSchema()
list_blog_schema = PanelListBlogSchema()


@panel_blog_api.route('/', methods=['POST'])
@cross_origin()
@Auth.admin_auth_required
def create():
  req_data = request.get_json()
  data = blog_schema.load(req_data)
  print(data)
  blog = Blog(data)
  blog.save()
  ser_data = blog_schema.dump(blog)
  print(ser_data)

  return make_response(ser_data,200)

@panel_blog_api.route('/', methods=['GET'])
@cross_origin()
@Auth.admin_auth_required
def get_all():
  blogs = Blog.get_all_blog()
  ser_blogs = list_blog_schema.dump(blogs, many=True)
  blogs_dict = {"blogs":ser_blogs}
  return make_response(blogs_dict)


@panel_blog_api.route('/<int:id>', methods=['GET'])
@cross_origin()
@Auth.admin_auth_required
def get_by_id(id):
  blog = Blog.get_blog_by_id(id)
  if not blog:
    return make_response({'error': 'Blog not found'}, 404)
  
  ser_blog = blog_schema.dump(blog)
  return make_response(ser_blog)


@panel_blog_api.route('/<int:id>', methods=['PUT'])
@cross_origin()
@Auth.admin_auth_required
def update(id):
  req_data = request.get_json()
  data = blog_schema.load(req_data, partial=True)

  blog = Blog.get_blog_by_id(id)
  blog.update(data)
  ser_blog = blog_schema.dump(blog)
  return make_response(ser_blog)

@panel_blog_api.route('/<int:id>', methods=['DELETE'])
@cross_origin()
@Auth.admin_auth_required
def delete(id):
  blog = Blog.get_blog_by_id(id)
  blog.delete()
  return make_response({'message': 'deleted'},200)


@panel_blog_api.route('/switch-publish/<int:id>', methods=['GET'])
@cross_origin()
@Auth.admin_auth_required
def switch_publish(id):
  blog = Blog.switch_publish(id)
  return make_response({'message': 'success'},200)



@panel_blog_api.route('/switch-feature/<int:id>', methods=['GET'])
@Auth.admin_auth_required
def switch_feature(id):
  blog = Blog.switch_feature(id)
  return make_response({'message': 'success'},200)

