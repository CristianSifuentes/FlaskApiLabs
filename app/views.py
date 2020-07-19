from flask import jsonify
from flask import Blueprint
from .models.task import Task
from .response import response
from .response import not_found

api_v1 = Blueprint('api',__name__, url_prefix='/api/v1')

@api_v1.route('/')
def index():
    return 'Hello!'

@api_v1.route('/tasks', methods=['GET'])
def get_tasks():
     tasks = Task.query.all()
     return response([
           task.serialize() for task in tasks
     ])


@api_v1.route('/tasks/<id>', methods=['GET'])
def get_task(id):
     task = Task.query.filter_by(id=id).first()
     
     if task is None:
          return not_found()
          
     return response([
           task.serialize()
     ])

@api_v1.route('/tasks', methods=['POST'])
def create_task():
      return jsonify({
           'message': '/task/create_task'
      })
   
@api_v1.route('/tasks/<id>', methods=['PUT'])
def update_task():
    return jsonify({
           'message': '/task/update_task'
      })
   
@api_v1.route('/tasks/<id>', methods=['DELETE'])
def delete_task():
       return jsonify({
           'message': '/task/delete_task'
      })