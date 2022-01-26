#src/models/__init__.py

import imp
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize our db
db = SQLAlchemy()
bcrypt = Bcrypt()

from .UserModel import UserModel, Role, UserRoles
from .BlogModel import Blog
from .BlogCategoryModel import BlogCategory
from .BlogComment import BlogComment, BlogCommentLike
from .BlogReadsModel import BlogRead
from .SavedBlogModel import SavedBlog