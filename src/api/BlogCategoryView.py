
from flask import Blueprint,  make_response
from ..models.BlogCategoryModel import BlogCategory, BlogCategorySchema, ListBlogCategorySchema

blog_category_api = Blueprint('blog_category_api', __name__)
blog_category_schema = BlogCategorySchema()
list_blog_category = ListBlogCategorySchema()


@blog_category_api.route('/', methods=['GET'])
def get_active_blog_categories():
  """
  Get all users
  """
  blog_categories = BlogCategory.get_active_blog_categories()
  ser_blog_categories = list_blog_category.dump(blog_categories, many=True)
  blog_categories_dict = {"blog_categories":ser_blog_categories}
  return make_response(blog_categories_dict)



@blog_category_api.route('/<slug>', methods=['GET'])
def get_by_slug(slug):
  """
  Get a single user
  """
  blog_category = BlogCategory.get_blog_category_by_slug(slug)
  if not blog_category:
    return make_response({'error': 'Blog category not found'}, 404)
  
  ser_blog_category = blog_category_schema.dump(blog_category)
  return make_response(ser_blog_category)



