**Week 2 - Day 2

#### Session 1

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



### Week 2 - Day 3

#### Session 1

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



### Week 3 - Day 2

**Prerequisite**

<https://github.com/masai-school/full-stack-dev/blob/master/course/week_2/day_2/w2_day_2_notes1.md>

#### Session 1

```
.`
`,`
`+`
`~`
`>`
`space
```

**CSS Combinators**

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

**Multiple Selectors, Same Properties (,)**

The comma in a CSS selector separates multiple selectors within the same styles.

```
selector1, selector2 { style properties }
```

<https://codepen.io/nrupuld/pen/xopQEZ>

**Type & Class (.)**

```
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
```

<https://codepen.io/nrupuld/pen/zVweGK>

**Adjacent Sibling Selector (+)**

The adjacent sibling combinator (`+`) separates two selectors and matches the second element only if it *immediately*follows the first element, and both are children of the same parent element.

```
former_element + target_element { style properties }
```

<https://codepen.io/nrupuld/pen/XLVyzm>

**General Sibling Selector (~) **

The **general sibling combinator** (`~`) separates two selectors and matches the second element only if it follows the first element (though not necessarily immediately), and both are children of the same parent

```
former_element ~ target_element { style properties }
```

<https://codepen.io/nrupuld/pen/pXpQLM>

**Child Combinator (>)**

The **child combinator** (`>`) is placed between two CSS selectors. It matches only those elements matched by the second selector that are the children of elements matched by the first.

```
selector1 > selector2 { style properties }
```

<https://codepen.io/nrupuld/pen/rEpQRL>

**Descendant Combinator ( )**

The **descendant combinator** typically represented by a single space (` `) character combines two selectors such that elements matched by the second selector are selected if they have an ancestor element matching the first selector.

```
selector1 selector2 { style properties }
```

<https://codepen.io/nrupuld/pen/Oezaed>

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



## Week 5 - Day 2

### Cascading Style Sheets

**Inheritance**

In CSS, inheritance controls what happens when no value is specified for a property on an element. Refer to any CSS property definition to see whether a specific property inherits by default ("Inherited: yes") or not ("Inherited: no").

<https://developer.mozilla.org/en-US/docs/Web/CSS/color> - `Inherited yes`
<https://developer.mozilla.org/en-US/docs/Web/CSS/border> - `Inherited no`

<https://codepen.io/nrupuld/pen/WqYJqE> - Color Inherited <https://codepen.io/nrupuld/pen/WqYyvX> - Border Non-Inherited

**Important**

In CSS, there is a special piece of syntax you can use to make sure that a certain declaration will *always* win over all others: `!important` (even inline css)

<https://codepen.io/nrupuld/pen/JQeZEP>

<https://codepen.io/nrupuld/pen/mZQjGQ>

**Attribute Selector**

The CSS **attribute selector** matches elements based on the presence or value of a given attribute.<https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors>

<https://codepen.io/nrupuld/pen/ydQEzQ>

**Pseudo Classes**

A CSS pseudo-class is a keyword added to a selector that specifies a special state of the selected element(s).
<https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes>

```
selector:pseudo-class {
  property: value;
}
```

<https://codepen.io/nrupuld/pen/BgGPQG>

**Pseudo Element**

A CSS pseudo-element is a keyword added to a selector that lets you style a specific part of the selected element(s).
<https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements>

```
selector::pseudo-element {
  property: value;
}
```

<https://codepen.io/nrupuld/pen/xoQJOR>

**Specificity**

The amount of specificity a selector has is measured using four different values (or components), which can be thought of as thousands, hundreds, tens and ones — four single digits in four columns:

1000 - Inline/Style Tag
Hundreds - One for each ID Selector
Tens - One for each class selector, attribute selector, pseudo-class contained inside the overall selector.
Ones - One for each element selector, pseudo-element contained inside the overall selector.

**Note: Universal selector (\*), combinators (+, >, ~, ' ') and negation pseudo-class (:not) have no effect on specificity.**

| Selector                                | Thousands | Hundreds | Tens | Ones | Total |
| --------------------------------------- | --------- | -------- | ---- | ---- | ----- |
| h1                                      | 0         | 0        | 0    | 1    | 0001  |
| h1 + p                                  | 0         | 0        | 0    | 2    | 0002  |
| h1 + p::first-letter                    | 0         | 0        | 0    | 3    | 0003  |
| li > a[href*="en-US"] > .inline-warning | 0         | 0        | 2    | 2    | 0022  |
| .class1                                 | 0         | 0        | 1    | 0    | 0010  |
| ul.class1                               | 0         | 0        | 1    | 1    | 0011  |
| #id1                                    | 0         | 1        | 0    | 0    | 0100  |
| style                                   | 1         | 0        | 0    | 0    | 1000  |

<https://codepen.io/nrupuld/pen/VJVBBx>

<https://codepen.io/nrupuld/pen/ydQqrJ>



## Week 5 - Day 2

### Media Queries

<https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries>

**Exact Width** (Exact Width)

```
@media (width: 480px) {
  div {
    background: red;
  }
}
```

**Min Width** (Specified Width and Above)

```
@media (min-width: 600px) {
  div {
    background: green;
  }
}
```

**Max Width** (Specified Width And Below)

```
@media (max-width: 1024px) {
  div {
    background: blue;
  }
}
```

#### Typical Device Breakpoints

```
/* Extra small devices (phones, 600px and down) */
@media only screen and (max-width: 600px) {...} 

/* Small devices (portrait tablets and large phones, 600px and up) */
@media only screen and (min-width: 600px) {...} 

/* Medium devices (landscape tablets, 768px and up) */
@media only screen and (min-width: 768px) {...} 

/* Large devices (laptops/desktops, 992px and up) */
@media only screen and (min-width: 992px) {...} 

/* Extra large devices (large laptops and desktops, 1200px and up) */
@media only screen and (min-width: 1200px) {...}
```

### Flexbox

The Flexible Box Module, usually referred to as flexbox, was designed as a one-dimensional layout model, and as a method that could offer space distribution between items in an interface and powerful alignment capabilities. When we describe flexbox as being one dimensional we are describing the fact that flexbox deals with layout in one dimension at a time — either as a row or as a column.

### Grids

**CSS Grid Layout** excels at dividing a page into major regions or defining the relationship in terms of size, position, and layer, between parts of a control built from HTML primitives. Like tables, grid layout enables an author to align elements into columns and rows. However, many more layouts are either possible or easier with CSS grid than they were with tables.

## Week 5 - Day 4

### Flex

<https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout>

```
display: flex;
```

Displays an element as a block-level flex container

**flex-direction**

```
flex-direction: row|row-reverse|column|column-reverse;
```

The direction of the flexible items
<https://codepen.io/nrupuld/pen/GbeKbN?editors=1100#0>

**flex-wrap**

```
flex-wrap: wrap|nowrap
```

the flexible items should wrap or not.
<https://codepen.io/nrupuld/pen/VJRwyP>

**flex-flow**

```
flex-flow: flex-direction flex-wrap
```

**flex-basis**

```
flex-basis: value;
```

Specifies the initial length of a flexible item

<https://codepen.io/nrupuld/pen/ewXNYG>

**flex-grow**

```
flex-grow: value;
```

How much the item will grow relative to the rest of the flexible items inside the same container

<https://codepen.io/nrupuld/pen/bPZGPO>

**flex-shrink**

```
flex-shrink: value;
```

How the item will shrink relative to the rest of the flexible items inside the same container

<https://codepen.io/nrupuld/pen/vqPOLw>

**flex**

```
flex: flex-grow flex-shrink flex-basis
```

### Grid

<https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout>

```
display: grid
grid-template-columns: value value value;
grid-template-rows: value value;
grid-gap: value;
```

<https://codepen.io/nrupuld/pen/QXobeQ>

**grid-area**

```
grid-area: grid-row-start / grid-column-start / grid-row-end / grid-column-end 
```

<https://codepen.io/nrupuld/pen/mZoepM>