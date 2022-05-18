from flask_restx import Namespace
from .models import DBScale, Movies
from flask import request, Response, jsonify
from .app import app


con = Namespace("authentications",
                   description="Authentications")


@con.route("/")
def welcome():
    return "<p>Welcome to Flasks!</p>"


@app.route("/home")
def home():
    data = json.loads()
    data = BDScale(sno=data[sno], title=data[title], desc=data[desc])
    db.session.add(new_movie)
    db.session.commit()
    return Response(data)


@app.route("/movies_list/<int:id>", methods=["GET"])
def movies_list():
    movie = [Movies.json(movies) for movies in Movies.query.filter_by(id=id)]
    return jsonify({'movie': movie})


@app.route("/user/<int:id>", methods=["GET"])
def user_litss():
    user = Movie.db.user.find_one({'_id': ObjectId(id)})
    userr = dumps(user)
    return userr
