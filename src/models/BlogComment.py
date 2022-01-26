from marshmallow import fields, Schema
import datetime
from . import db



class BlogComment(db.Model):
    __tablename__ = 'blog_comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'users.id', ondelete='CASCADE'))
    blog_id=db.Column(db.Integer(),db.ForeignKey(
        'blogs.id',ondelete='CASCADE'
    ))
    comment=db.Column(db.String,nullable=False)
    like_count=db.Column(db.Integer,server_default='0')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())


class BlogCommentLike(db.Model):
    __tablename__ = 'blog_comment_likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'users.id', ondelete='CASCADE'))
    blog_comment_id=(db.Integer,db.ForeignKey(
        'blogs_comments.id',ondelete='CASCADE'
    ))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
