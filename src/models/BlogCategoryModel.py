from marshmallow import fields, Schema
import datetime
from . import db
from slugify import slugify
from sqlalchemy import asc, desc, func, or_,and_


class BlogCategory(db.Model):
    __tablename__ = 'blog_categories'

    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean(),
                       nullable=False, server_default='1')
    name = db.Column(db.String,nullable=False)
    slug = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    
    
    def __init__(self, data):
        self.name = data.get('name')
        self.slug = data.get('slug')
        self.description = data.get('description')
        self.is_active = data.get('is_active')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def switch_active(id):
        category = BlogCategory.query.get(id)
        category.is_active = not category.is_active
        db.session.commit()
    
    @staticmethod
    def get_active_blog_categories():
        return BlogCategory.query.filter(BlogCategory.is_active == True).all()


    @staticmethod
    def get_all_blog_categories():
        return BlogCategory.query.all()
    
    @staticmethod
    def get_blog_category_by_slug(slug):
        return  BlogCategory.query.filter(and_(BlogCategory.is_active == True, BlogCategory.slug == slug)).first()

    @staticmethod
    def get_blog_category_by_id(id):
        return BlogCategory.query.get(id)


class BlogCategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    slug = fields.Str(required=True)
    description = fields.Str()
    is_active = fields.Bool()


class ListBlogCategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    slug = fields.Str(required=True)
