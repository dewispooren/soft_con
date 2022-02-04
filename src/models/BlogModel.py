from marshmallow import fields, Schema
import datetime
from .BlogCategoryModel import BlogCategory, ListBlogCategorySchema
from . import db
from slugify import slugify
from sqlalchemy import asc, desc, func, or_,and_



class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer(), db.ForeignKey(
        'blog_categories.id', ondelete='CASCADE'))
    category = db.relationship('BlogCategory', lazy='joined')
    tags = db.Column(db.String)
    publisher = db.Column(db.String,nullable=False)
    title = db.Column(db.String,nullable=False)
    slug = db.Column(db.String, nullable=False)
    short_text = db.Column(db.String,nullable=False)
    content = db.Column(db.String,nullable=False)
    featured_photo = db.Column(db.String,nullable=False)
    read_time = db.Column(db.String)
    published_date = db.Column(db.DateTime)
    comment_count = db.Column(db.Integer,server_default='0')
    read_count = db.Column(db.Integer,server_default='0')
    saved_count = db.Column(db.Integer,server_default='0')
    is_published = db.Column(db.Boolean(), server_default='0')
    is_featured= db.Column(db.Boolean(),server_default='0')
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    comments = db.relationship('BlogComment', uselist=True)
  

    def __init__(self, data):
        self.category_id = data.get("category_id")
        self.tags = data.get("tags")
        self.title = data.get("title")
        self.slug = data.get("slug")
        self.short_text = data.get("short_text")
        self.content = data.get("content")
        self.publisher = data.get("publisher")
        self.featured_photo = data.get("featured_photo")
        self.read_time = data.get("read_time")
        self.is_featured = data.get("is_featured")
        self.is_published = data.get("is_published")
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
    def switch_publish(id):
        blog = Blog.query.get(id)
        blog.is_published = not blog.is_published
        if blog.is_published is True:
            blog.published_date = datetime.datetime.utcnow()
        db.session.commit()
    
    @staticmethod
    def switch_feature(id):
        blog = Blog.query.get(id)
        blog.is_featured = not blog.is_featured
        db.session.commit()
    
    @staticmethod
    def get_blogs_by_search_term(search_term):
        return Blog.query.filter(Blog.is_published == True, or_(Blog.title.ilike('%'+search_term+'%'), Blog.tags.ilike('%'+search_term+'%')))

    @staticmethod
    def get_published_blogs_by_category(category_id):
        return Blog.query.filter(and_(Blog.is_published == True, Blog.category_id == category_id)).all()
    
    @staticmethod
    def get_featured_blogs_by_category(category_id):
        return Blog.query.filter(and_(Blog.is_published == True, Blog.category_id == category_id, Blog.is_featured == True)).all()

    @staticmethod
    def get_published_blogs():
        return Blog.query.filter(Blog.is_published == True).all()

    @staticmethod
    def get_featured_blogs():
        return Blog.query.filter(Blog.is_featured == True, Blog.is_published == True).all()

    @staticmethod
    def get_all_blog():
        return Blog.query.all()
    
    @staticmethod
    def get_blog_by_slug(slug):
        return  Blog.query.filter(and_(Blog.is_published == True, Blog.slug == slug)).first()

    @staticmethod
    def get_blog_by_id(id):
        return Blog.query.get(id)


class BlogSchema(Schema):
    id = fields.Int(dump_only=True)
    category_id = fields.Int(required=True)
    slug = fields.Str(required=True)
    tags = fields.Str()
    title = fields.Str(required=True)
    short_text = fields.Str(required=True)
    content = fields.Str(required=True)
    publisher = fields.Str(required=True)
    featured_photo = fields.Str()
    read_time = fields.Str()
    is_published = fields.Bool()
    is_featured = fields.Bool()


class BlogDetailSchema(Schema):
    id = fields.Int(dump_only=True)
    category = fields.Nested(ListBlogCategorySchema)
    slug = fields.Str(required=True)
    tags = fields.Str(dump_only=True)
    title = fields.Str(dump_only=True)
    short_text = fields.Str(dump_only=True)
    content = fields.Str(dump_only=True)
    publisher = fields.Str(dump_only=True)
    featured_photo = fields.Str(dump_only=True)
    read_time = fields.Str(dump_only=True)
    published_date = fields.DateTime(dump_only=True)
    comment_count = fields.Int(dump_only=True)
    read_count = fields.Int(dump_only=True)
    saved_count = fields.Int(dump_only=True)


class ListBlogSchema(Schema):
    id = fields.Int(dump_only=True)
    category = fields.Nested(ListBlogCategorySchema)
    slug = fields.Str(required=True)
    title = fields.Str(required=True)
    short_text = fields.Str(required=True, dump_only=True)
    publisher = fields.Str(required=True, dump_only=True)
    featured_photo = fields.Str(dump_only=True)
    read_time = fields.Str(dump_only=True)
    published_date = fields.DateTime(dump_only=True)
    comment_count = fields.Int(dump_only=True)
    read_count = fields.Int(dump_only=True)
    saved_count = fields.Int(dump_only=True)

class PanelListBlogSchema(Schema):
    id = fields.Int(dump_only=True)
    category = fields.Nested(ListBlogCategorySchema)
    slug = fields.Str(required=True)
    title = fields.Str(required=True)
    is_published = fields.Bool()
    is_featured = fields.Bool()
 




    


