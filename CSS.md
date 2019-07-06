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


Prerequisite

https://github.com/masai-school/full-stack-dev/blob/master/course/week_2/day_2/w2_day_2_notes1.md

Session 1
.
,
+
~
>
space

CSS Combinators

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
Child node: A node directly inside another node id2 and id6 are child nodes of id1 also id3 is child node of id2 and id4 is child node of id3
Descendant node: A node anywhere inside another node. id2 and id6 are child nodes of id1 and also descendants. id3 id4 id5 are not child nodes of id1 but descendants
Sibling nodes: Nodes that sit on the same level. In the above example id2 and id6 are siblings and id3 and id5 are also siblings
Multiple Selectors, Same Properties (,)

The comma in a CSS selector separates multiple selectors within the same styles.

selector1, selector2 { style properties }
https://codepen.io/nrupuld/pen/xopQEZ

Type & Class (.)

elemtype.class { style properties }
<div>This is the first div</div>
<div class="class1">This is the second div</div>
<div class="class2">This is the third div</div>
<p>This is the first paragraph</p>
<p class="class1">This is the second paragraph</p>
<p class="class2">This is the third paragraph</p>
/* All <div> elements */
div {
  color: red;
}

/* All elements with class="class1" */
.class1 {
  color: green;
}

/* All <p> elements with class="class2" */
p.class2 {
  color: violet;
}
https://codepen.io/nrupuld/pen/zVweGK

Adjacent Sibling Selector (+)

The adjacent sibling combinator (+) separates two selectors and matches the second element only if it immediately follows the first element, and both are children of the same parent element.

former_element + target_element { style properties }
https://codepen.io/nrupuld/pen/XLVyzm

**General Sibling Selector (~) **

The general sibling combinator (~) separates two selectors and matches the second element only if it follows the first element (though not necessarily immediately), and both are children of the same parent

former_element ~ target_element { style properties }
https://codepen.io/nrupuld/pen/pXpQLM

Child Combinator (>)

The child combinator (>) is placed between two CSS selectors. It matches only those elements matched by the second selector that are the children of elements matched by the first.

selector1 > selector2 { style properties }
https://codepen.io/nrupuld/pen/rEpQRL

Descendant Combinator ( )

The descendant combinator typically represented by a single space ( ) character combines two selectors such that elements matched by the second selector are selected if they have an ancestor element matching the first selector.

selector1 selector2 { style properties }
https://codepen.io/nrupuld/pen/Oezaed


JS CSS & Style Manipulation

snake_case
camelCase
Commonly used case in css

caterpillar-case dash-case hypen-case kebab-case

setAttribute

The setAttribute() method adds the specified attribute to an element, and gives it the specified value.

If the specified attribute already exists, only the value is set/changed.

element.setAttribute(attributename, attributevalue)
Adding Classes & IDs

https://codepen.io/nrupuld/pen/VJMNBw

Other Attributes

https://codepen.io/nrupuld/pen/qzPwzW?editors=1010

Using loops & conditional operators

https://codepen.io/nrupuld/pen/KjXLpe

removeAttribute

The removeAttribute() method removes a given attribute of a specific HTML element.

ele.removeAttribute(name);
https://codepen.io/nrupuld/pen/gNXYOg

style

The HTMLElement.style property is used to get as well as set the inline style of an element.

The style property has the same (and highest) priority in the CSS cascade as an inline style declaration set via the style attribute.

ele.style.property = value
https://codepen.io/nrupuld/pen/BgmBGV

Using loops

https://codepen.io/nrupuld/pen/OeOJyB

CSS Properties DOM Notation accessed from JS

https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference
