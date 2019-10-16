MONGO DB

db.users.find({"food":{$eq:["veg","juice"]}})

db.product.find({});

db.product.find({"price":{$gt:600}})

db.product.find({"price":{$gte:500}})

db.product.find({"price":{$lt:600}})

db.product.find({"price":{$lte:600}})

db.product.find({"price":{$lt:600}}).limit(1)

db.product.find({"price":{$lt:600}}).limit(1).count();

db.product.find({"food":{$in:["eggs"]}})   = eggs in fruits

 db.product.find({"food":{$nin:["eggs"]}})  ==not in

db.product.find({"name":{$ne:"Mobile"}}) ==not equal to



increment is a update query=

db.product.updateMany({},{$inc:{"stock":50}})

db.product.updateMany({},{$mul:{"stock":3}})

db.product.updateMany({},{$min:{"stock":5}})      it will convet all value to 5 which were greater than 5

db.product.updateMany({},{$max:{"stock":5}}) 

db.marks.find({})

db.product.find({$and:[{"price":{$gte:560}},{"stock":{$eq:125}}]})     - and 

db.product.find({$or:[{"price":{$gte:560}},{"stock":{$eq:125}}]})



db.product.find({$or:[{"price":560},{"stock":125}]}) =will show all  data satisfying any of the condition

db.product.find({"Mathmatics":{$exists:false}})







mongorestore -d dummy1 assignments-1/

mongo

show dbs

use dbname

show colections







PYTHON

sudo apt install ipython

sudo apt install ipython3

ipython3

name="Masai School"

In [2]: name
Out[2]: 'Masai School'

In [3]: name[0]
Out[3]: 'M'

In [4]: name[4]
Out[4]: 'i'

In [5]: name[-1]
Out[5]: 'l'

In [6]: name[-3]
Out[6]: 'o'

In [7]: name[3:6]
Out[7]: 'ai '

In [8]: name.lower()
Out[8]: 'masai school'

In [9]: name.upper()
Out[9]: 'MASAI SCHOOL'

In [10]: name.replace("a","@")
Out[10]: 'M@s@i School'

In [11]: tag="Transformation"

In [12]: heading=name+" "+tag

In [13]: heading
Out[13]: 'Masai School Transformation'

## In [14]: School in heading

NameError                                 Traceback (most recent call last)
<ipython-input-14-a96e9e641008> in <module>()
----> 1 School in heading

NameError: name 'School' is not defined

In [15]: "School" in heading
Out[15]: True

In [16]: "School" in heading:
  File "<ipython-input-16-c2b3f305e8db>", line 1
    "School" in heading:
                        ^
SyntaxError: invalid syntax

In [17]: if "School" in heading:
    ...:     print("School is in heading")
    ...:     
School is in heading

In [18]: if "any not in heading:
  File "<ipython-input-18-977e2d823f0c>", line 1
    if "any not in heading:
                           ^
SyntaxError: EOL while scanning string literal

In [19]: 

In [19]: if "any" not in heading:
    ...:     print("any is not in heading")
    ...:     
any is not in heading

In [20]: name=" masai "

In [21]: name.strip()
Out[21]: 'masai'

In [22]: range(10)
Out[22]: range(0, 10)

In [23]: range(2,10)
Out[23]: range(2, 10)

In [24]: range(2,10,2)
Out[24]: range(2, 10, 2)

In [25]: for x in range(10):
    ...:     print(x)
    ...:     
0
1
2
3
4
5
6
7
8
9

In [26]: for x in range(2,10):
    ...:     print(x)
    ...:     
2
3
4
5
6
7
8
9

In [27]: for x in range(2,10,5):
    ...:     print(x)
    ...:     
2
7

In [28]: len(range(5,50,5))
Out[28]: 9

In [29]: students=["xxx","yyhggh","gffy"]

In [30]: students
Out[30]: ['xxx', 'yyhggh', 'gffy']