from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__,template_folder="authentications/templates")




"""
DataBase Settings SQLAlchemy

"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)





if __name__ =='__main__':
  app.run(debug = True)
