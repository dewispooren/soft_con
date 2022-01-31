from bcrypt import re
from marshmallow import fields, Schema
import datetime
from . import db
from .BlogModel import Blog, ListBlogSchema


class BlogRead(db.Model):
    __tablename__ = 'blog_reads'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'users.id', ondelete='CASCADE'))
    user = db.relationship('UserModel', lazy='joined')
    blog_id=db.Column(db.Integer(),db.ForeignKey(
        'blogs.id',ondelete='CASCADE'
    ))
    blog = db.relationship('Blog', lazy='joined')
    count= db.Column(db.Integer,server_default='1')
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.blog_id = data.get("blog_id")
        self.user_id = data.get("user_id")
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    
    def save(self):
        db.session.add(self)
        blog = db.session.query(Blog).get(self.blog_id)
        blog.read_count=blog.read_count +1 
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()
    
    @staticmethod
    def control_by_blog_and_user(blog_id, user_id):
        return BlogRead.query.any(BlogRead.user_id == user_id, BlogRead.blog_id == blog_id)
    
    @staticmethod
    def read_blogs_by_user_id(user_id):
        return BlogRead.query.filter(BlogRead.user_id == user_id).all()
    
    @staticmethod
    def read_blogs_ids_by_user_id(user_id):
        blog_ids_values = BlogRead.query.filter(BlogRead.user_id == user_id).with_entities(BlogRead.blog_id).all()
        return [value for (value,) in blog_ids_values]


class BlogReadSchema(Schema):
    blog_id = fields.Int(required=True)
    user_id = fields.Int(required=True)


class ReadBlogsSchema(Schema):
    blog = fields.Nested(ListBlogSchema)



