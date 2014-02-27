from  datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from werkzeug.security import check_password_hash, generate_password_hash

from pyvly.database import Model


class Post(Model):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    content = Column(Text)
    burn_after = Column(DateTime)
    random_token = Column(Text)
    privly_application = Column(String(100))

    def __init__(self, content, burn_after, random_token, privly_application):
        self.content = content
        self.burn_after = burn_after
        self.random_token = random_token
        self.privly_application = privly_application


class User(Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    salt = Column(String(100))
    created = Column(DateTime)
    updated = Column(DateTime)
    confirmation_token = Column(String)
    verified = Column(Boolean, default=False)

    def __init__(self, email, password, token):
        self.email = email
        self.password = generate_passsword_hash(password=password,
                                                method='pbkdf2:sha512',
                                                salt_length=128)
        self.created = datetime.now()
        self.updated = self.created
        self.confirmation_token = token

    def check_password(self, password):
        return check_password_hash(self.password, password)
