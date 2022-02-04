from flask import request, Blueprint,  make_response
from flask_cors import cross_origin
from ...models.BlogCategoryModel import BlogCategory, BlogCategorySchema, ListBlogCategorySchema
from ...shared.Authentication import Auth

panel_blog_category_api = Blueprint('panel_blog_category_api', __name__)
blog_category_schema = BlogCategorySchema()
list_blog_category = ListBlogCategorySchema()


@panel_blog_category_api.route('/', methods=['POST'])
@cross_origin()
@Auth.admin_auth_required
def create():
  """
  Create User Function
  """
  req_data = request.get_json()
  data = blog_category_schema.load(req_data)
  blog_category = BlogCategory(data)
  blog_category.save()
  ser_data = blog_category_schema.dump(blog_category)
  print(ser_data)

  return make_response(ser_data,200)

@panel_blog_category_api.route('/', methods=['GET'])
@cross_origin()
@Auth.admin_auth_required
def get_all():
  """
  Get all users
  """
  blog_categories = BlogCategory.get_all_blog_categories()
  ser_blog_categories = list_blog_category.dump(blog_categories, many=True)
  blog_categories_dict = {"blog_categories":ser_blog_categories}
  return make_response(blog_categories_dict)


@panel_blog_category_api.route('/<int:id>', methods=['GET'])
@cross_origin()
@Auth.admin_auth_required
def get_by_id(id):
  """
  Get a single user
  """
  blog_category = BlogCategory.get_blog_category_by_id(id)
  if not blog_category:
    return make_response({'error': 'Blog category not found'}, 404)
  
  ser_user = blog_category_schema.dump(blog_category)
  return make_response(ser_user)


@panel_blog_category_api.route('/<int:id>', methods=['PUT'])
@cross_origin()
@Auth.admin_auth_required
def update(id):
  """
  Update user
  """
  req_data = request.get_json()
  data = blog_category_schema.load(req_data, partial=True)

  blog_category = BlogCategory.get_blog_category_by_id(id)
  blog_category.update(data)
  ser_blog_cateory = blog_category_schema.dump(blog_category)
  return make_response(ser_blog_cateory)

@panel_blog_category_api.route('/<int:id>', methods=['DELETE'])
@cross_origin()
@Auth.admin_auth_required
def delete(id):
  """
  Delete a user
  """
  blog_category = BlogCategory.get_blog_category_by_id(id)
  blog_category.delete()
  return make_response({'message': 'deleted'},200)


@panel_blog_category_api.route('/switch-active/<int:id>', methods=['GET'])
@cross_origin()
@Auth.admin_auth_required
def switch_active(id):
  """
  Delete a user
  """
  blog_category = BlogCategory.switch_active(id)
  return make_response({'message': 'success'},200)
