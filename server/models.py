from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 
    
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("error not name")
        return name
    
    @validates("phone_number")
    def validate_number(self, key, phone_number):
        if len (phone_number) != 10:
            raise ValueError("error less than 10")
        return phone_number

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 
    @validates('category')
    def validate_category(self, key, category):
        if category not in ['Fiction', 'Non-Fiction']:
            raise ValueError ("category must either be fiction or non-fiction")
        return  category
    
    @validates ('content')
    def validate_content(self, key, content):
        if len (content)<250:
            raise ValueError ("content not found, in our database")  
        return content
    
    @validates ('summary')
    def validate_summary(self, key, summary):
        if len (summary)>=250:
            raise ValueError ("summary not found, in our database")
        return summary
    
    @validates ('title')
    def validate_title(self, key, title):
        if not title:
            raise ValueError('title is required')
        if len (title)>100:
            raise ValueError('title is too long')
        clickbait_phrases=['wont believe', 'secret', 'top', 'guess']
        for phrase in clickbait_phrases:
            if phrase.lower() in title.lower():
                return title
            raise ValueError ('title does not contain clickbait_phrases')

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'