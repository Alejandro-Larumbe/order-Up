from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Column, Table, ForeignKey
from sqlalchemy.types import String, Integer, Float
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class Employee(db.Model, UserMixin):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    employee_number = Column(Integer, nullable=False, unique=True)
    hashed_password = Column(String(100), nullable=False)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Menu(db.Model):
    __tablename__ = 'menus'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

    items = relationship('MenuItem', back_populates='menu')


class MenuItem(db.Model):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    menu_id = Column(Integer, ForeignKey('menus.id'), nullable=False)
    menu_type_id = Column(
        Integer, ForeignKey('menu_item_types.id'), nullable=False)
    type = relationship('MenuItemType')
    menu = relationship('Menu', back_populates='items')


class MenuItemType(db.Model):
    __tablename__ = 'menu_item_types'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

class Table(db.Model):
    __tablename__ = 'tables'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False, unique=True)
    capacity = Column(Integer, nullable=False)