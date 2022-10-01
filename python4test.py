from flask import Flask,request,jsonify
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)


class Hellow (Resource):
    def get(self):
        return jsonify({'message':"hellow world"})
    
    def post(self):
        data=request.get_json()
        return jsonify ({'data':data})

class Square (Resource):
    def get (self,num):
         return jsonify({'square':num**2})

api.add_resource(Hellow,'/')
api.add_resource(Square,'/square/<int:num>')

if __name__=="__main__":
    app.run(debug=True)