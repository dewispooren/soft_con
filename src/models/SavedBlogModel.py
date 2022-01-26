from marshmallow import fields, Schema
import datetime
from . import db
from .BlogModel import BlogSchema, ListBlogSchema


class SavedBlog(db.Model):
    __tablename__ = 'saved_blogs'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'users.id', ondelete='CASCADE'))
    user = db.relationship('UserModel', lazy='joined')
    blog_id=db.Column(db.Integer(),db.ForeignKey(
        'blogs.id',ondelete='CASCADE'
    ))
    blog = db.relationship('Blog', lazy='joined')
    created_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.blog_id = data.get("blog_id")
        self.user_id = data.get("user_id")
        self.created_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def control_by_blog_and_user(blog_id, user_id):
        return SavedBlog.query.any(SavedBlog.user_id == user_id, SavedBlog.blog_id == blog_id)
    
    @staticmethod
    def saved_blogs_by_user_id(user_id):
        return SavedBlog.query.filter(SavedBlog.user_id == user_id).all()


class SavedBlogSchema(Schema):
    blog_id = fields.Int(required=True)
    user_id = fields.Int(required=True)


class ListSavedBlogSchema(Schema):
    blogs = fields.List(fields.Nested(BlogSchema))