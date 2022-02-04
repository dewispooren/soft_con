from flask import request, g, Blueprint,  make_response
from flask_cors import cross_origin
from ..models.BlogModel import Blog, BlogDetailSchema, ListBlogSchema
from ..models.BlogReadsModel import BlogRead, BlogReadSchema
from ..models.SavedBlogModel import SavedBlog, SavedBlogSchema
from ..shared.Authentication import Auth

blog_api = Blueprint('blog_api', __name__)
blog_schema = BlogDetailSchema()
list_blog_schema = ListBlogSchema()



@blog_api.route('/', methods=['GET'])
@cross_origin()
def get_published_blogs():
  blogs = Blog.get_published_blogs()
  ser_blogs = list_blog_schema.dump(blogs, many=True)
  blogs_dict = {"blogs":ser_blogs}
  return make_response(blogs_dict)


@blog_api.route('/cat/<id>', methods=['GET'])
@cross_origin()
def get_blogs_by_category(id):
  blogs = Blog.get_published_blogs_by_category(id)
  ser_blogs = list_blog_schema.dump(blogs, many=True)
  blogs_dict = {"blogs":ser_blogs}
  return make_response(blogs_dict)


@blog_api.route('/search/<search_term>', methods=['GET'])
@cross_origin()
def get_blogs_by_search(search_term):
  blogs = Blog.get_blogs_by_search_term(search_term)
  ser_blogs = list_blog_schema.dump(blogs, many=True)
  blogs_dict = {"blogs":ser_blogs}
  return make_response(blogs_dict)


@blog_api.route('/featured/', methods=['GET'])
@cross_origin()
def get_featured_blogs():
  blogs = Blog.get_featured_blogs()
  ser_blogs = list_blog_schema.dump(blogs, many=True)
  blogs_dict = {"blogs":ser_blogs}
  return make_response(blogs_dict)



@blog_api.route('/s/<slug>', methods=['GET'])
@cross_origin()
def get_by_slug(slug):
  blog = Blog.get_blog_by_slug(slug)
  if not blog:
    return make_response({'error': 'Blog not found'}, 404)
  
  ser_blog = blog_schema.dump(blog)
  return make_response(ser_blog)




@blog_api.route('/read/<blog_id>', methods=['GET'])
@cross_origin()
@Auth.auth_required
def read_blog(blog_id):
  blog_read_schema = BlogReadSchema()
  user_id = g.user.get('id')
  req_data = {"blog_id":blog_id, "user_id":user_id}
  data = blog_read_schema.load(req_data)
  blog_read = BlogRead(data) 
  blog_read.save()
  ser_data = blog_read_schema.dump(blog_read)

  return make_response(ser_data)


@blog_api.route('/save/<blog_id>', methods=['GET'])
@cross_origin()
@Auth.auth_required
def save_blog(blog_id)
  saved_blog_schema = SavedBlogSchema()
  user_id = g.user.get('id')
  req_data = {"blog_id":blog_id, "user_id":user_id}
  data = saved_blog_schema.load(req_data)
  saved_blog = SavedBlog(data) 
  saved_blog.save()
  ser_data = saved_blog_schema.dump(saved_blog)

  return make_response(ser_data)