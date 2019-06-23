**CSS Selectors (Simple)**

**Universal Selector**

The CSS universal selector (`*`) matches elements of any type.

```
/* Selects all elements */
* {
	color: black
}
```

<https://codepen.io/nrupuld/pen/xoOpeB>

**Type Selector**

The CSS type selector matches elements by node name. In other words, it selects all elements of the given type within a document.

```
/* All <div> elements. */
div {
  color: red;
}
```

<https://codepen.io/nrupuld/pen/qzNpez>

**Class Selector**

The CSS class selector matches elements based on the contents of their `class` attribute.

```
/* All elements with class="class1" */
.class1 {
  color: yellow;
}
```

<https://codepen.io/nrupuld/pen/agZqbM>

**ID Selector**

The CSS ID selector matches an element based on the value of its `id` attribute. In order for the element to be selected, its `ID` attribute must match exactly the value given in the selector.

```
/* The element with id="demo" */
#demo {
  color: purple;
}
```

<https://codepen.io/nrupuld/pen/qzNxaW>

**Defines a unique identifier (ID) which must be unique in the whole document**

WRONG

```
<div id="demo"></div>
<div id="demo"></div>
```

CORRECT

```
<div id="demo1"></div>
<div id="demo2"></div>
```

### CSS Precedence

**Multi Classes (Different Properties)**

```
<div class="class1">This is first div</div>
<div class="class1 class2">This is second div</div>
<div class="class1 class2 class3">This is third div</div>
```

<https://codepen.io/nrupuld/pen/KjMQqB>

**Multiple Definitions**

```
<div class="class1">This is first div</div>
<div class="class2">This is second div</div>
```

<https://codepen.io/nrupuld/pen/bPeLzj>

**Class Ordering (Same Properties)**

```
<div class="class1 class2">This is first div</div>
<div class="class2 class1">This is second div</div>
<div class="class3 class4">This is first div</div>
<div class="class4 class3">This is first div</div>
```

<https://codepen.io/nrupuld/pen/zVBRdV>

**Multi Classes & Ordering (Same & Different Properties)**

```
<div class="class1 class2">This is first div</div>
<div class="class2-1 class1">This is second div</div>
<div class="class3 class4">This is third div</div>
<div class="class4 class3 class5">This is fourth div</div>
```

<https://codepen.io/nrupuld/pen/qzNxKb>

**Priority**

Style Tag > ID Selector > Class Selector > Type Selector > Universal Selector

```
<body>
    Hello
    <div>This is first div</div>
    <div class="class1">This is second div</div>
    <div class="class1" id="id1">This is third div</div>
    <div class="class1" id="id2" style="color:red">This is third div</div>
 </body>
```

<https://codepen.io/nrupuld/pen/ewzVja>



**Coding Standards, Following Conventions, Naming, Clean Code**

[Code Quality](https://xkcd.com/1513/) [Code Quality 2](https://xkcd.com/1695/) [Code Quality 3](https://xkcd.com/1833/) [Good Code](https://xkcd.com/844/)

> *Any fool can write code that a computer can understand. Good programmers write code that humans can understand*
>
> *– Martin Fowler*

### NAMING

BAD

```
.class1 {

}
.class2 {

}
.class3 {

}
.class4 {

}

#id1 {

}
#id2 {

}

function my_function() {

}

function yourFuntion() {

}

function function1() {

}

function function2() {

}

function this_is_the_name_of_a_very_long_function_and_is_written_by_me() {

}

function ab() {

}
.element_box {

}

.red_background {

}

.center_align {

}

#displayBox {

}

#profilePic {

}

function displayName() {

}

function getGender() {

}
```

**DON'T CREATE CONFUSION**

BAD

```
.redBox {
	background-color: black;
}

.leftAlign {
	text-align: right;
}
```

GOOD

```
.redBox {
	background-color: red;
}

.leftAlign {
	text-align: left;
}
```

### INDENTATION

BAD

```
<div>
<div>
<p>
</p>
<ul>
<li>
</li>
</ul>
</div>
</div>
```

GOOD

```
<div>
    <div>
        <p>
        </p>
        <ul>
            <li></li>
        </ul>
    </div>
</div>
```

### SPACES

```
lifewithoutspaces
life_without_spaces
// snake_case
lifeWithoutSpaces
// camelCase
```

BAD

```
dOntINvent_YOURown_casE
```

### UNIFORMITY

BAD

```
function setName() {

}

function set_email() {

}

.blue_box {

}

.redBox {

}
```

GOOD

```
function setName() {

}

function setEmail() {

}

.blueBox {

}

.redBox {

}
function set_name() {

}

function set_email() {

}

.blue_box {

}

.red_box {

}
```

### SPACING & READABILITY

BAD

```
.class1 {color:red;padding:10px}
```

GOOD

```
.class {
	color: red;
	padding: 10px;
}
```

BAD

```
function function1() {
	doing set A 1
    doing set A 2
    doing set B 1
    doing set B 2
}
function function2() {

}
function function3() {

}
```

GOOD

```
function function1() {
	doing set A 1
	doing set A 2
	
	doing set B 1
	doing set B 2
}

function function2() {

}

function function3() {

}
```

### COMMENTS

BAD

```
// this class set the background color of an element to red
.redBox {
	background-color: red;
}

/**
If a number is not divisible by 2 then it is called odd number
To find a number is odd or not we divide it by 2
  - if the remainder is 1 then it is a odd number
  - if the remainder is 0 then it is a even number
**/
function isOddNumber() {

}
```

GOOD

```
// Styles for the comment box used for Posts and Videos 
.mainCommentBox {

}

/**
email & mobile - mandatory
dob & city - optional

**/
function checkRegistrationFields() {

}
```

### LEARN MARKDOWN

<https://guides.github.com/features/mastering-markdown/>