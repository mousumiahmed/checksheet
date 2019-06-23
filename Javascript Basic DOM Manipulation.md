**Javascript Basic DOM Manipulation**

#### What is JavaScript?

JavaScript is a scripting or programming language that allows you to implement complex things on web pages — every time a web page does more than just sit there and display static information for you to look at — displaying timely content updates, interactive maps, animated 2D/3D graphics, scrolling video jukeboxes, etc. — you can bet that JavaScript is probably involved.

**How to write Javascript**

```
<script>
function doSomething(){
 // Your Code Goes Here
}
</script>
```

**HTML Events**

HTML events allow JavaScript to register different event handlers on elements in an HTML document.

```
click
```

Execute a JavaScript when the element is clicked:

```
<button onclick="function1()">MASAI Button</button>
alert()
```

Display an alert box:

```
alert("Hello! I am an alert box!!");
```

<https://codepen.io/nrupuld/pen/gNMKWm>

**Changing Elements**

```
document.getElementById()
```

Change the content inside a particular html element

```
document.getElementById("id").innerHTML = "New Value"
```

<https://codepen.io/nrupuld/pen/qzNyYP>

Get the value of an input element

```
document.getElementById("id").value
```

<https://codepen.io/nrupuld/pen/zVBJaa>

Get the value of an select element

<https://codepen.io/nrupuld/pen/NZrOVL>

Getting Values and Setting Values and HTML

<https://codepen.io/nrupuld/pen/pXbOee>

**Styling Elements**

```
document.getElementById("id").style.color
```

<https://codepen.io/nrupuld/pen/vqKzbY>



# Javascript Basics II Notes:

## Variables:

We use programming languages like JavaScript to store and manipulate information.
**Variables** in JavaScript are used to store different kinds of data. Think of a variable like a bottle. We use bottles to store water, in much the same way we use variables to store various forms of data in JavaScript.

**Example:**

```
var number = 200
```

### Syntax:

```
var varname1 [= value1] [, varname2 [= value2] ... [, varnameN [= valueN]]];
```

You can also declare multiple variables in one statement as seen in the syntax above.

**Example:**

```
var a = 100, b = 200, c = 300;
```

The data inside variables is not constant. This means the data inside a variable can be changed.

**Example:**

```
var a = 200
a = 100
```

In the above example the variable called a first contained the value 200 but `a = 100` means that a now contains the value 100.

***NOTE: You can name variables whatever you want but try to give them good/descriptive names that tell the reader the variables function!***

## Data Types In Javascript:

There are 7 ***primitive*** types of data in JavaScript but we will focus on 3 types of data for now.

### Strings:

The first type of data is a `String`. This is used to store a sequence of characters used to represent text.

**Example:**

```
var name = "Masai School"
```

Any data within quotes `" "` is a String in JavaScript.

### Numbers:

The second type of data we want to know is a `Number`, which is used to store any kind of numbers. We have already seen this type of data in the variables example.
Numbers can store both ***Whole Numbers/Integers*** and ***Decimals***.

**Example:**

```
var num = 100
var dec = 100.001
```

### Booleans:

The last data type we are going to learn about is a `Boolean`.
This data type has only two values `true` and `false`.

**Example:**

```
var x = true
var y = false
```

### Checking the type of data:

Lets say you have some data but you don't know what type it is. You can user the `typeof()` function to find the type of the data.

**Example:**

```
var name = "Masai School"

console.log(typeof(name))
```

**Output:**

```
string
```

## Mathematical operators in JavaScript

### Common Operators

Javascript supports all the commonly used mathematical operators. Namely `+` `-` `*` `/`.

**Example:**

```
var a = 2
var b = 3
var c = a + b
var d = a * b
var e = a / b 
var f = a - b
```

**Output:**

```
c = 5
d = 6
e = 0.6666666666666666
f = -1
```

### Modulo or Remainder Operator:

Many programming languages including JavaScript have a modulo operator `%`. This operator returns the remainder when one variable is divided by another.

**Example:**

```
var a = 10 % 7
```

**Output:**

```
a = 3
```

This operator is often useful when you want to check if a number is odd or even.

**Example:**

```
var a = 10 % 2
var b = 11 % 2
```

**Output:**

```
a = 0
b = 1
```

Try this out for yourself, any even number `%2` returns 0 while any odd number `%2` returns 1.

### Exponentiation operator:

This operator is represented by `**`. This returns the value of the first operand raised to the power of the second operand. For example 24 = 16.

**Example:**

```
var a = 2 ** 4
var b = 3 ** 2
var c = 10 ** 1.5
```

**Output:**

```
a = 16
b = 9
c = 31.622776601683793
```

### Increment and Decrement Operator:

In programming we often want to increment or decrement an operator by just one value. For example we have a variable `age = 20` which increases every year. For this we use the `++` operator also called **increment operator** to increase the value of `age` by 1.

**Example:**

```
var birthday = 20
birthday++
```

**Output:**

```
birthday = 21
```

In the same we can also use the **decrement operator** `--` to decrease the value by 1.

## String concatenation

A special property of `Strings` is that they can be combined or concatenated with one another.

**Example:**

```
var word1 = "Welcome"
var word2 = "Masai"
var word3 = word1 + " to " + word2 + " school!"
console.log(word3)
```

**Output:**

```
Welcome to Masai school!
```

Strings can also be combined with other types like `numbers`.

**Example:**

```
var num1 = 1
var num2 = 2
var output = "1 + 2 = " + (num1 + num2)
console.log(output)
```

**Output:**

```
1 + 2 = 3
```

**Note**: Notice the circular brackets between `num1 + num2` this tells javascript that we want to add the two numbers mathematically. Without the brackets the output would be `1 + 2 = 12`.

## Converting between types:

Often we may have data in one type for example `string` and we may want to convert into another type for example `number` in order to do some calculations or to simply display the number.

To convert from a `string` to a `number` we can use the `Number()` function.

**Example:**

```
var num1 = "12"
var num2 = "13"
console.log(num1 + num2)
num1 = Number(num1)
num2 = Number(num2)
console.log(num1 + num2)
```

**Output:**

```
1213
25
```

Notice how the first output `1213` is simply the sting `"12"` concatenated with the string `"13"` whereas the second output is actually the value of `12 + 13 = 25`

On the other hand to convert a `number` to a `string` we can use the `.toString()` function.

**Example:**

```
var num1 = 12
var num2 = 13
console.log(num1 + num2)
num1 = num1.toString()
num2 = num2.toString()
console.log(num1 + num2)
```

**Output:**

```
25
1213
```

## Comparison Operators

### Equality

The **equality** operator `==` lets you test if two values are equal or not. It accepts 2 inputs of any type and outputs `true` if they are equal and `false` if the are not equal.

**Example:**

```
1 == 1
1 == 2
"Masai" == "Masai"
"Masai" == "masai"
```

**Output:**

```
true
false
true
false
```

## Inequality Operator

The **inequality** operator `!=` performs the opposite function of the equality operator. It accepts 2 inputs of any type and outputs `false` if they are equal and `true` if the are not equal.

**Example:**

```
1 != 1
1 != 2
"Masai" != "Masai"
"Masai" != "masai"
```

**Output:**

```
false
true
false
true
```

## Logical operators

### AND, OR and NOT Operators

Logical operators are usually used with `Boolean` values as inputs. The outputs are also `Boolean` values.

**AND Operator**

Lets say you want to check if 2 conditions in your program are true. The `&&` operator compares 2 `boolean` values and returns `true` when both `boolean` values are `true`.

**Example:**

```
true && true
false && false 
true && false 
```

***Output:***

```
true
false
false
```

**OR Operator**

Similarly to the AND operator the OR, `||` operator returns true when either boolean value is `true`.

**Example:**

```
true || true
false || false 
true || false 
```

***Output:***

```
true
false
true
```

**NOT operator**

The `!` operator returns `false` when the input is `true`. It returns `true` when the input is false.

**Note:** This is an ***unary*** operator which means it only has one input as compared to the **AND** and the **OR** operator which are ***binary*** operators and have 2 inputs as you have seen before.

**Example:**

```
!true
!false 
```

***Output:***

```
false
true
```

## Relational operators

These operators allow you to test the relation between 2 values and returns a `boolean`. JavaScript unlike other languages allows you to compare any type with any other type!

### Greater than and greater than equal to

The **greater than** operator `>` allows you to check if one value is greater than the other. It returns `true` if the first value is greater than the second and `false` if the second value is greater.

**Example:**

```
20 > 10
10 > 20
10 > 10
```

**Output:**

```
true
false
false
```

The **greater than equal to operator** `>=` also checks if the second value could be equal to the first value.

```
10 > 10
10 >= 10
```

**Output:**

```
false
true
```

### Lesser than and lesser than equal to

The **lesser than** operator `>` allows you to check if one value is lesser than the other. It returns `false` if the first value is greater than the second and `true` if the second value is greater.

**Example:**

```
20 < 10
10 < 20
10 < 10
```

**Output:**

```
false
true
false
```

The **lesser than equal to operator** `>=` also checks if the second value could be equal to the first value.

```
10 > 10
10 >= 10
```

**Output:**

```
false
true
```

## If Statements

We saw before that the **Boolean** operator has only 2 values, `true` and `false`. Now we can use these values in a meaningful way to write code.

The `if` statement executes a **block** of code only when a specified condition is `true`. If it is `false` it executes the `else` statement.

### Syntax:

```
if (condition)
   statement1
[else
   statement2]
```

**Example 1:**

```
var username = "Masai"
if(username == "Masai"){
	alert("Welcome to Masai School!")
}
else{
	alert("Invalid User")
}
```

**Example 2:**

```
var age = 15
if(age >= 18){
	alert("You can vote!")
}
else{
	alert("You cannot vote!")
}
```

Check the result of the above programs on your Web-browsers console!

## Else-If Statement:

The `else if` statement allows you to check for another condition.

### Syntax:

```
if (condition1)
  statement1
else if (condition2)
  statement2
else if (condition3)
  statement3
...
else
  statementN
```

## Switch Statement

The switch statement evaluates an value and matches the value to various **cases**. It then executes the code associated with each statement until it encounters a `break` statement.

### Syntax:

```
switch (expression) {
  case value1:
    //Statements executed when the
    //result of expression matches value1
    [break;]
  case value2:
    //Statements executed when the
    //result of expression matches value2
    [break;]
  ...
  case valueN:
    //Statements executed when the
    //result of expression matches valueN
    [break;]
  [default:
    //Statements executed when none of
    //the values match the value of the expression
    [break;]]
}
```

**Example:**

```
var day = 6
switch (day) {
  case 0:
    day = "Sunday";
    break;
  case 1:
    day = "Monday";
    break;
  case 2:
    day = "Tuesday";
    break;
  case 3:
    day = "Wednesday";
    break;
  case 4:
    day = "Thursday";
    break;
  case 5:
    day = "Friday";
    break;
  case 6:
    day = "Saturday";
    break;
  default:
    day = "Invalid Input";
}
alert(day)
```

Check the result of the above programs on your Web-browsers console!

## Few Important Javascript Functions to remember:

### Console.log

**Syntax:**

```
console.log(msg [, subst1, ..., substN]);
```

This function prints the input to the console.

### alert() function

***Syntax:***

```
alert(message)
```

This function displays an alert dialog with the input message.

## Codepen

<https://codepen.io/steviekong/pen/agmBZM>

# Javascript Basics III Notes:

## Functions:

You would have seen functions before but now you can also write your own functions!

### Example:

```
function square(number) {
  return number * number;
}
```

The `function` keyword defines the start of a function. Functions also have a name, the above function's name is `square`.
Functions are used to represent `blocks` of code that perform very specific functions. Just like `if` statements all the code within the braces `{}` are executed by the function.

Functions also have `arguments`, theses are values you can pass to a function. In the example `number` is the argument we are passing to the function.

Functions also have a `return` statement, they are optional but many functions `return` some data that can be used later in your overall program.

### While Loops

Lets say we wanted to run a piece of code multiple times. We could write out duplicate code multiple times but loops save us a lot of time and make our code efficient!

For example, let’s say we wanted to print "Hello World!" 100 times. It would be impractical to write `console.log("Hello World!")` 100 times.

This is where loops are useful.

Example:

```
var i = 0

while(i < 100){
	console.log("Hello World!")
	i++
}
```

The above code prints `Hello World!` 100 times, try it out for yourself!

*How does it work?*

The loop in the code is called a while loop. It can execute a block of code as long as a specified condition is `true`.

In the above example the while loop prints `Hello World!` until `i == 100`.

Notice the line `i++`. This is another simpler way of doing `i = i + 1`. You can also do `i--` which is a simpler way of doing `i = i - 1 `.

Once i is equal to 100 the loop **breaks** and stops executing the code within.

Here's another example:

```
var i = 0
while(true){
	console.log(i)
	i++
}
console.log("This line of code will never execute")
```

The above loop is called an infinite loop since the specified condition is always `true`. The loop will run forever which is often undesirable since we want to break out of loops to do other useful work in our program.
**Note:** Please do not try to run a infinite loop on your browser as this can cause your browser to crash. If you run and infinite loop and your browser freezes all you can do is try and close it!

### How do we fix this?

By using a `break` statement.

Example:

```
var i = 0
while(true){
	console.log(i)
	if(i == 100){
		break
	}
	i++
}
console.log("This line of code will execute after i equals 100")
```

Now our loop will gracefully break after i equals 100 and the next line of code which prints `"This line of code will execute after i equals 100"` will be executed.

### For loops

The next kind of loop in JavaScript is a for loop.

Example:

```
for(var i = 0; i < 100; i++){
	console.log("Hello World!")
}
```

This again prints `Hello World!` 100 times. For loops work in much the same way as while loops.

`i < 100` represents the limit condition, after which the loop stops executing.

### More Strings!

We can get the length of any `string` by using the `.length` property of a string.

**Example:**

```
var s = "Masai School!"
console.log(s.length)
```

**Output:**

```
13
```

We can access any element of a string by using its index.

**Example:**

```
var s = "Masai School"
var e1 = s[0]
var e2 = s[3]
var e3 = s[s.length-1]
console.log(e1)
console.log(e2)
console.log(e3)
```

**Output:**

```
M
a
l
```

In the above code `s[0]` accesses the first character of the string `s` and `s[s.length-1]` accesses the last element of the string `s`.

If you are wondering why the first element is not `s[1]` this is because of **Zero-based Indexing**. You can read more about it here <https://skillcrush.com/2013/01/17/why-programmers-start-counting-at-zero/>

Lastly you can also use loops to access every character in a string one-by-one.

**Example:**

```
var s = "Masai School is amazing!"

for(var i = 0; i < s.length; i++){
	console.log(s[i]);
}
```

**Output:**

```
M
a
s
a
i

S
c
h
o
o
l

i
s

a
m
a
z
i
n
g
!
```

### Codepen with complex examples!

<https://codepen.io/steviekong/pen/pXNwrY>