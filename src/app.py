#src/app.py
import flask
from flask import Flask
from flask_cors import CORS, cross_origin

from .config import app_config
from .models import db, bcrypt

# import user_api blueprint

from .api.BlogView import blog_api as blog_blueprint
from .api.BlogCategoryView import blog_category_api as blog_category_blueprint
from .api.ProfileView import profile_api as profile_blueprint

from .api.panel.UserView import panel_user_api as panel_user_blueprint
from .api.panel.Blog import panel_blog_api as panel_blog_blueprint
from .api.panel.BlogCategory import panel_blog_category_api as panel_blog_category_blueprint


def create_app():
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config["development"])
  CORS(app)

  # initializing bcrypt and db
  bcrypt.init_app(app)
  db.init_app(app)

  
  app.register_blueprint(blog_blueprint, url_prefix='/api/v1/blog')
  app.register_blueprint(blog_category_blueprint, url_prefix='/api/v1/blog-category')
  app.register_blueprint(profile_blueprint, url_prefix='/api/v1/profile')

  app.register_blueprint(panel_user_blueprint, url_prefix='/panel/api/v1/users')
  app.register_blueprint(panel_blog_blueprint, url_prefix='/panel/api/v1/blog')
  app.register_blueprint(panel_blog_category_blueprint, url_prefix='/panel/api/v1/blog-category')

  @app.route('/', methods=['GET'])
  @cross_origin()
  def index():
    """
    example endpoint
    """
    return 'Congratulations! Your part 2 endpoint is working'

  return app

