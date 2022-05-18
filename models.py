from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class DBScale(db.Model):
  sno=db.Column(db.Integer, primary_key=True)
  title= db.Column(db.String(100), nullable=False)
  desc =db.Column(db.String(100), nullable=False)

  def __repr__(self):
    return self.title



class Movie(db.Model):
    __tablename__ = 'movies'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)
