from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# what do these commands do?
app = Flask(__name__)
api = Api(app) # wrap app in api
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
# define models in database

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name= {self.name}, views={self.views}, likes={self.likes})"

# with app.app_context():
#     db.create_all()



video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", location = 'form', required = True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", location = 'form', required = True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required", location = 'form', required = True)

#how to serialize an object

resource_fields = {
    'if' : fields.Integer,
    'name' : fields.String,
    'views' : fields.Integer,
    'likes' : fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields) # when we return take return value and serialize using the defined fields
    def get(self, video_id):
        result = VideoModel.query.get(id=video_id)
        return 
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args # dictionary stores all values passed in
        video = VideoModel(id = video_id, name = args['name'], views = args['views'], likes = args['likes'])
        db.session.add(video) # add object to current database session
        db.session.commit # make permanent changes to db

        return video, 201
    
    # def delete(self, video_id):
    #     abort_if_video_id_doesnt_exist(video_id)
    #     del videos[video_id]
    #     return '', 204

api.add_resource(Video, "/video/<int:video_id>/")



if __name__ == "__main__":
    app.run(debug=True)

