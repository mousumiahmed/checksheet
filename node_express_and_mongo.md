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