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
    checklist_ids = user['checklists_ids']
    checklists = db.checklists.find({'_id': {"$in": checklist_ids}})


@app.route('/checklist/create/user_id', methods=['POST'])
def checklist_create(user_id):
    checklist = {}
    checklist['_id'] = ObjectId()
    checklist['name'] = request.json['name']
    checklist['items'] = []
    mongo.db.checklists.insert_one(checklist)
    mongo.db.user.update({'_id':user_id}, {"$push": {"checklist_ids": checklist['_id']}})

@app.route('/checklist/create/checklist_id', methods=['POST'])
def checklist_create(user_id):
    item = {}
    item['name'] = request.json['name']
    item['checked'] = False
    mongo.db.checklists.update({'_id': checklist_id}, {"$push": {'items': item}})


@app.route('/checklist_id/item_index', methods=['POST'])
def mark_done(checklist_id, item_index):
    mongo.db.user.update({'_id': checklist_id}, {"$set": {'items.'+str(item_index)+'.checked': True}})