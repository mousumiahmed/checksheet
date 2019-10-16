from flask import Flask
from flask import request
import json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/dummy"
mongo = PyMongo(app)
    
@app.route('/user/create', methods=['POST'])
def user_create():
    user = {}
    user['_id'] = ObjectId()
    user['name'] = request.json['name']
    user['email'] = request.json['email']
    mongo.db.users.insert(user)
    return dumps(user)

@app.route('user/checklist')
def user_checklists(user_id):
    user = mongo.db.users.find_one({'_id': user_id})
    return user['checklists']

@app.route('/checklist/create/user_id', methods=['POST'])
def checklist_create(user_id):
    checklist = {}
    checklist['name'] = request.json['name']
    checklist['items'] = []
    mongo.db.user.update({'_id': user_id}, {"$push": {"checklists": checklist}})


@app.route('/checklist/create/user_id/index', methods=['POST'])
def items_create(user_id, index):
    item = {}
    item['name'] = request.json['name']
    item['checked'] = False
    mongo.db.user.update({'_id': user_id}, {"$push": {"checklists."+str(index)+'.items': item}})


@app.route('/checklist/create/user_id/index/item_index', methods=['POST'])
def mark_done(user_id, index, item_index):
    mongo.db.user.update({'_id': user_id}, {"$set": {"checklists."+str(index)+'.items.'+str(item_index)+'.checked': True}})