from flask import Flask
from flask import request
from flask_cors import CORS
import json
app = Flask(__name__)
arr=[]
CORS(app)
@app.route('/')
def home():
    return 'Masai Home Page'


@app.route("/items")
def items():
    items = []
    fl = open("items_list")
    for ln in fl:
        item = ln.split()
        items.append({'items': item[0], "qty": item[1]})
    fl.close()

    return json.dumps({"items": items})

@app.route('/add', methods=['POST'])
def add():
    item = request.json["item"]
    qty = request.json["qty"]
    fl=open("items_list","a")
    fl.write(item + " " + qty + "\n")
    fl.close()
    return json.dumps({"message": "Item Created"})

@app.route('/edit/<int:line_no>', methods=['POST'])
def edit(line_no):
    curr_line = 0
    new_lines = []
    item = request.json["item"]
    qty = request.json["qty"]
    fl = open("items_list")
    for ln in fl:
        if curr_line == line_no-1:
            new_lines.append(item + " " + qty + "\n")
        else:
            new_lines.append(ln)
        curr_line = curr_line + 1
    fl.close()

    new_fl = open('items_list', "w")
    for itm in new_lines:
        new_fl.write(itm)
    new_fl.close()
    
    return json.dumps({"message": "Item Changed"})
    
@app.route('/delete/<int:line_no>')
def delete(line_no):
    curr_line = 0
    new_lines = []
    fl = open("items_list")
    for ln in fl:
        if curr_line != line_no:
            new_lines.append(ln)            
        curr_line = curr_line + 1
    fl.close()

    new_fl = open('items_list', "w")
    for itm in new_lines:
        new_fl.write(itm)
    new_fl.close()
    
    return json.dumps({"message": "Item Deleted"})