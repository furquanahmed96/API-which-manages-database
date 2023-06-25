from flask import Flask, request
from flask_restful import Resource, Api
from greenbay import lakers 

app = Flask(__name__)
api = Api(app)

db = lakers() 

class Player(Resource):
    def get(self, player_id):
        query = {"_id": player_id}
        player = db.get_player(query)
        return player

    def post(self):
        
        player_data = request.get_json(force=True) 
        result = db.add_player(player_data)
        return {"result": result}

    def put(self, player_id):
        
        update_data = request.get_json(force=True)
        result = db.update_player(player_id, update_data)
        return {"result": result}

    def delete(self, player_id):
        result = db.delete_player(player_id)
        return {"result": result}

api.add_resource(Player, "/player", "/player/<player_id>")

class Query(Resource):
    def post(self):
        query = request.get_json(force=True)
        result = db.perform_query(query)
        return result

api.add_resource(Query, "/query")

if __name__ == "__main__":
    app.run(debug=True)
