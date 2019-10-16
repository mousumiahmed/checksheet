## Week 13 - Day 1

**Express JS**

<https://expressjs.com/>

Installation

```
$ mkdir myapp
$ cd myapp
$ npm init
$ npm install express --save
$ npm install body-parser --save
```

**Getting Started**

```
var express = require('express')
var bodyParser = require('body-parser')
var app = express()
app.use(bodyParser.json())

app.get('/', function (req, res) {
  res.send('hello masai')
})

app.listen(8080)
```

Starting the server

```
$ npm index.js
```

visit - [http://localhost:8080](http://localhost:8080/)

**Routing**

GET

```
app.get('/users/:id', function (req, res) {
  res.json({"params": req.params})
})
```

POST

```
app.post('/create', function (req, res) {
  const data = req.body;
  res.json({"data": data})
})
```

# Week 13 - Day 2

### MongoDB

**Installation** <https://github.com/masai-school/full-stack-dev/wiki/MongoDB-Installation>

**UI Interface** <https://robomongo.org/>

**DB & Collections** <https://docs.mongodb.com/manual/core/databases-and-collections/>

**Create Operations** <https://docs.mongodb.com/manual/crud/#create-operations>

**Read Operations** <https://docs.mongodb.com/manual/crud/#read-operations>

**Update Operations** <https://docs.mongodb.com/manual/crud/#update-operations>

**Delete Operations** <https://docs.mongodb.com/manual/crud/#delete-operations>





# Week 13 - Day 4

### MongoDB

**Document** <https://docs.mongodb.com/manual/core/document/>

**$set** <https://docs.mongodb.com/manual/reference/operator/update/set/>

**$unset** <https://docs.mongodb.com/manual/reference/operator/update/unset/>

**$rename** <https://docs.mongodb.com/manual/reference/operator/update/rename/>

**$push** <https://docs.mongodb.com/manual/reference/operator/update/push/>

**Node & Express Connection**

```
npm install mongodb --save
```

<http://mongodb.github.io/node-mongodb-native/3.3/>

**Basic DB Connection**

```
const MongoClient = require('mongodb').MongoClient;
const ObjectId = require('mongodb').ObjectId;

// Connection URL
const url = 'mongodb://localhost:27017';

// Database Name
const dbName = 'dummy';

// Create a new MongoClient
const client = new MongoClient(url);

let db;

// Use connect method to connect to the Server
client.connect(function(err) {
  db = client.db(dbName);
});
```

## MongoDB

**sort** <https://docs.mongodb.com/manual/reference/method/cursor.sort/>

**limit** <https://docs.mongodb.com/manual/reference/method/cursor.limit/>

**skip** <https://docs.mongodb.com/manual/reference/method/cursor.skip/>

**count** <https://docs.mongodb.com/manual/reference/method/cursor.count/>

## MongoDB

**$eq** <https://docs.mongodb.com/manual/reference/operator/query/eq/>

**$gt** <https://docs.mongodb.com/manual/reference/operator/query/gt/>

**$gte** <https://docs.mongodb.com/manual/reference/operator/query/gte/>

**$in** <https://docs.mongodb.com/manual/reference/operator/query/in/>

**$lt** <https://docs.mongodb.com/manual/reference/operator/query/lt/>

**$lte** <https://docs.mongodb.com/manual/reference/operator/query/lte/>

**$ne** <https://docs.mongodb.com/manual/reference/operator/query/ne/>

**$nin** <https://docs.mongodb.com/manual/reference/operator/query/nin/>

**$inc** <https://docs.mongodb.com/manual/reference/operator/update/inc/>

**$min** <https://docs.mongodb.com/manual/reference/operator/update/min/>

**$max** <https://docs.mongodb.com/manual/reference/operator/update/max/>

**$mul** <https://docs.mongodb.com/manual/reference/operator/update/mul/>

## MongoDB

**$and** <https://docs.mongodb.com/manual/reference/operator/query/and/>

**$or** <https://docs.mongodb.com/manual/reference/operator/query/or/>

**$exists** <https://docs.mongodb.com/manual/reference/operator/query/exists/>

**Mongo Dump** <https://docs.mongodb.com/manual/reference/program/mongodump/>

**Mongo Restore** <https://docs.mongodb.com/manual/reference/program/mongorestore/>

## MongoDB

**$all** <https://docs.mongodb.com/manual/reference/operator/query/all/>

**$elemMatch** <https://docs.mongodb.com/manual/reference/operator/query/elemMatch/>

**$size** <https://docs.mongodb.com/manual/reference/operator/query/size/>

**Query Documents** <https://docs.mongodb.com/manual/tutorial/query-embedded-documents/>

**Query Arrays** <https://docs.mongodb.com/manual/tutorial/query-arrays/>

**Query Array of Documents** <https://docs.mongodb.com/manual/tutorial/query-array-of-documents/>

## MongoDB

<https://docs.mongodb.com/manual/core/data-modeling-introduction/>

<https://docs.mongodb.com/manual/core/data-model-design/>

<https://docs.mongodb.com/manual/core/data-model-operations/>

<https://docs.mongodb.com/manual/tutorial/model-embedded-one-to-one-relationships-between-documents/>

<https://docs.mongodb.com/manual/tutorial/model-embedded-one-to-many-relationships-between-documents/>

<https://docs.mongodb.com/manual/tutorial/model-referenced-one-to-many-relationships-between-documents/>

## Python

<https://xkcd.com/353/>

**Indentation**

```
if 2 > 3:
    print("2 is greater than 2")

if 2 > 3:
print("2 is greater than 3")
```

**Variables**

```
name = "Masai School"
num = 100
dec = 12.50
valid = True
```

**Data Types**
<https://docs.python.org/3/library/datatypes.html>

```
name = "Masai School" # str
num = 100 # int
dec = 12.50 #float
vaild = True # bool
fruits = ["grapes", "oranges", "mangoes"] # list
vegetables = ("carrot", "potato", "onion") # tuple
counter = range(100) # range
user = {"name": "Sid", "age": "21", "gender": "Male"} # dict
```

**Numbers**
<https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex>

```
int` `float` `complex
a = 2
b = 3.14
c = 4+5j
```

Conversion
`int()` `float()` `complex()`

**Strings** <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>

```
a = "Masai"
b = 'School'
c = '''A Transformation in education
learn to earn, pay when you get
'''
name = "Masai School"
for i in name:
	print(i)
```

**Operators**

Arithmetic

```
a + b # addition
a - b # substraction
a * b # multiplication
a / b # division
a % b # modulus
a ** b # exponent
a // b # floor division
```

Comparison

```
a == b # equal
a != b # not equal
a > b # greater than
a < b # less than
a >= b # greater than equal to
a <= b # less than equal to
```

Logical

```
a < 5 and x > 10 # both are true
a < 5 or x < 10 # if one of the statement is true
not (a < 5) # reverse the result
```

**if else**

```
x = 4
y = 5
if x > y:
    print("x is greater than y")
elif:
    print("x and y are equal")
else:
    print("y is greater than x")
```

**while**

```
counter = 10
while counter < 1:
    print(counter)
    counter = counter - 1
```

## Python

**Strings**

<https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>

```
name = "Masai School"
print(name[2]) # character at position 2 starts with 0
print(name[-1]) # negative from last position
print(name[2:5]) # string from position 2 (included) to position 5 (excluded)
print(name[3:]) # string from positon 3 to end
print(name[-5:-3]) # string from position -5 (included) to position -3 (excluded)
print(name[:-4]) # string from starting to -4 

## Length of the string
print(len(name))

## String methods

print(name.lower()) # lower case
print(name.replace("a", "@")) # find and replace

# Concatenation
tag = "A transformation in education"
heading = name + " " + tag

# Check sub string exists in string
if "School" in heading:
    print("School exists in heading")
    
if "for" not in heading:
    print("for doesn't exists in heading")
```

**Sequence Types**

<https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range>

Range

```
range(10)
range(2, 20)
range(5, 50, 5)

range(start, stop, step) # default start is 0 default step is 1

# looping the range
for x in range(10):
    print(x)

# Checking for items in range
if 35 in range(5, 50, 5):
    print("35 exists in range")

if 32 not in range(5, 50, 5):
    print("32 does no exists in range")

# Size/length of range
len(range(5, 50, 5))
```

List

```
students = ["Ajay", "Akshay", "Haren"]
alphabets = ["a", "b", "c", "d", "e"]
primes = [2, 3, 5, 7, 11, 13, 17, 19]

alphabets[2] ## Item at position 2
alphabets[4:] ## Items from position to end

## Size/Length of list
len(primes)

## looping the list
for x in students:
    print(x)
    
## Adding item at the end
students.append("Anusha")

## Adding the item at a particular position
students.insert(2, "Rahul")

## Removing item from the end
students.pop()

## Remove a particular position from the list
students.pop(index)
del students[index]

## Remove the specified item (first occurance)
students.remove(value)

## Remove all the elements of the list
del students
students.clear()

## Count all the occurances
students.count(value)

## Check for existance
if "Ajay" in students:
    print("Ajay is present in students")
    
if "Priyanshu" not in students:
    print("Priyanshu doesn't exist in the list of students")
```

## Python

**Lists** *mutable - liable to change*

```
students_1 = ["Ajay", "Akshay", "Anusha"]
students_2 = ["Anuj", "Amit", "Ravi", "Nitin"]

## Joining Lists
students = students_1 + students_2

## Merging Lists
students_1.extend(students_2)
```

**Tuples** *immutable - unchanging over time*

```
students = ("Ajay", "Akshay", "Anusha", "Vetri", "Rahul", "Mahesh", "Pavan", "Haren")

students[1] ## Item at index 1
students[2:] ## Items from index 2 to end

students.index("Anusha") ## Gives the index of the item if found in the tuple
students.count("Vetri") ## The number of times the item appears in the tuple

len(students) ## Size/Length of the tuple
```

**Sets**

<https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>

*Unordered collection of distinct items*

```
students = {"Ajay", "Akshay", "Anusha", "Vetri", "Rahul", "Mahesh", "Pavan", "Haren"}

## Add items to the set
students.add("Priyanshu")

## Add multiple items to the set
students.update(["Hasaan", "Sumanta", "Mousumi"])

## Adding or updating existing elements
students.add("Ajay")

len(students) ## Count of items in the set

student.remove("Ajay") ## Remove an item from the set
student.discard("Akshay") ## Discards an item from the set

## Difference between remove and discard
students.remove("Chandrashekhara") ## Raises Error
students.discard("Chandrashekhara") ## Doesn't raise error

## Remove the last item
students.pop() # Since the items are unordered you can't know which will be removed

## Inbuilt methods

set.union(set1, set2...) # returns a set that contains all items from the original set, and all items from the specified sets

set.intersection(set1, set2 ... etc) # returns a set that contains the similarity between two or more sets

set.difference(set1) # returns set contains items that exist only in the first set, and not in both sets

set.symmetric_difference(set1) # returns set contains a mix of items that are not present in both sets

set.isdisjoint(set1) # returns True if none of the items are present in both sets, otherwise it returns False

set.issubset(set1) # returns True if all items in the set exists in the specified set, otherwise it retuns False

set.issuperset(set1) # returns True if all items in the specified set exists in the original set, otherwise it retuns False
```

Union
<https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Venn0111.svg/220px-Venn0111.svg.png>

Intersection
<https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Venn0001.svg/220px-Venn0001.svg.png>

Difference
<https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Venn0100.svg/220px-Venn0100.svg.png>

Symmetic Difference
<https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Venn0110.svg/220px-Venn0110.svg.png>

Subset & Superset
<https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Venn_A_subset_B.svg/150px-Venn_A_subset_B.svg.png>

**Dictionaries**

<https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>

```
student = {
    "name": "Ajay",
    "state": "Tamil Nadu",
    "gender": "Male",
    "married": False,
    "age": 23
}

## Accessing the items of a dictionary
print(student["age"]) # raises an error if the key is not present
print(student.get("age")) # doesn't raise an error if the key is not present

## Update/Set the values
student["age"] = 22
student.update({"age": 23, "city": "Chennai"})

## Removing vales from dictionary
student.pop("gender")
del student["state"]

## Empty the dictionary
student.clear()

## Length of the dictionary
len(student)

## Looping a dictionary
for x in student:
    print(x)
    print(students[x])
    
for key, value in student.items():
    print(key)
    print(value)
    
student.keys() ## returns the list of all keys
student.values() ## returns the list of all values

## Check existance
if "age" in student:
    print("Age is present")
    
if "designation" not in student:
    print("Designation is not present")
```

**NOTE: You can't concatenate strings and numbers in python to do that you can cast it**

```
name = "Ajay"
age = 23
heading = name + " " + str(age)
```

## Python

**Functions**

```
# Defining a function
def some_function():
    print("Hello Masai")
    
# Using a function
some_function()

# Defining a function with params
def print_name(name):
    print(name)

# Calling a function with params
print_name("Ajay")
print_name("Akshay")

# Passing default values
def print_name(name = "Masai"):
    print(name)
    
print_name("Ajay")
print_name()
print_name("Akshay")

### Function return
def can_drive(student):
    if student.get("age") > 18 :
        return True
    else:
        return False

def show_student():
    student = {
        "name" : "Ajay",
        "age" : 23,
        "gender" : "M"
    }
    if can_drive(student):
        print(student["name"] + " of age " + str(student["age"]) + " is eligible for driving")
```

**Scope**

```
"""
A variable inside function is only available inside
A variable outside the function and in the main body is available everywhere
"""
name = "Masai"

def show_name():
    name = "School"
    print(name)

print(name)
show_name()
print(name)
"""
Use global keyword to define a variable available everywhere
"""
def show_name():
    global name
    name = "School"
    print(name)

show_name()
print(name)
"""
Use the global keyword to change the global variable 
"""
name = "Masai"

def show_name():
    global name
    name = "School"
    print(name)
    name = "Hello"

print(name)
show_name()
print(name)
```

## Python

**Files**

<https://docs.python.org/3/library/functions.html#open>

Read File Content

```
fl = open("demo.txt")
fl.read() # Whole file content
fl.close()
```

Read File line

```
fl = open("demo.txt")
print(fl.readline()) # First Line
fl.close()
```

Read File line by line

```
fl = open("demo.txt")
for line in fl:
    print(line)
fl.close()
```

Write File

```
fl = open("demo.txt", "w")
fl.write("Masai School")
fl.close()
```

Append File

```
fl = open("demo.txt", "a")
fl.write("Masai School")
fl.close()
```

## Week 15 - Day 5

### Python Flask

```
$ export FLASK_ENV=development 
$ export FLASK_APP=server.py
$ flask run
```

Starting Code

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Masai Home Page'
```

URL & Routing

```
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def home():
    return 'Masai Home Page'
    
@app.route('/hello')
def hello():
    return 'Hello Masai'

@app.route('/user/<username>')
def show_user(username):
    return username

@app.route('/task/<username>/<int:task_id>')
def show_task(username, task_id):
    return "Task for user " + username + " id " + str(task_id)

@app.route('/login', methods=['POST'])
def login():
    return "Login Post Method"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return "Register Post Method"
    else:
        return "Register Get Method"
```

JSON Requests & Responses

```
from flask import Flask
from flask import request
import json
app = Flask(__name__)

@app.route('/hello')
def hello():
    return json.dumps({"message": "Hello Masai"})

@app.route('/login', methods=['POST'])
def login():
    username = request.json["username"]
    password = request.json["password"]
    login = False
    if username == password:
        login = True
    return json.dumps({"login": login})
```

## Python & MongoDB

**PyMongo**

<https://api.mongodb.com/python/current/>

```
$ python -m pip install pymongo
```

**Flask PyMongo**

<https://flask-pymongo.readthedocs.io/en/latest/>

```
$ pip install Flask-PyMongo
from flask import Flask
from flask import request
import json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/dummy"
mongo = PyMongo(app)

@app.route('/users')
def users():
    users = mongo.db.users.find()
    return dumps(users)

@app.route('/users/<ObjectId:user_id>')
def user(user_id):
    user = mongo.db.users.find_one({"_id": user_id})
    return dumps(user)
    
@app.route('/user/create', methods=['POST'])
def user_create():
    user = {}
    user['_id'] = ObjectId()
    user['name'] = request.json['name']
    user['email'] = request.json['email']
    mongo.db.users.insert(user)
    return dumps(user)

@app.route('/user/update/<ObjectId:user_id>', methods=["POST"])
def user_update(user_id):
    name = request.json['name']
    email = request.json['email']
    mongo.db.users.update({"_id": user_id}, {"$set": {"name": name, "email": email}})
    return dumps({"name": name, "email": email})

@app.route('/user/delete/<ObjectId:user_id>')
def user_delete(user_id):
    mongo.db.users.remove({'_id': user_id})
    return dumps({"message": "User Deleted"})
```

## Flask - Mongo

**$set** <https://docs.mongodb.com/manual/reference/operator/update/set/>

**$unset** <https://docs.mongodb.com/manual/reference/operator/update/unset/>

**$rename** <https://docs.mongodb.com/manual/reference/operator/update/rename/>

**$push** <https://docs.mongodb.com/manual/reference/operator/update/push/>

**$eq** <https://docs.mongodb.com/manual/reference/operator/query/eq/>

**$gt** <https://docs.mongodb.com/manual/reference/operator/query/gt/>

**$gte** <https://docs.mongodb.com/manual/reference/operator/query/gte/>

**$in** <https://docs.mongodb.com/manual/reference/operator/query/in/>

**$lt** <https://docs.mongodb.com/manual/reference/operator/query/lt/>

**$lte** <https://docs.mongodb.com/manual/reference/operator/query/lte/>

**$ne** <https://docs.mongodb.com/manual/reference/operator/query/ne/>

**$nin** <https://docs.mongodb.com/manual/reference/operator/query/nin/>

**$inc** <https://docs.mongodb.com/manual/reference/operator/update/inc/>

**$min** <https://docs.mongodb.com/manual/reference/operator/update/min/>

**$max** <https://docs.mongodb.com/manual/reference/operator/update/max/>

**$mul** <https://docs.mongodb.com/manual/reference/operator/update/mul/>

**$and** <https://docs.mongodb.com/manual/reference/operator/query/and/>

**$or** <https://docs.mongodb.com/manual/reference/operator/query/or/>

**$exists** <https://docs.mongodb.com/manual/reference/operator/query/exists/>

**$all** <https://docs.mongodb.com/manual/reference/operator/query/all/>

**$elemMatch** <https://docs.mongodb.com/manual/reference/operator/query/elemMatch/>

**$size** <https://docs.mongodb.com/manual/reference/operator/query/size/>

**sort** <https://docs.mongodb.com/manual/reference/method/cursor.sort/>

**limit** <https://docs.mongodb.com/manual/reference/method/cursor.limit/>

**skip** <https://docs.mongodb.com/manual/reference/method/cursor.skip/>

**count** <https://docs.mongodb.com/manual/reference/method/cursor.count/>

## Mongo DB Modelling

<https://docs.mongodb.com/manual/applications/data-models-tree-structures/>

<https://docs.mongodb.com/manual/tutorial/model-tree-structures-with-parent-references/>

<https://docs.mongodb.com/manual/tutorial/model-tree-structures-with-child-references/>

<https://material-ui.com/components/tree-view/>

### Coding Task

**Build an application with the below mentioned features (If you are only building frontend use Redux and localstorage)**

Guidelines

- Write your own css files and the layouts should be responsive (Use of Bootstrap and Material UI is not allowed)
- Write clean code with proper formatting and good variable and function naming
- Submission Deadline 19:00
- Folder `cohort_1/submissions/week_18/day_3/`

**Application**

- Route `/home` should contain two buttons `Create` and `Show`

- On clicking the

   

  ```
  Create
  ```

   

  button it should a form with the below fields and should be able to save them (DB is case you are doing for Full Stack, Redux and Localstorage for Frontend)

  - Name (Text)
  - Grade (Dropdown 1-10)
  - Maths (Marks Scored 0-100)
  - Science (Marks Scored 0-100)

- On clicking the `Show` button you should be able to see all the students with a pagination of 10 results per page and should also have the ability to filter by grade and sort by Maths or Science marks

- On clicking on Name of any student you should show the report card with the Name, Grade, Maths, Science, Total (Sum of Maths and Science) and Rank (Criteria for calculating the rank is mentioned below)

  - The ranks are calculated based on the Student Grade (So the topper in each grade will get first rank)

  - If two students in the same grade those who got same marks they will get same rank

  - The student placed next to the same marks students will get the rank skipping the intermediate ranks. Refer to the example below MARKS IN GRADE 10 Iron Man - 10, Spider Man - 10, Captain Marvel - 15, Thor - 13, Hulk - 10, Hawkeye - 8 RANKS OF STUDENTS Captain Marvel - 1, Thor - 2, Iron Man - 3, Spider Man - 3, Hulk - 3, Hawkeye - 6

  - ### Mongo DB Array Update

    <https://docs.mongodb.com/manual/reference/operator/update-array/>

    **$** <https://docs.mongodb.com/manual/reference/operator/update/positional/#up._S>_

    **$addToSet** <https://docs.mongodb.com/manual/reference/operator/update/addToSet/>

    **$pop** <https://docs.mongodb.com/manual/reference/operator/update/pop/>

    **$pull** <https://docs.mongodb.com/manual/reference/operator/update/pull/>

    **$push** <https://docs.mongodb.com/manual/reference/operator/update/push/>

    **$pullAll** <https://docs.mongodb.com/manual/reference/operator/update/pullAll/>

    **$each** <https://docs.mongodb.com/manual/reference/operator/update/each/>

    **$position** <https://docs.mongodb.com/manual/reference/operator/update/position/>

    **$slice** <https://docs.mongodb.com/manual/reference/operator/update/slice/>

    **$sort** <https://docs.mongodb.com/manual/reference/operator/update/sort/>