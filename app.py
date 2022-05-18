from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request,Response,jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)




  
  
  



@app.route("/")
def hello_world():
  return "<p>Welcome to Flask!</p>"



@app.route("/home")
def home():
  data = json.loads()
  data = BDScale(sno=data[sno],title=data[title],desc = data[desc])
  db.session.add(new_movie)
  db.session.commit()
  return Response(data)


@app.route("/movies_list/<int:id>",methods=["GET"] )
def movies_list():
  movie = [Movies.json(movies) for movies in Movies.query.filter_by(id = id)]
  return jsonify({'movie': movie})

  

# MongoDB User Data :<List>\\\\\\\\\\\\\\\\\\\\

# @app.route("/home")
# def home():
#   users = Movie.db.user.find()
#   usere = dumps(users)
#   return usere

@app.route("/user/<int:id>",methods=["GET"])
def user_litss():
  user = Movie.db.user.find_one({'_id':ObjectId(id)})
  userr = dumps(user)
  return userr





if __name__ == "__main__":
  app.run(debug=False)
  
  