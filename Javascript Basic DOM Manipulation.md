### Week 2 - Day 2

#### Session 2

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



# Javascript Basics IV Notes:

## Arrays:

Arrays are the most basic data structure that JavaScript offers users.

Arrays can store any type of data including `numbers` `strings` `booleans` etc.

### Syntax:

```
var array_name = [element1, element2 ...]
```

**Example:**

```
var numbers = [0, 2, 3, 56, 90]
```

### Empty Arrays:

Lets say you have some data you want to store in an array at a later time. You can declare an empty array before you generate your data as follows.

**Example:**

```
var emptyArray = []
```

### Can you store multiple types of data in the same array ?

The simple answer is ***YES!***. JavaScript allows you to store all types of data within the same array.

**Example:**

```
var multiple = [12, "Masai", true]
```

The above array `multiple` has 3 different types of data in it. Namely `number` `string` and `boolean`.

### Array Length

Getting the array length is simple. Just use the `arrayname.length` property.

**Example:**

```
var numbers = [0, 1, 2, 3, 4]
console.log(numbers.length)
```

**Output:**

```
5
```

### Accessing array elements:

Just like strings we can use the `array[index]` syntax to access any element of an array.

***Example:**

```
var fruits = ["apple", "pear", "mango", "banana"]
console.log(fruits[0])
console.log(fruits[fruits.length-1])
```

**Output:**

```
apple
banana
```

### Looping Through Arrays

Again just like strings we can loop through arrays and access each element by its `index`.

**Example:**

```
var cities = ["bangalore", "mumbai", "chennai", "new york", "hong kong"]

for(var i = 0; i < cities.length;i++){
	console.log(cities[i])
}
```

**Output:**

```
bangalore
mumbai
chennai
new york
hong kong
```

### Adding to the End of an array:

You can add an element to the end of an array by using the `arrayname.push(element)` function.

**Example:**

```
var cities = ["bangalore", "mumbai", "chennai", "new york", "hong kong"]
cities.push("delhi")
```

***Output:**

```
["bangalore", "mumbai", "chennai", "new york", "hong kong", "delhi"]
```

### Removing from the end of an array

You can remove an element from the end of an array by using the `arrayname.pop()` function.

**Example:**

```
var cities = ["bangalore", "mumbai", "chennai", "new york", "hong kong"]
cities.pop()
```

***Output:**

```
["bangalore", "mumbai", "chennai", "new york"]
```

The `pop()` function also returns the removed value.

There are many more useful array functions available in JavaScript, you can read about them in this link <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array>

## Scope

In programing **Scope** determines the accessibility (visibility) of variables.

There are two types of scope in JavaScript:

- Local Scope
- Global Scope

### Local Variables

Consider the following snippet of code

```
// code here cannot access the `number` variable!
function someFunction(){
    var number = 20
}
// code here cannot access the `number` variable!
```

In the above example only the code within the funciton `someFunction` can access the `number` variable.

## Global Variables

Consider another snippet of code

```
var number = 20
//code here can access the `number` variable!
function someFunction(){
    //code here can access the `number` variable!
}
//code here can access the `number` variable!
```

The variable `number` is said to be a global variable and can be accessed by any line of code below its declaration.

## Local Scope within functions

Consider one last example

```
for(var i = 0; i < 10; i++){
    console.log(i)
}
// the variable `i` cannot be accessed here
```

In the above example since `i` is declared within the for loop it cannot be accessed outside it!

### Week 3 - Day 3

#### Session 2

**Basic DOM manipulation**

```
<div id="id1">
    <div id="id2">
        <div id="id3">
            <p id="id4">
                Some Text
            </p>
        </div>
        <div id="id5">
            Some Text
        </div>
    </div>
    <div id="id6">
        Some Text
    </div>
</div>
```

- **Child node**: A node *directly* inside another node `id2` and `id6` are child nodes of `id1` also `id3` is child node of `id2` and `id4` is child node of `id3`
- **Descendant node**: A node *anywhere* inside another node. `id2` and `id6` are child nodes of `id1` and also descendants. `id3` `id4` `id5` are not child nodes of `id1` but descendants
- **Sibling nodes**: Nodes that sit on the same level. In the above example `id2` and `id6` are siblings and `id3` and `id5` are also siblings

**querySelector**

The `querySelector()` method returns the first element that matches one or more CSS selectors. If no match is found, it returns `null`.

```
var ele = document.querySelector(selector);
```

<https://codepen.io/nrupuld/pen/BgdvQQ>

**querySelectorAll**

The `querySelectorAll()` returns all elements that match the specified CSS selector.

```
var eles = document.querySelectorAll(selector);
```

Using Element Selector
<https://codepen.io/nrupuld/pen/QXMzOa>

Using Class Selectors
<https://codepen.io/nrupuld/pen/xoLmNx>

**createElement**

The `createElement()` method creates a new HTML element

```
document.createElement(tagName);
```

<https://codepen.io/nrupuld/pen/MMvLed>

**appendChild**

The `appendChild()` method adds an element as the last child to the HTML element

```
ele.appendChild(childEle);
```

<https://codepen.io/nrupuld/pen/zVdezv>

**removeChild**

The `removeChild()` method **removes a specified child element** from the HTML element

```
ele.removeChild(childEle);
```

<https://codepen.io/nrupuld/pen/ewExqz>

**insertBefore**

The `insertBefore()` method **adds a specified child element before another child element**.

```
ele.insertBefore(newEle, refEle);
```

<https://codepen.io/nrupuld/pen/dBzLVy>



### Week 3 - Day 4

#### Session 2

JS CSS & Style Manipulation

```
snake_case
camelCase
```

Commonly used case in css

```
caterpillar-case` `dash-case` `hypen-case` `kebab-case
```

**setAttribute**

The `setAttribute()` method adds the specified attribute to an element, and gives it the specified value.

If the specified attribute already exists, only the value is set/changed.

```
element.setAttribute(attributename, attributevalue)
```

Adding Classes & IDs

<https://codepen.io/nrupuld/pen/VJMNBw>

Other Attributes

<https://codepen.io/nrupuld/pen/qzPwzW?editors=1010>

Using loops & conditional operators

<https://codepen.io/nrupuld/pen/KjXLpe>

**removeAttribute**

The `removeAttribute()` method removes a given attribute of a specific HTML element.

```
ele.removeAttribute(name);
```

<https://codepen.io/nrupuld/pen/gNXYOg>

**style**

The `HTMLElement.style` property is used to get as well as set the *inline* style of an element.

The `style` property has the same (and highest) priority in the CSS cascade as an inline style declaration set via the `style` attribute.

```
ele.style.property = value
```

<https://codepen.io/nrupuld/pen/BgmBGV>

Using loops

<https://codepen.io/nrupuld/pen/OeOJyB>

**CSS Properties DOM Notation accessed from JS**

<https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference>

# Week 3 - Day 3

# Javascript Basics V Notes:

## Introduction to events in JavaScript

Events are actions that happen on a web page when users perform actions. Events also occur when browsers also perform actions.

**Example [1]**:

- The user clicking the mouse over a certain element or hovering the cursor over a certain element.
- The user pressing a key on the keyboard.
- The user resizing or closing the browser window.
- A web page finishing loading.
- A form being submitted.
- A video being played, or paused, or finishing play.
- An error occurring.

When these actions are performed by users `events` are fired in the browser window. Events are also usually attached to a specific element or multiple elements within a web page.

There are 1000's of events in Javascript so we will only go over a few important ones.

If you want to take a look all the events available in JavaScript visit this link <https://developer.mozilla.org/en-US/docs/Web/Events>

## Simple events

### Button Clicks

You have already attached `functions` to button clicks within HTML tags but now we can use ***Event Handlers*** to do the same in a much more useful way.

**Example:** HTML CODE SNIPPET:

```
<button id = "changeColor">Click here to change my color</button>
```

**JavaScript Code Snippet:**

```
var changeButton = document.getElementById('changeColor');

function random(number){
  return Math.floor(Math.random()*number);
}

function switchColor()
{
    var randomColor = 'rgb(' + random(255) + ',' + random(255) + ',' + random(255) + ')';
    changeButton.style.backgroundColor = randomColor;
}
changeButton.addEventListener('click', switchColor);
```

In the above code we have attached a the `click` listener to the button element with the id `changeColor` using the `addEventListener()` function.

When the button is clicked the listener function `switchColor` is called.

The listener function then calls the random number to get a random color and sets the `style.backgroundColor` property of the button to the random color.

### Button Double Click

As I mentioned before there are thousands of listeners in JavaScript. Another common listener for buttons is `dblclick`.

This listener listens for a user double clicking the button.

**Example:**

***HTML CODE SNIPPET:***

```
<button id = "changeColorDouble">Click here to change my color</button>
```

**JavaScript Code Snippet:**

```
ar doubleButton = document.getElementById('changeColorDouble');
function switchColorDouble(){
  var randomColor = 'rgb(' + random(255) + ',' + random(255) + ',' + random(255) + ')'; // random is a function that I have defined above
  
  doubleButton.style.backgroundColor = randomColor
}
doubleButton.addEventListener('dblclick', switchColorDouble)
```

## Removing Listeners

The best part of using the `addEventListener` function is that you can also remove listeners using the `removeEventListener` function.

Consider the below example where where we want the button to change colors only 1 time.

**Example:** **HTML CODE SNIPPET:**

```
<button id = "changeColorOnce">Double Click here to change my color</button>
```

**JavaScript Code Snippet:**

```
var buttonOnce = document.getElementById('changeColorOnce');

function switchColorOnce(){
  var randomColor = 'rgb(' + random(255) + ',' + random(255) + ',' + random(255) + ')'; // 
  buttonOnce.style.backgroundColor = randomColor
  buttonOnce.removeEventListener('click', switchColorOnce)
}

buttonOnce.addEventListener('click', switchColorOnce)
```

This is the same code as the first example. However, once the function `switchColorOnce()` is called we also call the `buttonOnce.removeEventListener('click', switchColorOnce)` function which removes the event listener from the button.

This means that the button only changes color once when it is clicked. After it is clicked once, if you try and click it again the button does not change color anymore.

## Validating Forms and preventDefault:

You might have validated forms before but now you can do it easier with listeners.

Look at the code below:

**Example:** **HTML CODE SNIPPET:**

```
<form id  = "nameForm">
  <div>
    <label for="fname">First name: </label>
    <input id="fname" type="text">
  </div>
  <div>
    <label for="lname">Last name: </label>
    <input id="lname" type="text">
  </div>
  <div>
     <input id="submit" type="submit">
  </div>
</form>
<p id = "output"></p>
```

**JavaScript:**

```
var form = document.getElementById('nameForm');
var fname = document.getElementById('fname');
var lname = document.getElementById('lname');
var submit = document.getElementById('submit');
var para = document.getElementById('output');

function validate(e){
  if(fname.value == '' || lname.value == ''){
    e.preventDefault()
    para.textContent = "First name or last name is empty!"
  }
}

form.addEventListener('submit', validate);
```

Notice how we attach the listener to the `form` element and not the submit button!

This is how you should be doing it normally!

When forms are submitted in HTML the ***default*** or normal action is that the form gets submitted to the back-end.

We use the `e.preventDefault()` function to override the ***default*** functionality.

Instead we print some the error message `"First name or last name is empty!"` to a paragraph tag.

The `e` argument is called the **Event Object** we will learn more about this later when we discuss **Objects**.

For now just use it to call the `e.preventDefault()` function.

## Codepen.io Link:

All examples discussed today are on the codepen! <https://codepen.io/steviekong/pen/LKLqwm?editors=1111>

## Mozilla Link

If you want more information on events and listeners visit this link <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events>

### Source Cited:

[1] Introduction to events, Mozilla, <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events>





# Week 3 - Day 4

# Javascript Basics VI Notes:

## Introduction to Objects and revisiting types

### More Types!

We have already discussed a few types of **primitive** data in JavaScript like `string` `number` `boolean`.

Lets discuss a few more:

`null` : **null** is a special **primitive** data type that signifies that a there is 'no value' or that there is a lack of value.

It is important to note that JavaScript will never assign a `null` value to anything, only you the programmer can do that. This is because `null` is used to represent the **intentional** absence of any object value.

`null` is often useful when you want to return nothing from a function. This is especially useful for handling errors!

**Example:**

```
var x = null

console.log(x)

if(x == null){
    console.log('x is null!')
}
else{
    console.log('x is not null!')
}
```

`undefined`: **undefined** is a another special primitive type that signifies that a variable has not been assigned any value. This is a **default** value that JavaScript assigns.

This is often useful if you want to check if a variable contains a value yet.

**Example:**

```
var num;

console.log(num)
```

`null` and `undefined` are not the same in Javascript. If you want to read more about their difference visit this link <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null>

### Now onto Objects

We have studied around 5 **primitive** types in JavaScript. There are two more but we can get to them later.

Other than these primitive types the only other type is called an **object**.

Other than the 7 **primitive types** almost everything else in JavaScript is an `object`.

Some examples of objects you might have seen before:

- `Math` Object.
- `String` wrapper object.
- `Number` wrapper object.
- Every `function` in JavaScript is also a `Function` object!
- `Array` is also an object.

Nearly everything in JavaScript is an `object` or acts like an object in the case of wrapper objects like `String` or `Number`.

`objects` are a collection of properties. These properties can be modified by functions/methods that these `objects`provide you with.

For example you have already seen the `string.length` property and the `array.length` property which gives you the length of arrays and objects.

### Accessing object properties

You can access any `object`'s property using the following syntax.

**Syntax**:

```
objectName.propertyName
```

For example we access the `length` property of a string by using `string.length`.

### Making your own objects

Lets say you have a person.

A person may several properties like:

- Name
- Age
- Height
- Gender
- Hobbies

We can define an object called `person` with several properties like so.

**Code**:

```
var person = {
    name : "Sidharth",
    age : 100,
    height: "6 Ft 12 In",
    gender : "Female",
    hobbies: ["Coding", "Weight Lifting", "Running", "Eating"]
}
```

Now you have a person with several properties. Notice how the properties are different JavaScript types.

You can then access those properties:

```
var person = {
    name : "Sidharth",
    age : 100,
    height: "6 Ft 12 In",
    gender : "Female",
    hobbies: ["Coding", "Weight Lifting", "Running", "Eating"]
}

console.log(person.name)

console.log(person.age)

console.log(person.Hobbies[1])
```

**Output:**

```
Sidharth
100
Weight Lifting
```

Notice the syntax of the `object`. Each object is made up of multiple members.

Each member has a **key** or **name** and a value. We calls these key-value pairs in programming.

### Adding new names/keys and modifying existing names/keys

You can add new names/keys to an object with the following syntax. You can also modify values with the same syntax.

```
objectname.name = value
```

**Example:**

```
var person = {
    name : "Sidharth",
    age : 100,
    height: "6 Ft 12 In",
    gender : "Female",
    hobbies: ["Coding", "Weight Lifting", "Running", "Eating"]
}

person.favColor = "Red"
person.name = "Piker"
```

## String wrapper object functions/methods

The `string` wrapper object gives you some basic functions to modify and manipulate strings. Lets use some of these functions.

### substring() method

The `substring(startIndex, endIndex)`` method returns a part of a string from an input string.

The start index is the index of the first character in the output string.

The end index is the index of the last character in the output string.

**Example:**

```
var input = "Welcome to Masai School"

var output1 = input.substring(0, 6)
var output2 = input.substring(4, 10)

console.log(output1)
console.log(output2)
```

**Output:**

```
Welcom
ome to
```

### indexOf() method

The `indexOf(searchString)` method returns the index of the first instance of the string you are searching for within the the given string.

**Example:**

```
var input = "Welcome to Masai School"

var output = input.indexOf("Masai")

console.log(output)
```

**Output:**

```
11
```

### toUpperCase() and toLowerCase()

The `toUpperCase()` converts a string from **lower case** to **upper case**.

**Example:**

```
var input = "Welcome to Masai School"

var output = input.toUpperCase();

console.log(output)
```

**Output:**

```
WELCOME TO MASAI SCHOOL
```

The `toLowerCase()` does the opposite and converts a string from **lower case** to **upper case**.

**Example:**

```
var input = "WELCOME TO MASAI SCHOOL"

var output = input.toLowerCase();

console.log(output)
```

**Output:**

```
welcome to masai school
```

There are many more `string` wrapper object functions which you can check out here <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#String_generic_methods>

## Other useful function you may use in the future.

Just like `strings` there are many useful function you may want to use.

The `Math` object gives you many useful mathematical functions. You can check all these functions out here <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math>

The `array` object also gives you useful functions to manipulate arrays. You can check these out here <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array>

There are thousands of objects in javascript so it would be difficult to go over all of them here.

But all objects have specific properties and functions to manipulate those properties.

## Codepen link:

<https://codepen.io/steviekong/pen/orGpWR?editors=1011>



## Week 4 - Day 1

### Basics of the Unix Philosophy

The ‘Unix philosophy’ originated with Ken Thompson's early meditations on how to design a small but capable operating system with a clean service interface. It grew as the Unix culture learned things about how to get maximum leverage out of Thompson's design. It absorbed lessons from many sources along the way.

- Make each program do one thing well. To do a new job, build afresh rather than complicate old programs by adding new features.
- Expect the output of every program to become the input to another, as yet unknown, program. Don't clutter output with extraneous information. Avoid stringently columnar or binary input formats. Don't insist on interactive input.
- Design and build software, even operating systems, to be tried early, ideally within weeks. Don't hesitate to throw away the clumsy parts and rebuild them.
- Use tools in preference to unskilled help to lighten a programming task, even if you have to detour to build the tools and expect to throw some of them out after you've finished using them.

**Print Odd & Even Number from 1-20**

- Basic Increments <https://codepen.io/nrupuld/pen/PrQxYm?editors=1011>
- Basic Increments (Params) <https://codepen.io/nrupuld/pen/wLyQaP?editors=1011>
- Looping Modulus <https://codepen.io/nrupuld/pen/gNvQPR?editors=1011>
- Looping Modulus Single Function <https://codepen.io/nrupuld/pen/vqdQXg?editors=1011>
- Looping Modulus Generalised Function <https://codepen.io/nrupuld/pen/rEJQjE?editors=1011>
- Looping Modulus Generalised Abstraction <https://codepen.io/nrupuld/pen/vqdQem?editors=1011>



# Week 4 - Day 1

# Javascript Basics VII Notes:

## The for in loop

Last time, we discussed how objects basically consist of key-value pairs.

It can often get tedious to access each and every `key` within and object one by one and retrieve all the data.

Once again loops come to our rescue! We can use the **for in ** loop to do this.

**Syntax:**

```
for(key in object){

}
```

**Example:**

```
var person = {
    name : "Sidharth",
    age : 100,
    height: "6 Ft 12 In",
    gender : "Female",
    hobbies: ["Coding", "Weight Lifting", "Running", "Eating"]
}

for(key in person){
    var output = key + ":" + person[key]
    console.log(output)
}
```

**Output:**

```
name:Sidharth
age:100
height:6 Ft 12 In
gender:Female
hobbies:Coding,Weight Lifting,Running,Eating
```

Notice how we accessed each value of the object by using the `object[key]` syntax.

This is an alternative to the `object.key` syntax. You must use the `object[key]` syntax in `for in` loops otherwise your values will be `undefined`.

## Functions within objects and `this` keyword

Since `function`s are also objects in JavaScript, we can add them to objects to provide useful functionality.

Remember in the last coding session we printed the values of the `person` object when a button was clicked ?

We can do the same but with a function defined within an object.

**Example:**

```
var person = {
    name : "Sidharth",
    age : 100,
    height: "6 Ft 12 In",
    gender : "Female",
    hobbies: ["Coding", "Weight Lifting", "Running", "Eating"],
    printDetails: function(){
        for(key in this){
        var output = key + ":" + person[key]
        console.log(output)
        }
    }
};

person.printDetails()
```

**Output:**

```
name:Sidharth
age:100
height:6 Ft 12 In
gender:Female
hobbies:Coding,Weight Lifting,Running,Eating
printDetails:function(){
        for(key in this){
        var output = key + ":" + person[key]
        console.log(output)
        }
    }
```

Notice how we use the `this` keyword in the function and not the name of the object. The `this` keyword is used to refer to the object itself in javaScript.

When you want to access an objects properties within that object itself you must use the `this` keyword. If you use the objects name, it will not work!

Look at the example below:

**Example:**

```
var person = {
    name : "Sidharth",
    age : 100,
    height: "6 Ft 12 In",
    gender : "Female",
    hobbies: ["Coding", "Weight Lifting", "Running", "Eating"],
    printDetails: function(){
        for(key in person){
        var output = key + ":" + person[key]
        console.log(output)
        }
    }
};

person.printDetails()
```

**Output:**

```
name:Sidharth
age:100
height:6 Ft 12 In
gender:Female
hobbies:Coding,Weight Lifting,Running,Eating
printDetails:function(){
        for(key in this){
        var output = key + ":" + person[key]
        console.log(output)
        }
    }
```

### Using `this` keyword to modify function properties

We can also use functions to update properties like so.

**Example:**

```
var person = {
    name : "Sidharth",
    age : 100,
    height: "6 Ft 12 In",
    gender : "Female",
    hobbies: ["Coding", "Weight Lifting", "Running", "Eating"],
    printDetails: function(){
        for(key in person){
        var output = key + ":" + person[key]
        console.log(output)
        }
    },
    addHobby: function(hobby){
        this.hobbies.push(hobby)
    }
};
console.log(person.hobbies)
person.addHobby("Swimming")
console.log(person.hobbies)
```

**Output:**

```
[ 'Coding', 'Weight Lifting', 'Running', 'Eating' ]
[ 'Coding', 'Weight Lifting', 'Running', 'Eating', 'Swimming' ]
```

The `addHobby` function accepts a `hobby` as an argument and updates the `this.hobbies` array with a new hobby.

## Constructors in JavaScript

We made one person object with several properties but if we wanted to make another person we need to write the same bit of code over and over.

JavaScript actually makes it very easy to create an object `constructor`.

Think of a `constructor` as a skeleton of our person. It has no properties, but we can use it to create any number of new `person` objects!

**Important note!:** According to mozilla "A constructor function name usually starts with a capital letter — this convention is used to make constructor functions easier to recognize in code."

So always name you constructor functions starting with a capital letter!

**Example:**

```
function Person(name, age, height, gender, hobbies){
    this.name = name;
    this.age  = age 
    this.height = height 
    this.gender = gender
    this.hobbies = [hobbies]
}

var sid = new Person("Sidharth", 90, "7 ft 9 in", "Male", ["swimming", "boxing"]);
var sam = new Person("Sam", 67, "2 ft 3 in", "Male", ["dancing", "running"]);

console.log(sid)
console.log(sam)
```

***Output:**

```
Person {
  name: 'Sidharth',
  age: 90,
  height: '7 ft 9 in',
  gender: 'Male',
  hobbies: [ [ 'swimming', 'boxing' ] ] }

Person {
  name: 'Sam',
  age: 67,
  height: '2 ft 3 in',
  gender: 'Male',
  hobbies: [ [ 'dancing', 'running' ] ] }
```

As you can see `sid` and `sam` are both `Person` objects but they have different attributes!

You can make new objects from `constructors` using the `new` keyword.

## CodePen:

<https://codepen.io/steviekong/pen/ZdaBxN>



# Week 4 - Day 3

# Javascript Basics VIII Notes:

## JSON (JavaScript Object Notation)

**So what is JSON?**

According to Mozilla - "JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax." [1]

**Why should we use JSON?**

JSON is one of the most commonly used data formats to transmit data in web applications. Moreover, its not just JavaScript that supports JSON, many commonly used languages on the Web including PHP, Python, C/C++, Java etc., also support JSON.

Thus, JSON can be used to send data from the front-end to the back-end, and vice-versa. Many popular databases like MongoDB, CouchDB, MySQL, Oracle and PostgreSQL also have extensive support for JSON.

Think of JSON as an almost universal data format on the Internet.

### What Does JSON look like ?

A JSON string's format is very similar to a regular JavaScript Object literal which we have studied before.

It also consists of `key` - `value` pairs.

It supports the 6 common data types in JavaScript, `String` `Number` `Array` `Boolean` `Null` `Object`.

Lets look at an example of a JSON object below:

```
var emp = 

{
    "Employees" : [
        {
        "userId":"sqwert",
        "jobTitleName":"Developer",
        "firstName":"Sam",
        "lastName":"Pat",
        "preferredFullName":"Samuel Patrick",
        "employeeCode":"E1",
        "region":"CA",
        "phoneNumber":"123-4567890",
        "emailAddress":"abc@gmail.com"
        },
        {
        "userId":"amir1337",
        "jobTitleName":"Front-end Developer",
        "firstName":"Amir",
        "lastName":"Khan",
        "preferredFullName":"Amir Khan",
        "employeeCode":"E2",
        "region":"MA",
        "phoneNumber":"098-7654321",
        "emailAddress":"xyz@gmail.com"
        }
    ],
    "count": 2
}

console.log(emp["Employees"][0]["region"])
console.log(emp["Employees"][1]["phoneNumber"])
```

**Output:**

```
CA
098-7654321
```

In the above example, the JSON contains a key called `Employees` which is an array. It contains 2 objects with several fields.

Any data from the above object can be accessed in the same way as a regular JavaScript object literal as you can see from the example.

However, notice that in the JSON format all the `keys` are surrounded by double quotes!

### Important notes about JSON:

1. JSON is just a data format and does not contain any properties or functions/methods.
2. JSON requires double quotes to be used around strings and property names. **Single quotes are not valid.**
3. Even a single misplaced comma or colon can cause a JSON file to go wrong, and not work.
4. Unlike JavaScript code in which object properties may be unquoted, in JSON, only quoted strings may be used as properties.

### Converting between JSON and JavaScript object literals

You may often want to convert between JSON and JavaScript object literals, especially for sending and receiving data across the Internet.

To convert from a JavaScript Object to a JSON string we can use the `JSON.stringify` method.

To convert from a JSON string to a JavaScript Object we can use the `JSON.parse` method.

**Example:**

```
var person = {
    name : "Sidharth",
    age : 100,
    height: "6 Ft 12 In",
    gender : "Female",
    hobbies: ["Coding", "Weight Lifting", "Running", "Eating"]
}

var json = JSON.stringify(person)

console.log(json)

var regularObject = JSON.parse(json)

console.log(regularObject)
```

**Output:**

```
{"name":"Sidharth","age":100,"height":"6 Ft 12 In","gender":"Female","hobbies":["Coding","Weight Lifting","Running","Eating"]}

{
    name : "Sidharth",
    age : 100,
    height: "6 Ft 12 In",
    gender : "Female",
    hobbies: ["Coding", "Weight Lifting", "Running", "Eating"]}
```

JSON will become more relevant when we learn about API's and retrieving data from them.

**Codepen Link:** <https://codepen.io/steviekong/pen/mZXYKe>

## Functions as objects / Function expressions

Remember that in a previous class, we discussed how `function`s in JavaScript are objects too.

Thus, we can use them in much the same way as we use any other object in JavaScript.

This, means we can assign them to variables. This is known as a **function expression**.

**Example:**

```
var sum = function(x, y){
    return x + y
}

var division = function(x, y){
    return x / y
}

console.log(sum(1, 2))
console.log(division(10,5))
```

This can often be useful when we want to use functions as variables, add them to arrays or objects. **Or even pass them as arguments to other functions!**

We will go over functions as arguments in the next part.

## Callback functions

A callback function is a function that is passed as an argument to another function, to be “called back” at a later time. [2]

Lets take a look at an example to see what this means in more detail.

**Example:**

```
function sum(x, y, callBack){
    var sum = x + y
    callBack(sum)
}

var print = function(toPrint){
    console.log(toPrint)
}

sum(4, 5, print)
```

**Output:**

```
9
```

As you can see we passed the print function as an argument to the sum function. First the sum function calculated the sum of `x` and `y` and then the print function was called after the sum was calculated to print the sum to the `console`.

**Codepen Link** <https://codepen.io/steviekong/pen/agqgde>

### Common functions that take callbacks as arguments

Many functions in JavaScript will often take functions as arguments and it is important to understand how they work!

**Array.foreach()**

The forEach() method runs a given callback function on every element of an array.

**Example:**

```
var arr = [1, 2, 3, 4, 5];

arr.forEach(function(element){
    console.log(element)
});
```

**Output:**

```
1
2
3
4
5
```

As you can see the `forEach` function performs a very similar role as a regular `for` loop. That is, it performs some piece of code for every element in the array.

However, the `forEach` method can only be used with an array as it is a method of the `Array` object!

**Array.map()**

The `map()` method creates a new array with the results of applying a callback function on every element of the original array.

**Example:**

```
var arr = [1, 2, 3, 4, 5]

var timesTwo = arr.map(function (element){
    return element *2
});

console.log(timesTwo)
```

**Output:**

```
[ 2, 4, 6, 8, 10 ]
```

The above function simply accepted an element, multiplied by 2 and returned the value. The map applies the callback function to each element and returns a new modified array.

There are many more interesting Array functions which accept functions as arguments.

**Codepen link:** <https://codepen.io/steviekong/pen/MMVKew?editors=1111>

You can check them out here <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach>

### Citations

[1] Mozilla, 2019, Working with JSON, <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON>

[2] FreeCodeCamp, 2019, CallBack functions, <https://guide.freecodecamp.org/javascript/callback-functions/>





# Week 4 - Day 4

# JavaScript Basics IX Notes:

## Fetching Data From a Server

All this time we have been making web applications but they don't actually connect to the web!

Whats the point in making an application if it can't send and retrieve data from the Internet?

In short, nothing! Web-applications (in my opinion) are only useful if they can send, retrieve, process and delete data using the Internet.

In this next part we are going to learn about the basics of the web and how to retrieve data from a server/API.

## Some groundwork about the Web

The web itself is a very complex network of billions of computers (possibly trillions), but thanks to advancements in software and web technology, it is an easy process for front-end developers to send and retrieve data from servers.

### Client Server Model

**Real Life Explanation:**

Imagine you are at a restaurant and you want to get some food.

You look at the menu and **request** the waiter to **GET** you some dosa.

The waiter looks at your **request** and **responds** by giving you your dosa.

**Technical Explanation:**

The client server model works in much the same way.

You the client sends the server a HTTP **request** with the **GET** method and the server responds with a **HTTP** **response**with the data you requested.

**GET** is one of many HTTP request methods you would use to **request** data from a web server.

This might be a lot to take in but I think it will get simpler once you are able to use it in JavaScript.

## The XMLHttpRequest

The `XMLHttpRequest` object used to send and receive HTTP requests.

Lets take a look at a simple example where we send a simple `GET` request and retrieve some JSON data.

The freeCodeCamp weather API accepts Latitude and Longitude and returns weather information in `JSON` format.

You can see it's documentation here <https://fcc-weather-api.glitch.me/>

Lets try and retrieve the weather information for Bangalore.

```
// This creates a new XMLHttpsRequest() object
var xhr = new XMLHttpRequest(); 

// This configures the object to perform a GET request to the given url
// Notice how we pass lat=12.9716&lon=77.5946, this is the latitude and longitude for Bangalore.
xhr.open('GET', 'https://fcc-weather-api.glitch.me/api/current?lat=12.9716&lon=77.5946');
// This will send the GET request to the server.
xhr.send()
// This function will be called after the information is retrieved
xhr.onload = function (){
    // The HTTP 200 status code is returned when your request is successful so we check for that
    if(xhr.status == 200){  
        console.log(xhr.response) // Print the response from the server after a successful request
    }
    else{
        // If the request is unsuccessful we print some error text along with the error code
        console.log("Error Code is:" + xhr.status)
    }
}
```

**Output:**

```
"{'coord':{'lon':77.59,'lat':12.97},'weather':[{'id':802,'main':'Clouds','description':'scattered clouds','icon':'https://cdn.glitch.com/6e8889e5-7a72-48f0-a061-863548450de5%2F03d.png?1499366020890'}],'base':'stations','main':{'temp':29.6,'pressure':1009,'humidity':45,'temp_min':27.78,'temp_max':31},'visibility':10000,'wind':{'speed':7.2,'deg':270},'clouds':{'all':40},'dt':1562059584,'sys':{'type':1,'id':9205,'message':0.0078,'country':'IN','sunrise':1562027230,'sunset':1562073580},'timezone':19800,'id':1277333,'name':'Bangalore','cod':200}"
```

**CodePen Link:** <https://codepen.io/steviekong/pen/PreYVZ>

As you can see we got a response from the server with some `JSON`.

The `JSON` contains a lot of weather Data about Bangalore. You can parse it into a JavaScript Object and retrieve any data you want.

### Small note about the `onload` event

Something important to note is that `onload` is a JavaScript event just like `onclick` `onhover` etc. It is **not** a function!

This means that just like other events in JavaScript it is triggered by some action occurring on the browser.

In `xhr.onload` the event it is triggered by is a successful HTTP request. Once the event is triggered it executes the callback function.

### HTTP Codes

When you send requests to servers you may get many different responses or HTTP status codes.

These codes mean many things and can be useful in debugging your program.

**Some common HTTP status codes codes and their meanings:**

1. 200 : OK - This is the standard HTTP response when the request was successful.
2. 400 : Bad Request- You will get this error when you make a "Bad" or "Incorrect" request.
3. 404: Not Found - You will get this error when the resource you are looking for on the server is not found.

There are many more error codes in HTTP which you can look at here <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>

## Now lets display the data!

In the code below after a button is clicked the data will be displayed.

We use callback functions to achieve this.

**But why? Can I do this without callback functions?**

You could but, remember that web servers may take an unknown amount of time to retrieve data.

While this data is being retrieved we still need our program to do other useful tasks like fetching data from another server or any other useful task really.

We don't want our entire webpage to halt or hang just because we are getting some data from a server.

**Program Flow:**

1. Button is clicked.
2. A HTTP GET request is sent to the server within the `getWeatherData` function.
3. The server looks at the request and sends an appropriate response.
4. The function verifies the response and sends it to the display function.
5. The display function checks the input string and prints it to a p tag.

**Example:**

```
// This function will get JSON data from the server and call the printWeatherData function!
//The argument displayFunction is a function!
function getWeatherData(displayFunction){
  var result = null;
  var xhr = new XMLHttpRequest(); 
  xhr.open('GET', 'https://fcc-weather-api.glitch.me/api/current?lat=12.9716&lon=77.5946');
  xhr.send()
  xhr.onload = function (){
    if(xhr.status == 200){
      result = xhr.response;
      printWeatherData(result);
    }
    else{
      console.log("Error Code is:" + xhr.status);
    }
  } 
}

// This function will check the input to see if it is null and print the input to a p tag if it is not null.
var printWeatherData = function (input){
  var body = document.querySelector('body');
  var display = document.createElement('p');
  if(input == null){ // checking if the input is null
    display.textContent = "Error! No weather data received or invalid request!";
    //It will print an error if the input is null
  }
  else{
    display.textContent = input;
    //Otherwise it will display the text
  }
  body.append(display);
}

//Button and listener for the `click here to print the weather data!` button
var displayBtn = document.querySelector('#printWeather')
displayBtn.addEventListener('click',function(){
  getWeatherData(printWeatherData);
});
```

**CodePen Link:**

<https://codepen.io/steviekong/pen/dBeyxN>

## What if we want the weather data for other cities ?

We can also change the `url` string we pass to the `xhr.open` function to get the data of different cities.

**How can we do this?**

Simply by passing 2 strings to the `getWeatherData` function.

**Example:**

```
// This function will get JSON data from the server and call the printWeatherData function!
//The argument displayFunction is a function!
//The argument latitude is a string from the input with id = "latitude"
//The argument longitude is a string from the input with id ="longitude"
function getWeatherData(displayFunction, latitude, longitude){
  var result = null;
  var xhr = new XMLHttpRequest(); 
  xhr.open('GET', 'https://fcc-weather-api.glitch.me/api/current?lat='
           +latitude
           +'&lon='+longitude); //Here I have simply appended latitude and longitude to the string
  xhr.send()
  xhr.onload = function (){
    if(xhr.status == 200){
      result = xhr.response;
      printWeatherData(result);
    }
    else{
      console.log("Error Code is:" + xhr.status);
    }
  } 
}

// This function will check the input to see if it is null and print the input to a p tag if it is not null.
var printWeatherData = function (input){
  var body = document.querySelector('body');
  var display = document.createElement('p');
  if(input == null){ // checking if the input is null
    display.textContent = 'Error! No weather data received or invalid request!';
    //It will print an error if the input is null
  }
  else{
    display.textContent = input;
    //Otherwise it will display the text
  }
  body.append(display);
}

//Button and listener for the `click here to print the weather data!` button
//The block of code below was changed from the previous example.
var displayBtn = document.querySelector('#printWeather')
displayBtn.addEventListener('click',function(){
  var latitude = document.querySelector('#latitude').value 
  var longitude = document.querySelector('#longitude').value
  getWeatherData(printWeatherData, latitude, longitude);
});
```

**CodePen Link:**

<https://codepen.io/steviekong/pen/bPMqzy>.

### A few takeaways

Notice how we executed a chain of functions.

```
displayBtn.addEventListener -> callback anonymous function -> getWeatherData -> xhr.onload -> printWeatherData
```

**This is intentional!**

We structured our code in such a way because everything needs to happen one after the other in `asynchronous`programming.

Also notice we only call the `printWeatherData` function after we get some data from the server!

If we tried to store this data to a global variable or return it at the end of our function, our code will return an `undefined`variable.

This is why we chain our callback functions to perform tasks one after the other only after the data has been retrieved from the server.

# Week 5 - Day 1

# JavaScript Basics X Notes:

## Other events in XMLHTTP requests

### `onerror`

The XMLHttpRequestEventTarget.onerror is the function called when an XMLHttpRequest transaction fails due to an error.

This is on of the more important events as error handling is crucial in any HTTP transaction.

### `onprogress`

The XMLHttpRequestEventTarget.onprogress is the function called periodically with information when an XMLHttpRequest before success completely .

This is useful when we want to show a loading bar or do something else while data is being received from the server.

There are a few more useful events you can take a look at here <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequestEventTarget>

**CodePen Example:** <https://codepen.io/steviekong/pen/NZOqye>

Change the url in the `xhr.open` to an invalid url to see the `onerror` working!

### HTTP POST

We don't just want to be getting data from a server, we also want to be sending or posting data to a server.

We can do this with the HTTP `POST` method.

Notice how we use the `XMLHttpRequest.setRequestHeader()` method to send some important header information to the server.

<https://reqres.in/> is a free api that lets you send and receive fake data to test your front end webpages.

Lets use this to send some form data and receive a response!

**CodePen Example:** <https://codepen.io/steviekong/pen/OeByrP>

### HTTP headers

**What are HTTP headers?**

HTTP headers allow the client and the server to pass additional information with the request or the response. An HTTP header consists of its case-insensitive name followed by a colon ':', then by its value (without line breaks).

This can often be useful when we need to send additional `Meta-data` to a server.

We can use the `XMLHttpRequest.setRequestHeader(header, value)` method to do this.

This can often be useful when you need to send tokens to authenticate your request.

Remember to set your headers after you call the `open()` method but before you call the `send()` method.

**Example:**

```
xhr.open("POST", 'https://reqres.in/api/users')
xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');
xhr.send(json);
```

Here the header is `Content-type` and the value is `application/json; charset=utf-8`.



# Week 5 - Day 3

## Algorithms:

Link to slides is here <https://docs.google.com/presentation/d/1QOds5GbJSkFHrx__Ml2cGqCmvG9s6MOWclll53SfJ18/edit?usp=sharing>



# Week 5 - Day 3

# Introduction to Data Structures

**What is a data structure?**

According to wikipedia, "In computer science, a data structure is a data organization, management, and storage format that enables efficient access and modification".

**What does this mean?**

As programmers we create data structures to represent real world data like bank accounts, social relationships, maps etc.

We do this so that we can efficiently manage data on a computer, efficiently access data and efficiently modify this data.

### There are 2 types of data structures:

***Linear:*** A data structure is said to be linear if its elements form a sequence.

**Examples:**

- Arrays
- Lists
- Stack
- Set
- Queue

***Non-linear:*** A data structure is said to be non-linear if its elements do not form a sequence.

**Examples:**

- Trees
- Graphs
- Hash-based structures

There are many different data structures as you can see and they all store and manipulate data in different ways. We have to start somewhere to lets start with an easy data structure.

## Stack

A stack is a linear data structure that has 3 important operations/methods:

- **push** which adds an element to the top of the stack.
- **pop** which removes an element from the top of the stack and returns it.
- **peek** which looks at the top of stack but doesn't remove any element.

A stack looks like what a stack of any objects looks like.

[![img](https://github.com/masai-school/full-stack-dev/raw/master/course/week_05/day_3/images/stack_stones.jpg)](https://github.com/masai-school/full-stack-dev/blob/master/course/week_05/day_3/images/stack_stones.jpg)

In the above image you can only add or remove rocks from the top of the stack.

In much the same way you can `push` data to the top of the stack and then `pop` data from the top of the stack.

Stacks are also known as a LIFO (last in, first out) data structure due to the nature of `push` and `pop`.

A animation of a stack in action <http://www.cs.armstrong.edu/liang/animation/web/Stack.html>



# Week 6 - Day 1

JavaScript Basics XI notes:

# Introduction to ES6 and Beyond

JavaScript is an ever growing languages and new features are introduced all the time.

The ES6 or ECMAScript 2015 introduced tons of new useful features. All modern JavaScript frameworks use many features from from ES6 and you will have to write in ES6 to be able to use them.

A lot of this tutorial and examples are taken from Luke Hoban's ES6 features repository, <https://github.com/lukehoban/es6features#readme>, please give it a star if you liked it!

Lets learn some of these new features now:

## Arrow function expressions

Arrow functions are a simpler and more compact way of writing functions in JavaScript.

Take a look at the examples in the codepen of `functions`

**Example**

```
// Example of ES5 add function

function add(x, y){
  return x + y;
}

console.log(add(3,4));

//Example of ES6 add function

var add = (x, y) => x + y;

console.log(add(3,4));
```

As you can see, the syntax is shorter and concise.

This is also really useful in callback functions.

**Example:**

```
var arr = [1, 2, 3, 4, 5];

//ES5 callback

var timesTwo = arr.map(function(element){
    return element*2;
});
console.log(timesTwo);

// When the only statement in an arrow function is `return`, we can remove `return` and remove
// the surrounding curly brackets
var timesThree = arr.map(element => element*3);

console.log(timesThree);

// When there is only one parameter, we can remove the surrounding parentheses. But we have to include the return statement in a multi-line arrow function. 

var timesFour = arr.map(element =>{
    return element * 4;
})
```

The key difference between arrow functions and ES5 functions is how they handle the `this` value.

In ES5 functions, each function has its own `this` value. This is not very ideal when you are doing object oriented programming.

ES6 Arrow function do not have a `this`. When this is accessed within an arrow function, it is taken from the parent scope.

There are many more quirks and features of arrow functions that I encourage you to read <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions>

If you need an in-depth understanding of arrow functions vs ES5 functions I encourage you to read this article <https://medium.com/@oprearocks/es6-arrow-functions-in-depth-f241d49ede33>.

## let and const

`let` allows you to declare variables that are limited to a scope of a block statement, or expression on which it is used, unlike the var keyword, which defines a variable globally, or locally to an entire function regardless of block scope.

What does this mean?

You may have encountered this.

```
function varTest() {
  var x = 1;
  if (true) {
    var x = 2;  // same variable!
    console.log(x);  // 2
  }
  console.log(x);  // 2
}
```

As you can see, the scope of `var` is for the entire function. This can be really inconvenient when you start to write very large functions or large programs where you many want to alter the value of globals.

Same examples with `let`

```
function varTest() {
  let x = 1;
  if (true) {
    let x = 2;  // different variable!
    console.log(x);  // 2
  }
  console.log(x);  // 1
}
```

MDN documentation <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let>

`const` produces block scoped constants. This means unlike `let` their value cannot be changed after initialization. If you try to reinitialize it, an error will be produced.

```
const x = 1;

x =2; //This will produce an error!
 
```

This is often useful when declaring globals who's value will not change over the execution of the program.

MDN documentation <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const>

From now on you should mostly be using `let` and `const`, `var` should only be used in very specific instances.

If you want an in-depth explanation on `let` vs `const` vs `var` read this <https://tylermcginnis.com/var-let-const/>

## Class

Classes are syntactical sugar over the existing object oriented model in JavaScript. This means that it does not introduced any new features but improves upon old features.

They are similar to function constructors that you have already studied but give you much more functionality with less code.

**Example:**

```
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}

let box = new Rectangle(12, 13);
```

The `constructor` is a special function for initializing objects created with `class`. They work similar to function constructors.

They also support simple instance methods/functions with short declaration syntax.

```
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }

  area(){
    return this.height * this.width;
  }

}

let box = new Rectangle(12, 13);
box.area();
```

Classes also support inheritance which means they can take properties and functions from other classes.

For example lets say we have two classes `Car` and `Sedan`.

```
Car:
class Car{
  constructor(horsePower){
    this.horsePower = horsePower;
    this.fuel = 100;
  }

  consumeFuel(amount){
    this.fuel -= amount;
  }
}
let myCar = new Car(102);
Sedan
class Sedan{
  constructor(name){
    this.name = name;
  }
  printName(){
    console.log(this.name);
  }
}
var mySedan = new Sedan('Civic');
```

Right now they are independent. Lets say we want `Sedan` to inherit or get the properties and functions of the `Car` object.

We can use the `extends` keyword to make `Sedan` a child of the `Car` class. This will allow `Sedan` to get properties and methods/functions of the parent class `Car`.

```
class Car{
  constructor(horsePower, name){
    this.horsePower = horsePower;
    this.fuel = 100;
    this.name = name;
  }

  consumeFuel(amount){
    this.fuel -= amount;
  }
}

class Sedan extends Car{
  printName(){
    console.log(this.name)
  }
}

let mySedan = new Sedan(150, 'Civic');
mySedan.consumeFuel(10);
console.log(mySedan.fuel);
mySedan.printName();
```

MDN documentation <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes>

### The `super` keyword

Now what if we need to access the parent class's properties or functions in the child class?

Also what if we want to declare a constructor for our child class?

The `super`keyword is used to access and call functions on an object's parent.

Lets update our above example with the super keyword.

```
class Car{
  constructor(horsePower, name){
    this.horsePower = horsePower;
    this.fuel = 100;
    this.name = name;
  }

  consumeFuel(amount){
    this.fuel -= amount;
  }
}

class Sedan extends Car{
  constructor(horsePower, name, numSeats){
    super(horsePower, name);
    this.numSeats = numSeats;
  }
  printName(){
    console.log(this.name);
  }

  updateHorsePower(input){
    super.horsePower = input;
  }
}

let mySedan = new Sedan(150, 'Civic', 4);

mySedan.updateHorsePower(300);

mySedan
```

It is important to note that when used in a constructor, the super keyword appears alone and must be used before the this keyword is used.

MDN documentation <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super>

## Template Literals

Template literals are string literals that allow you to embed expressions and values within strings.

Template literals are enclosed by the back-tick (` `) or grave accent character instead of double or single quotes.

**Example:**

```
let x = "Hello world!" //This is a regular string literal
let y = `Hello World!` //This is a template literal
```

**Some Cool features of template literals:**

Makes it really easy to write Multi-line strings:

```
`This is the first line
and this is the second line.`
```

**Output:**

```
'This is the first line\nand this is the second line.'
```

Notice how the `\n` newline character is automatically inserted.

The key feature is expression interpolation or the ability to embed expressions within strings.

```
var a = 5;
var b = 10;
console.log(`Fifteen is ${a + b} and not ${2 * a + b}.`);
```

This saves time on writing and managing a lot of `+` operators within strings.

You can also call functions within these expressions.

There are a few more cool features that you can read about on MDN <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals>

There are many more features we have yet to discuss but we will get to them at a later time.

I really encourage you read a few if not all the extra links and documentation given to you.





# Week 6 - Day 2

# More Sorting Algorithms

Lets continue to learn more sorting algorithms.

## Insertion Sort

Insertion sort is similar to the algorithms we have studied before. However it follows a slightly different core idea.

**Simple Steps:**

1. Get an array of unsorted numbers
2. Set a marker (i) for the sorted section after the first number in the list
3. Repeat steps 4 through 6 until the unsorted section is empty
4. Select the first unsorted number
5. Swap this number to the left until it arrives at the correct sorted position.
6. Advance the marker to the right one position.
7. Stop.

**Pseudo code:**

```
insertionSort(array)
  for i = 1 to array.size
    key = array[i]
    j = i - 1
      while array[j] > key and j > = 0
        array[j+1] = array[j]
        j = j–1
      end while 
      array[j+1] = key
  end for
end insertionSort
```

**Visualizer:** <https://visualgo.net/bn/sorting> Select insertion sort on the navigation bar!

## Recursion

There are 2 primary approaches to solving problems when you have to iterate over some values or generate values in some pattern.

- Iterative : Using for loops, while loops etc. Basically loops.
- Recursion

We write recursive algorithms using a **recursive function**.

But what is a recursive function?

in the simplest terms, a recursive function is a function that calls itself.

Lets take a look at a simple example:

The following function will print all the numbers from the initial value of curr to 0.

```
function  nums(curr){
    if(curr === 0){
        console.log(curr)
        return curr;
    }
    console.log(curr);
    return nums(curr - 1);
}
nums(10)
```

**Output:**

```
10
9
8
7
6
5
4
3
2
1
```

How does this work?

Recursion calls the same function `nums` with different values. It does this until `curr === 0` and then it returns the curr and exits.

**Base Case:** `curr === 0` is our base case, all recursive algorithms must have a base case. These are values after which the recursion ends.

How to think about recursion in a meaningful way ?

Lets say we are in a room and the room has 1 door with a number on it. You are looking for door with number 0 as it has a treasure in it.

There is a number on the door `10`.

You open that door and you see a door with the number `9`.

You keep opening doors that decrease in value until you get to the door with the number `0`. You open it and you get your treasure!

**Lets look at another example:**

This program adds numbers from the initial value to 0.

```
function sum(curr){
    if(curr === 0){
        return curr;
    }
    return curr + sum(curr-1);
}
sum(5)
```

**Output:**

```
5 
5+4
5 + 4 + 3
5 + 4 + 3 + 2
5 + 4 + 3 + 2 + 1
5 + 4 + 3 + 2 + 1 + 0 = 15
```

15 is the final result and is the output.

Coming back to our door analogy:

1. We are in a room with doors but each room contains a decreasing number of gold coins.
2. The first room has 5 coins so we pick those coins up and open the next door.
3. the second room has 4 coins so we pick those up and add it to our collection. Now we have 9 coins in total.
4. We keep opening doors and collecting coins until we get to the door with 0 coins and we end our search.
5. At the end we have 5 + 4 + 3 + 2 + 1 = 15 coins!

**Lets look at one last example:**

This is for the Fibonacci series.

```
function fibo(n){
    if(n < 2){
        return n;
    }
    return fibo(n-1) + fibo(n-2);
}
fibo(5)
```

[![img](https://github.com/masai-school/full-stack-dev/raw/master/course/week_06/day_2/fibo.png)](https://github.com/masai-school/full-stack-dev/blob/master/course/week_06/day_2/fibo.png)

(Diagram from Stephen Grider’s “The Coding Interview Bootcamp“ course on Udemy.com)

The tree gives us a great way to visualize recursion. The tree keeps growing until it reaches the base case.

