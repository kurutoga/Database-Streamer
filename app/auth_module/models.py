from app import db
from werkzeug import generate_password_hash, check_password_hash

class Base(db.Model):

    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())


class User(Base):

    __tablename__ = 'Users'
    __bind_key__  = 'auth'

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)
    role = db.Column(db.SmallInteger, nullable=False)
    table = db.Column(db.String(30), nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, name, email, password, role, status, table):
        self.name = name
        self.email = email
        self.set_pass(password)
        self.table = table
        self.role = role
        self.status = status

    def set_pass(self, p):
        self.password = generate_password_hash(p)

    def check_pass(self, p):
        return check_password_hash(self.password, p)

    def is_authenticated(self):
        return True

    def get_table(self):
        return self.table

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.name)


