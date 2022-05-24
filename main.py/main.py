# from flask import Flask
# from flask_restful import Api, Resource
# import json

# app = Flask(__name__)
# api = Api(app)
# @app.route('/')
# def Helloword:
#     return "xvc"

# class HelloWorld(Resource):
#     def get(self):
#         print("x")
#         return "Hello World"

# api.add_resource(HelloWorld,"/helloworld")

# if __name__=="__main__":
#     app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# if __name__=="__main__":
#     app.run(debug=True)


