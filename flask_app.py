from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def post_data_validation(data):
	if "X" in data.keys() and "Y" in data.keys():
		return True
	else:
		return False

class Add(Resource):
	def post(self):
		data = request.get_json()
		if post_data_validation(data):
			X = data["X"]
			Y = data["Y"]
			if type(X) is int and type(Y) is int:
				Z = X+Y
			else:
				return jsonify({"Message": "X and Y should be numbers.", "Status Code": 402})
			return jsonify({"Message": Z, "Status Code": 200})
		else:
			return jsonify({"Message": "Either X or Y is missing.", "Status Code": 403})

api.add_resource(Add, "/add")

class Sub(Resource):
	def post(self):
		data = request.get_json()
		if post_data_validation(data):
			X = data["X"]
			Y = data["Y"]
			if type(X) is int and type(Y) is int:
				Z = X-Y
			else:
				return jsonify({"Message": "X and Y should be numbers.", "Status Code": 402})
			return jsonify({"Message": Z, "Status Code": 200})
		else:	
			return jsonify({"Message": "Either X or Y is missing.", "Status Code": 403})

api.add_resource(Sub, "/sub")

class Multiply(Resource):
	def post(self):
		data = request.get_json()
		if post_data_validation(data):
			X = data["X"]
			Y = data["Y"]
			if type(X) is int and type(Y) is int:
				Z = X*Y
			else:
				return jsonify({"Message": "X and Y should be numbers.", "Status Code": 402})
			return jsonify({"Message": Z, "Status Code": 200})
		else:
			return jsonify({"Message": "Either X or Y is missing.", "Status Code": 403})

api.add_resource(Multiply, "/multiply")

class Divide(Resource):
	def post(self):
		data = request.get_json()
		if post_data_validation(data):
			X = data["X"]
			Y = data["Y"]
			if type(X) is int and type(Y) is int:
				if Y != 0:
					Z = X*Y
				else:
					return jsonify({"Message": "Y can not be zero.", "Status Code": 401})
			else:
				return jsonify({"Message": "X and Y should be numbers.", "Status Code": 402})
			return jsonify({"Message": Z, "Status Code": 200})
		else:
			return jsonify({"Message": "Either X or Y is missing.", "Status Code": 403})

api.add_resource(Divide, "/divide")

if __name__ == "__main__":
	app.run()