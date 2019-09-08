- # Week 6 - Day 3

  ## Introduction to ReactJS

  **What is React Js?**

  In short, React is a JavaScript library for building web interfaces. A library is a group of files that contains objects and functions/methods that collectively accomplish a useful task.

  You have already been using in-built libraries in JavaScript and React is just a library written by a third-party.

  React is a declarative, efficient, and flexible JavaScript library for building user interfaces.

  We will be closely following the ReactJS official docs available on <https://reactjs.org/>

  ## Getting started

  We will be doing most of our development on local JS files but all the examples will be on codepen.io

  Lets write a simple hello world program.

  <https://codepen.io/steviekong/pen/PrrMXE?editors=1010>

  You might already recognize most of the html code.

  Lets look at what is new:

  ```
  <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.26.0/babel.min.js"></script>
   <script crossorigin src="https://unpkg.com/react@16/umd/react.development.js"></script>
  <script crossorigin src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
  ```

  Here we import the ReactJS libraries over the Internet through something called a CDN.

  Make sure you have these three lines in your `body` tag when you write any react applications in HTML files.

  ```
  ReactDOM.render(
    <h1>Hello, world!</h1>,
    document.getElementById('root')
  );
  ```

  `ReactDOM` is a global object provided by the React JS library. It contains a `render` functions that accepts 2 arguments.

  The first argument is a **JSX** object and the second is the `HTML` container element onto which we are rendering the the `JSX` as a child.

  When the `render` function is called it renders a react object into the DOM as a child of the `container` element. In this case the `container` is a `div` element with the `id` ***root***.

  ## JSX

  **What is JSX?**

  In formal terms JSX is a preprocessor that adds XML or HTML syntax to Javascript. There are other preprocessors you could use but JSX and React go hand in hand so it is very easy to use the two of them.

  You could also write react without JSX but JSX makes react much more readable as it is visually similar to HTML and much easier to write. For more about react without JSX, read this <https://reactjs.org/docs/react-without-jsx.html>.

  JSX produces "Elements" which you can then render to the DOM.

  **Lets try writing some JSX**

  ```
  const welcome = <h1>Welcome to Masai School</h1>
  ```

  This is a simple JSX element store in the constant called `welcome`.

  You can then render it by calling `ReactDOM.render`.

  Take a look at the following example.

  <https://codepen.io/steviekong/pen/qzeEZe>

  **Lets write some larger JSX elements:**

  <https://codepen.io/steviekong/pen/LKwxPd?editors=1000>

  Notice how we wrapped all the elements in a `div` tag. This is because JSX must return a single element. Several JSX elements who are siblings with no parent are invalid JSX and will not transpile.

  **Valid JSX:**

  ```
  <div>
  <h1>Shopping Cart</h1>
  <ul>
    <li>Apples</li>
    <li>Oranges</li>
    <li>Banana</li>
  </ul>
  </div>
  ```

  **Invalid JSX:**

  ```
  <h1>Shopping Cart</h1>
  <ul>
    <li>Apples</li>
    <li>Oranges</li>
    <li>Banana</li>
  </ul>
  ```

  **Embedding Expressions within JSX:**

  You can also embed JavaScript expressions within JSX. We do this by wrapping the expressions within `{}` curly brackets.

  <https://codepen.io/steviekong/pen/pXMpqQ>

  <https://codepen.io/steviekong/pen/pXMaJY?editors=1000>

  **JSX evaluates to a JavaScript Object:**

  After the code compiles, JSX expressions become regular javascript objects. This means just like any other other object, you can store it inside variables, return it from functions, use it within if statements, for loops etc.

  <https://codepen.io/steviekong/pen/orKqXd?editors=1010>

  **Updating Rendered Elements:**

  React elements are immutable which means that once you create an element it cannot be changed in any way. However you can render element again to get different results.

  Here is an example from the react docs given here <https://reactjs.org/docs/rendering-elements.html>

  Here is that same example on codepen <https://codepen.io/steviekong/pen/bPXMPM>

  As you can see it calls the function to re-ender the `h2` element with new values each second.

  If you inspect the element within the developer console, you can see that only that time string value within the `h2` element is being updated, not the whole DOM and not even the other text within the `h2` element.

  This is because React is smart and uses a [**Virtual DOM**](https://reactjs.org/docs/faq-internals.html) and a smart [**Reconciliation Algorithm**](https://reactjs.org/docs/reconciliation.html) to compare the difference and only perform the necessary changes to the DOM.

  Lets look at a simple example with a pre-defined button. The DOM will render after the button is clicked.

  <https://codepen.io/steviekong/pen/OeKENZ>

  **Note:** Most react applications will only call render once. In the next few classes we will learn about components and state which we will use to render the DOM in a much more powerful way.



# Week 6 - Day 4

## Introduction to ReactJS Part 2

## Comments

You can add comments to JSX elements with the `{/* */}` syntax.

**Syntax:**

```
let jsx = (
    <div>
        {/* This is a comment. None of this code will be executed! */}
    </div>
);
```

## Components

Components are the building blocks of React. Everything you do in react has to do with components and interactions between components.

We can define react components with functions but for this tutorial we will only be using ES6 classes as they give us a lot of really useful functionality in react over regular JavaScript functions.

Lets take a look at an example of a simple component.

<https://codepen.io/steviekong/pen/YmKGZz>

In the above example we created a simple class called `Header` which extends the `React.component` class. This is a component in React.

Because `Header` is a child of the `React.component` class, it inherits several useful react properties like local state, life-cycle hooks and props.

We will discuss some of these properties soon.

Take a look at these two lines of code.

```
const head = <Header />
          
ReactDOM.render(head, document.getElementById('root'))
```

`head` contains the JSX component that we created called `Header` and we render the component to the DOM using `ReactDOM.render`.

We could have also written it in this way:

```
ReactDOM.render(<Header />, document.getElementById('root'))
```

The `Header` tag here is a **self-closing tag**, in JSX any element can be written with a self closing tag but all element in JSX ***must*** be closed.

**Note:** All user defined components must be **Capitalized**!

**Correct**

```
class Header extends React.Component
```

**Wrong**

```
class header extends React.Component
```

## Composing two or more Components together

You can also define multiple components and compose them together.

This feature is core to react as you could make changes to one small component in react without affecting other components.

<https://codepen.io/steviekong/pen/YmKNGj>

In the above example I could make any changes to the parent or child components but all the changes are contained within that component.

This feature is especially useful when you have a large web-page with many dynamic elements.

When you work with react you must work on breaking down each part of your webpage into small workable components.

## Classes in JSX

JSX and HTML seem very similar but there are small differences.

Since the keyword `class` is also present in JavaScript we cannot use it within JSX.

So in JSX we use `className` instead.

**HTML:**

```
<div class = "container">></div>
```

**JSX:**

```
<div className = "container"></div>
```

This is the same for the `for` html attributes use in `<label>` elements. In JSX it is `htmlFor`.

Many html attributes need small changes to become JSX attributes.

You can read about it here <https://reactjs.org/docs/dom-elements.html>. Scroll to the button of the page to see the supported attributes.

In general most attributes are the same as their HTML counter part but in **camelCase**.

## In-line Styling in JSX

Applying styles in JSX are also a little different.

We apply styles using the style attribute but all the CSS properties must be in **camelCase**.

**HTML**

```
<div style = "background-color: red;"></div>
```

**JSX**

```
<div style={{backgroundColor: 'red'}}></div>
```

You might have noticed that we actually passed a object literal to the style attribiute!

This is because the style attribute actually accepts a regular JavaScript object literal to render css.

**Example:**

```
const myStyle = {
    color : 'blue',
    border: '5px solid yellow';
}
<div style = {myStyle}>Hello World!</div>
```

Lets see an example in codepen:

<https://codepen.io/steviekong/pen/OKLBgQ?editors=1000>

Notice how I defined the `headerStyle` object within the render function! This is completely fine in react as `render()` is just like any other JavaScript.

**Note**: We want to avoid using in-line styles in react in general. We will learn how to link external css files after we start our react apps using npm.

## Props

React components are very similar to functions at a conceptual level. Just like functions you can pass arbitrary inputs to components and then return react elements.

Lets take a look at an example

<https://codepen.io/steviekong/pen/gVYWOR?editors=1000>

Here we pass a `prop` called `username` to the `Header` component.

The key idea behind props is to control the flow of information in react.

Props is primary used as a system to pass information from parent components to child components.

**Parent component --props(information)--> child component**

To see a good example of this lets build a small but useful component.

Lets say we are building the comments section of a social network or blog. Each of the comment components are the same but, the information contained within them is different.

So we can use props to pass information to the child element from the parent element.

<https://codepen.io/steviekong/pen/dxbQZK?editors=1000>



# Week 7 - Day 1

## Introduction to ReactJS Part 3

### Setting up a React app using NPM and nodeJS

While writing react apps into HTML isn't incorrect, it can be tedious.

Most react apps are developed as standalone front-end apps which can then interact with an API backend.

Instead we use the `create-react-app` NPM package developed by Facebook to give us some starter files with `boilerplate` code along with a basic file structure into which we can develop our own ReactJS app.

To read more about the `create-react-app` package you can visit their official github repository <https://github.com/facebook/create-react-app>.

Follow these steps to setup and run a react app locally:

1. Make a directory where you would want to create a react app and `cd` in to the directory.
2. Make sure you have NPM installed by running `npm --version`. This should show you the version number of NPM you have installed.
3. Then run `npm install -g create-react-app`.

**Breaking down this command:**

`npm install <package_name>` is how you install any package in NPM. The `-g` flag tells NPM to install that package globally rather than locally. This allows us to use this package from the command-line. (Note: Some of you might need to run `sudo` before the command, dependent on your systems write permissions.)

If all goes well you should see something like `added 91 packages from 45 contributors in 15.389s` in your terminal.`4. Now run`create-react-app <name_of_your_app>`. This will take a bit of time since this is building a lot of files so be patient!

If all goes well you should get a message that says `Happy Hacking!`.

You will observe that a folder with the name of you app has been created. This contains all the files necessary for your react app. All new files you create will be within this folder.

Before we start creating our app lets understand why we had to go through this process.

**Why did we have do to all of this??**

If you run `sudo du -sh <folder_name>` on the project folder you created you might notice it is around `200`+ MegaBytes!

An obvious question might be, why? What is in this folder? Do I need all of this? Why is it so large? My HTML file was very small!

A large portion of this is taken up by NPM `packages`. These are libraries which contain code that other programmers wrote and have hosted on NPM which is a package manager for NodeJS.

`create-react-app` dependents on these libraries to work correctly so these packages are also called **dependencies**. In many cases these ***dependencies** also dependent on other dependencies and so on..

You can visualize these dependencies here <http://npm.broofa.com/?q=create-react-app>

As you can see, `create-react-app` depends on 83 different dependencies.

You can also use `npm ls` to see all the dependencies on your terminal.

**Babel:**

While there are many dependencies I want to draw you attention to `Babel`. We have used this before by linking it through a script tag.

But, what is `Babel` and what does it do?

Anyone who has read the **HitchHikers Guide to the Galaxy** will know of the Babel fish which can translate between any language in the universe.

Similarly the `Babel` package is used to translate from ES6 and above back to ES5. In our case, Babel also performs the necessary translations from `JSX` syntax to regular JavaScript. This is useful since this allows our code to run on virtually any browser that supports ES5 features.

For this reason `Babel` is often called a Transpiler as it does both translation as well as compilation of Javascript code.

To learn more about `Babel` visit their website `https://babeljs.io/docs/en/`.

**Learning more about the files and folders in the app:**

This should give you a short overview of all the important files and folders in the project/app directory. We will discuss each of these in detail at a later time.

1. `src`: This is where we will put all the JS code we write.
2. `public`: This folder is used to store static files like images, text files, html files, icons etc.
3. `node_modules`: This is the folder where NPM stores all the dependencies for our project. If you LS into that folder you can see all of them. 4.`package.json`: This file contains the configuration for our project including the dependencies as well as some starter scripts.
4. `package-lock.json`: This file contains the exact version numbers for all the dependencies we are using.
5. `README.md`: This file is used to tell any developers or users about your project. It should include information about your project, as well as instructions on how to set it up and run it. Github natively displays this file at the homepage of a repository and you might have seen before.

## Starting and stopping your project

To start your app use `npm start`.

You should see your project running on your browser at the url `localhost:3000`.

To stop your app return to the terminal and press `Control+c`.

When you look at your browser you should get a page with the react logo and a prompt `Edit src/App.js and save to reload`.

Once we change some code in `App.js` we should see the result here.

## Writing a simple Hello World App

Open up the src folder and delete all the files within. We want to start fresh so delete everything in there.

Now create a file called `index.js`.

**Import statements:**

Add these two lines to your code

```
import React from 'react';
import ReactDOM from 'react-dom';
```

What are these statements?

`import` statements allow us to use objects and functions from dependencies or modules.

Lets break down each part of the import statement:

`React` is the variable we want to assign to this import.

We write `from` before we specify the name of the dependency or path to the file we want to include.

`react` is the name of the dependency that we are importing.

You can use `import` statements to import any dependency that you include in your project.

You can also use `import` statements to import JS files that you create.

You can read more about it here <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import>

**Creating and displaying a simple component:**

Open up `public/index.html`. This is a fairly normal HTML file.

Notice there is a div with the `id="root` we will use this as the parent element for our react app to which we will attach all our components to.

Now go back to index.js and create a simple component and render it to the DOM.

```
//Create a React Compoenent
const App = () =>{
    return <h1>Hello world</h1>;
};

//Render it to the DOM
ReactDOM.render(
    <App />, 
    document.getElementById('root')
);
```

The example covered here can be seen at <https://github.com/masai-school/full-stack-dev/tree/master/course/week_7/day_1/session1/hello_world>.

If you want to run the above app locally, you must clone the repository and run `npm install` within the project folder to install all the required dependencies.

## Creating multiple components in different files

When you start working on larger projects you want to structure your project folder in a meaningful way.

Usually a react project will have a separate components folder where all your components are stored.

The task of `index.js` will be to simply call `ReactDOM.render`.

I'm going to create a new project called `multiple_test`.

To start out, I create a folder called `components` within the `src` folder.

In here I'm going to write create a file called `SimpleList.js` which will be a basic list component which will render an ordered list.

Here is the code for the SimpleList component:

```
import React from 'react';

class SimpleList extends React.Component{
    render(){
        return (
            <ol>
                <li>Apple</li>
                <li>Banana</li>
                <li>Watermelon</li>
            </ol>
        );
    }
}

export default SimpleList
```

Here I created a component called `SimpleList`. In the last line I used the `export` statement so that any import statements used in other JS files could have access to the `SimpleList` class that I created here.

For more on import statements check out the MDN documentation <https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export>

I will also create an `App` component which will render multiple `SimpleList` components.

Here is the code for the App component.

```
import React from 'react';
import SimpleList from './SimpleList.js'

class App extends React.Component{
    render(){
        return (
            <div>
                <h1>Shopping List</h1>
                <SimpleList />
                <SimpleList />
                <SimpleList />
            </div>
        );
    }
}

export default App
```

Finally I use `ReactDOM.render` in my `index.js` file to render the `App` component.

Here is the `index.js` code:

```
import React from 'react';
import ReactDOM from 'react-dom';
import App from "./components/App.js"


ReactDOM.render(<App />, document.getElementById('root'));
```

You can check the source code out for this app here <https://github.com/masai-school/full-stack-dev/tree/master/course/week_7/day_1/session1/multiple_test>.

## Adding styles and CSS modules

It is commonplace in react to have a style-sheet for each component as this can help you retain a lot of modularity.

You can add styles in many ways, including including inline styles, style object literals.

Here we will be using CSS Modules which offer many advantages including local scoping and class composition.

Lets add some CSS to the `multiple_test` app.

For the `App` component, I make a new css file called `app.module.css` in my components folder.

Any new CSS modules must follow the syntax `<name>.module.css`.

Here is the code for `app.module.css`:

```
.header{
    color: blue;
    border: 1px groove black;
    background-color: lightgrey;
}
```

**Note:** Since this is not JSX you can use regular CSS syntax.

Now I have to import these styles from my `App` component.

Updated code in app component:

```
import React from 'react';
import SimpleList from './SimpleList.js'
import styles from './app.module.css'

class App extends React.Component{
    render(){
        return (
            <div>
                <h1 className = {styles.header} >Shopping List</h1>
                <SimpleList />
                <SimpleList />
            </div>
        );
    }
}

export default App
```

The only changes are `import styles from './app.module.css'` which imports the styles and `className = {styles.header}` which adds the header style to the `H1` tag.

Lets also add styles to the `SimpleList` component.

I create a file called `simpleList.module.css` and add the following css into it.

```
.list{
    font-family: monospace;
    font-size: 2em;
    margin: 2em;
    padding: 0;
    list-style-type: '> ';
}
```

Then I add a few lines of code to add the styles to my component.

```
import React from 'react';
import styles from './simpleList.module.css'

class SimpleList extends React.Component{
    render(){
        return (
            <ol className = {styles.list}>
                <li>Apple</li>
                <li>Banana</li>
                <li>Watermelon</li>
            </ol>
        );
    }
}

export default SimpleList
```

This is the basics of using CSS modules. For a deeper look visit <https://programmingwithmosh.com/react/css-modules-react/>

## Adding images

Adding images is very simple.

Any images you want to must be included in the `public` folder.

I have added an image called `computer.jpg`.

Now I can render it in the App component with an image tag.

```
<img src = "/computer.jpg" height = "50%" width = "50%" />
```

React automatically knows the image is in the public directory so you don't need to include the entire path.

The updated project with styles and the image can be found at <https://github.com/masai-school/full-stack-dev/tree/master/course/week_7/day_1/session1/multiple_test_styles>



# Week 7 - Day 4

## Introduction to ReactJS Part 4

## Stateful components

Lets get to learning something new.

The components we were making so far were called `stateless` components as they did not have any `state`.

But what is state? How do we use it? Where do we use it ? Why is it useful ?

These are important questions to consider so lets answer them by working through a few examples.

Consider the following stateless component:

```
class Profile extends React.Component{
  render(){
    return (
      <div>
        <h1>Profile</h1>
        <p>Name: Patrick</p>
        <p>Age: 21</p>
        <p>Gender: Male</p>
      </div>
    );
  }
}

ReactDOM.render(<Profile />, document.querySelector('#root'))
```

Now lets add state to it:

```
class Profile extends React.Component{
  constructor(props){
    super(props)
    
    this.state = {      //This is the state.
      name : "Patrick",
      age : 21,
      gender: "Male"
    }
  }
  render(){
    return (
      <div>
        <h1>Profile</h1>
        <p>Name: {this.state.name}</p>
        <p>Age: {this.state.age}</p>
        <p>Gender: {this.state.gender}</p>
      </div>
    );
  }
}

ReactDOM.render(<Profile />, document.querySelector('#root'))
```

Now we have a stateful component as it contains `this.state` in the constructor.

Codepen link <https://codepen.io/steviekong/pen/xvwgbv?editors=1010>.

Right now state seems to work just like props but state is very different from props.

Before we continue with state lets learn about event handlers.

## Handling events in React

You handle events in react much the same way as in regular javaScript.

```
class SimpleComponent extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      printValue : "clicked"
    }
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick() {
    console.log(this.state.printValue);
  }
  render(){
    return (
      <button onClick = {this.handleClick}>Click here to print to the console</button>
    );
  }
}

ReactDOM.render(<SimpleComponent />, document.querySelector('#root'))
```

CodePen Example: <https://codepen.io/steviekong/pen/PMPmPo?editors=1011>

When you look the code above an obvious question is why are we doing `this.handleClick = this.handleClick.bind(this);` ?

Remember that regular ES5 functions have their own `this`. So when we call `this.state` within that function, `this` will refer to the function itself.

So we use the `bind` function which allows us to change the `this` value of the given function. We change it to refer to the class `SimpleComponent`

You can read more about the `bind` function here <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind>.

If you are not a big fan of using `bind`, you can simply use arrow function which do not have a `this` value so you don't have to bind a new `this` value to it.

**Example with arrow functions:**

```
class SimpleComponent extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      printValue : "clicked"
    }
  }
  handleClick = () => {
    console.log(this.state.printValue);
  }
  render(){
    return (
      <button onClick = {this.handleClick}>Click here to print to the console</button>
    );
  }
}

ReactDOM.render(<SimpleComponent />, document.querySelector('#root'))
```

CodePen: <https://codepen.io/steviekong/pen/QejMEX>

**Using the Event Object:**

You can also use `event.target` property from functions called by events to extract values or other properties from elements.

**For example:**

<https://codepen.io/steviekong/pen/KOVBGx?editors=1010>

The above example really highlights the power of combining events and state. Without having to directly manipulate the DOM, we can instead focus on implementing the core of our application, rather than worrying about JavaScript bugs.

## Updating state

Now we know how to make a stateful component and add event listeners!

Lets combine both to update a components state!

We use the `this.setState` function to change the state of a component.

**Important:** Never directly modify the `this.state` object! This will not modify state or will produce errors!

Codepen Example: <https://codepen.io/steviekong/pen/OKyjvG?editors=1010>

Every time the button is clicked, the state is updated using the `setState` function.

**Some basic information about state:**

1. State can only be used within class components.(For the most part, we will come back to this later).
2. State is just an object literal but it has special meaning to the React.Component class.
3. When you call `setState` and change any state value, react will automatically re-render it.
4. Component state must be initialized when a component is created.

**Some advanced information about state:**

**1. State updates may be Asynchronous:**

For performance reasons React might batch multiple `setState()` calls into a single update.

Due to this, it may not be ideal to rely on the current value of `this.props` and `this.state` to calculate the next state of your component.

However to fix this, `setState()` can also accept a callback function as an argument in which we can pass the current state and props.

CodePen Example: <https://codepen.io/steviekong/pen/bXERGq?editors=1010>

**2. State Updates are merged**

When you update one state value, others remain the same. For example your state may contain several variables.

```
  constructor(props) {
    super(props);
    this.state = {
      counter : 0,
      names : ["masai" , "school"]
    };
  }
```

You can then update them independently:

Codepen Example: <https://codepen.io/steviekong/pen/GVoEqq?editors=1010>

For more on `setState` read the official docs <https://reactjs.org/docs/react-component.html#setstate>

**3. State flows down**

Parent and child components do not know whether if a certain component is stateful or not.

Unlike props, state is scoped locally which means it cannot be accessed by any other component.

***However, state can be passed as props from a parent component to its children.***

```
<Child name = {this.state.name} /> 
```

Here the `name` value from state is being passed down to a child component as props.

Within the context of a child component, it would not know where the props came from.

Moreover, any state updates from the parent will then also apply to the child who inherits that state.

## Some cool examples:

I encourage you to check out some amazing projects created with React here <https://reactjs.org/community/examples.html>





# Week 8 - Day 1

## Introduction to ReactJS Part 5

## LifeCycle of a Component

Any react component that extends `React.Component` almost like a living organism will go through the following phases in its lifetime:

1. Mounting
2. Updating
3. Unmounting

Lets go though each phase in-depth:

1. Mounting: This is the phase when a component is created and inserted into the DOM. When this happens the following methods are called in same order as below:
   - `constructor`: <https://reactjs.org/docs/react-component.html#constructor>
   - `getDerivedStateFromProps`: <https://reactjs.org/docs/react-component.html#static-getderivedstatefromprops>
   - `render`: <https://reactjs.org/docs/react-component.html#render>
   - `componentDidMount()`: This is a `lifecycle` method that is called right after a component is **mounted** or rendered. We can use this method to modify state right after a component is rendered to the DOM using `setState`. <https://reactjs.org/docs/react-component.html#componentdidmount>
2. Updating: After the react component has been mounted, it can then recieve new updates through new props being sent by parents or from updating the state. When this happens the following methods are called in the same order as below:
   - `static getDerivedStateFromProps()`: <https://reactjs.org/docs/react-component.html#static-getderivedstatefromprops>
   - `shouldComponentUpdate()`: <https://reactjs.org/docs/react-component.html#shouldcomponentupdate>
   - `render()`: This is the same render method as before.
   - `getSnapshotBeforeUpdate()`: <https://reactjs.org/docs/react-component.html#getsnapshotbeforeupdate>
   - `componentDidUpdate()`: This method is called right after a component updates. This method is usually used to perform DOM operations when a component has been updated. <https://reactjs.org/docs/react-component.html#componentdidupdate>
3. Unmounting: This is the pahse when a component is not needed anymore and has been unmounted from the DOM. It only contains one method:
   - `componentWillUnmount()`: This method is called right before a component is unmounted or destroyed. <https://reactjs.org/docs/react-component.html#componentwillunmount>

If that was too confusing, here is a simple graphic:

<http://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/>

While there are many lifecycle methods the most important one's you should be focusing on are:

- `constructor()`
- `render()`
- `componentDidMount()`
- `componentDidUpdate()`
- `componentWillUnmount()`

The rest are not as commonly used but can provide additional functionality when required.

Lets take a look at a simple example to see how these methods are executed during the lifecycle of a component:

**CodePen Link:** <https://codepen.io/steviekong/pen/LwbvoY?editors=0011>

Lets better understand these lifecycle methods by doing an example:

Remember in the first tutorial we made a `Clock` that called `ReactDOM.render` multiple times?

We are going to rewrite that code using the lifecycle methods we learned above.

**CodePen Link:** <https://codepen.io/steviekong/pen/wVoZJz?editors=1010>

## Conditional Rendering:

Often you will want to render components based on a condition. This can easily be done in react by using a conditional `if` within the render function.

**Example:**

<https://codepen.io/steviekong/pen/RXozRB?editors=1011>

You can also embed javascript expressions within JSX to perform conditional rendering.

**Example:** <https://codepen.io/gaearon/pen/ozJddz?editors=0010>

**Using the conditional(ternary) operator:**

The conditional operator is often used as a shorthand for the if statement.

<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator>

This can be really useful in react for in-line conditional rendering. Here is the login button example with the conditional operator.

**Example:** <https://codepen.io/steviekong/pen/MNbMPJ>

**Preventing components from rendering:**

Sometimes you may want to hide or delete components after rendering it.

To do this return `null` instead of any JSX in the render function.

**Example:**

<https://codepen.io/gaearon/pen/Xjoqwm?editors=0010>

## Using setInterval the right way using `componentWillUnmount`

An great use-case for `componentWillUnmount` is the following example.

Here's the right way to do this:

<https://codepen.io/peterbe/pen/LNxmRp?editors=0010>

Here's the wrong way to do this:

<https://codepen.io/peterbe/pen/VaPXNL?editors=1010>



# Week 8 - Day 3

## Introduction to ReactJS Part 6

## Handling lists/arrays in ReactJS

React makes it very easy to transform arrays into components.

Moreover JSX renders an array of components/elements just like any other element.

**Example:** <https://codepen.io/gaearon/pen/GjPyQr?editors=0011>

It is commonplace to pass arrays as props to a child element and use map to render the children.

You might have noticed a warming in the console, this is because we have not included keys.

## Importance of keys

React uses keys to identify elements. React needs to be aware of all elements that are added, removed or modified.

When you pass a list of elements is very important to give each element a **unique key**. You must do this manually.

This key **must not** be the index of the element.

**Example where elements values are used as keys:**

<https://codepen.io/gaearon/pen/jrXYRR?editors=0011>

Here is a great article on why index should not be used as the key <https://medium.com/@robinpokorny/index-as-a-key-is-an-anti-pattern-e0349aece318>.

If you want to know why react needs to use key read this <https://reactjs.org/docs/reconciliation.html#recursing-on-children>.

## Rules of keys

**Keys should be used with correct context:**

When rendering child elements, keys should be applied from the parent, not the child.

**Incorrect:**

```
function ListItem(props) {
  const value = props.value;
  return (
    // Wrong! There is no need to specify the key here:
    <li key={value.toString()}>
      {value}
    </li>
  );
}

function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) =>
    // Wrong! The key should have been specified here:
    <ListItem value={number} />
  );
  return (
    <ul>
      {listItems}
    </ul>
  );
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
  <NumberList numbers={numbers} />,
  document.getElementById('root')
);
```

**Correct:**

```
function ListItem(props) {
  // Correct! There is no need to specify the key here:
  return <li>{props.value}</li>;
}

function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) =>
    // Correct! Key should be specified inside the array.
    <ListItem key={number.toString()}
              value={number} />
  );
  return (
    <ul>
      {listItems}
    </ul>
  );
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
  <NumberList numbers={numbers} />,
  document.getElementById('root')
);
```

**CodePen:** <https://codepen.io/gaearon/pen/ZXeOGM?editors=0010>

**Keys only need to be unique among siblings:**

Key are just used by react to differentiate between siblings, therefore keys just need to be unique among siblings. They can be non-unique globally.

**CodePen:** <https://codepen.io/gaearon/pen/NRZYGN?editors=0010>

**Keys are not passed to components:**

Keys are not passed as props to your component, if you need to identify components you create, you can pass another prop with a different name but with the same keys.

**Example:**

```
const content = posts.map((post) =>
  <Post
    key={post.id}
    id={post.id}
    title={post.title} />
);
```

Here id is passed as a key and as a prop called `id`. They both use `post.id` but only `id` is available to the Post component as props.

### Embedding `map()` in to JSX

Since `map()` is a valid JavaScript expression you can also embed `map()` right into JSX.

**CodePen:** <https://codepen.io/steviekong/pen/YmNaGe?editors=0010>

## Communicating from child component to parent component

We have already learned how to share data and even `state` from parent to child component using `props`.

However it may often be useful to share state updates of child components with parent components.

This is especially useful when you have several components who need to reflect the same changing data.

**How do we do this?**

In short we pass functions as props.

For a longer answer read this <https://reactjs.org/docs/lifting-state-up.html>.

Lets take a look an a simple example to start out with:

In the example below the `SearchBar` calls a function when the form `onSubmit` event occurs.

The function it calls is passed as props from the parent Component.

**CodePen:** <https://codepen.io/steviekong/pen/VopopE?editors=0011>

You can even user this value to set state in the parent.

Here is a great example of setting state and passing values between sibling components <https://codepen.io/gaearon/pen/WZpxpz?editors=0010>.

Also read [Lifting State Up](https://reactjs.org/docs/lifting-state-up.html) from the official docs.



# Week 8 - Day 4

## Introduction to ReactJS Part 7

## Handling forms in React

React does not give you any special way to deal with forms. If you use a regular HTML form in react it will work just as intended.

**Example:**

```
<form>
  <label>
    Name:
    <input type="text" name="name" />
  </label>
  <input type="submit" value="Submit" />
</form>
```

**CodePen Link:** <https://codepen.io/steviekong/pen/YmZMqO?editors=0010>

However state of this form is now unknown to react and when users input any values or submit the form or any other such event, react is unaware.

Because of this, the above form is called an **uncontrolled** form.

**Controlled forms:**

While the above form works just fine, when we write react Apps, we will usually be doing something useful with the data we receive from forms. We may want to store it, send it to a server or API etc.

Thankfully, form elements such as `<input> <textarea> and <select>` maintain their own state.

We can combine the internal state of these elements and react state to ***control** the value of these elements.

Also, according to the React Docs "An input form element whose value is controlled by React in this way is called a “controlled component”."

**Codepen Example:** <https://codepen.io/steviekong/pen/jgBRQy?editors=0011>

Controlled forms are really useful for sanitizing or modifying data before sending to an API or a server.

For more on forms visit <https://reactjs.org/docs/forms.html>.

## Using NPM to import 3rd party packages and Styling

Till now we haven't really installed any NPM packages of our own.

We also haven't used any UI frameworks like Bootstrap that can reduce the number of components we need to built from scratch.

While we could use [reactstrap](https://reactstrap.github.io/) which gives us Bootstrap 4 components, I have chosen to go with [Material-UI](https://material-ui.com/) which is the most popular UI framework.

To install any packages from npm, just run the `npm install command`. You can see the documentation here <https://docs.npmjs.com/cli/install>.

## Installing Material UI and importing components.

You can find all the basic instructions on installing Material-UI here <https://material-ui.com/getting-started/installation/>.

1. To start out with go to your react application folder and run `npm install @material-ui/core`.
2. Also make sure to include font and icon links in your base `index.html` file.

This will ensure you have a consistent design language across your entire App.

Add the following lines to `index.html`:

```
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" />

<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons" />
```

1. We are just making basic template app so we can just keep all the javascript code in the App component.
2. Lets add a simple navigation bar to our app. First you must import the App bar component with an import statement `import AppBar from '@material-ui/core/AppBar`. `You also need to import a ToolBar with another import statement`import Toolbar from '@material-ui/core/Toolbar`.

Finally you can render both it within your App component.

Your App.js code should look like this:

```
import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';

class App extends React.Component{
    render(){
        return (
            <div>
                <AppBar>
                    <Toolbar>
                    </Toolbar>
                </AppBar>
            </div>
        );
    }
}
export default App
```

Lets also include a title and a menu button into the page.

We also want the material-ui icons package so run `npm install @material-ui/icons`.

Updated code:

```
import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Typography from '@material-ui/core/Typography';

class App extends React.Component{
    render(){
        return (
            <div>
                <AppBar>
                    <Toolbar>
                        <IconButton edge="start" color="inherit" aria-label="menu">
                            <MenuIcon />
                        </IconButton>
                        <Typography variant="h5">
                            Home
                        </Typography>
                    </Toolbar>
                </AppBar>
            </div>
        );
    }
}
export default App
```

You can check out the example here <https://github.com/masai-school/full-stack-dev/tree/master/course/week_8/day_4/material_test>

Material UI has many components but you can see all of them and any examples on <https://material-ui.com/components>.

The website has many examples for each component so using them in your projects should be easy.

## Other UI frameworks

Don't let me limit your options, there are many other popular UI frameworks for ReactJS and you are free to use any of them.

Here is a small list of great frameworks:

1. [Ant Design (Used by Alibaba, Baidu and many other Chinese Companies)](https://ant.design/)
2. [React Bootstrap (Bootstrap 3)](https://react-bootstrap.github.io/)
3. [React Strap (Bootstrap 4)](https://reactstrap.github.io/)
4. [React Virtualized (Great for handling a lot of Data)](https://bvaughn.github.io/react-virtualized/)

There are many others so feel free to search Google for a UI framework that you like and enjoy working with!

## Deploying a React App to Netlify

After making our apps look amazing we want to show it off to the world!

Lets host our React App using Netlify.

Follow these steps:

1. First go to <https://www.netlify.com/> and create an account using Github.
2. Next go to your React App folder in the command line and run the command `npm run build`. This will do all the work necessary to have your app ready for deployment.
3. Install the netlify CLI using `npm install netlify-cli -g`.
4. Now type `netlify deploy` and visit the link it provides to verify your account.
5. Once you are done verifying, it should give you some options, select `+ Create & configure a new site `.
6. Select a team, this would usually be the same as your Netlify-ID.
7. Then give your website some unique name.
8. In the deploy path option type `build`.
9. Your draft should be live on the `Live Draft URL:`. Visit the lin kand make sure your application is working correctly.
10. If you application is working, type `netlify deploy --prod` to deploy the application. The deploy path should be `build`.
11. Visit the live URL to see your website live on the Internet for anyone to visit.





# Week 8 Day 5

## Deep dive into JavaScript and Asynchronous Programming

## The Event loop and Concurrency Model:

Before we actually go over asynchronous programming lets go over some core JavaScript concepts first.

[![img](https://camo.githubusercontent.com/697b36e7ba71552e1014eefe08dba3bd158c2219/68747470733a2f2f6d646e2e6d6f7a696c6c6164656d6f732e6f72672f66696c65732f343631372f64656661756c742e737667)](https://camo.githubusercontent.com/697b36e7ba71552e1014eefe08dba3bd158c2219/68747470733a2f2f6d646e2e6d6f7a696c6c6164656d6f732e6f72672f66696c65732f343631372f64656661756c742e737667)

Source: MDN web docs 

https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop



### Stack

When you call a function in JavaScript all the instructions within that function get loaded into a Stack. Each function has a logical **frame** within the call Stack. Javascript then executes the instructions in each frame by popping them from the stack.

**Example From MDN:**

```
function foo(b) {
  var a = 10;
  return a + b + 11;
}

function bar(x) {
  var y = 3;
  return foo(x * y);
}

console.log(bar(7)); //returns 42
```

"When calling bar, a first frame is created containing bar's arguments and local variables. When bar calls foo, a second frame is created and pushed on top of the first one containing foo's arguments and local variables. When foo returns, the top frame element is popped out of the stack (leaving only bar's call frame). When bar returns, the stack is empty."

### Heap

On the other hand, objects in JavaScript are stored in what is called the **Heap**. This is an unstructured portion of memory which object data lives.

### Task/Message Queue

JavaScript also uses a data structure known as a Queue to store tasks/messages.

Tasks/messages are added to the queue anytime an event occurs and there is a listener attached to that event.

Functions like `setTimeout` and `setInterval` which accept callbacks also add tasks/messages to the queue.

### The Event loop

JavaScript has one thread called which runs a loop that looks for new messages/tasks on the message queue and pushes them onto the call stack to be executed.

**Think of it sort of like this:**

```
while (queue.waitForMessage()) {
  queue.processNextMessage();
}
```

However, the event loop gives priority to the frames currently on the call stack pushes a new message from the Queue onto the stack after all the frames in the stack have been executed and the call stack is empty.

**Run to completion:**

It is also important to note that each message on the queue is completely processed before another other message is processed.

[Great Talk on Event Loop](https://www.youtube.com/watch?v=8aGhZQkoFbQ)

[Call Stack and Queue Visualizer](https://github.com/masai-school/full-stack-dev/blob/master/course/week_08/day_5/latentflip.com/loupe)

### Synchronous Programming

Most programs you write often tend to be **synchronous**. This means that actions in code happen one at a time.

Take the function `sumUntil` that is given below. Any code that needs to run after line 2 can only run after `sumUntil` has finished all its work and returned some value.

```
let a = 10; //1
console.log(sumUntil(a), new Date().getTime()); //2
console.log("The function is done!", new Date().getTime());

function sumUntil(y){
    let arr = [];
    for(let i = 0; i < y; i++){
        for(let j = 0; j < y; j ++){
            arr.push([i, j])
        }
    }
    return arr;
}
```

This means that while waiting for that function to return its value the rest of your program is still waiting and not able to any useful work in the mean time.

This can be a huge problem with tasks that take a very long time or an **indeterminate** amount of time.

For example HTTP requests could take any amount of time to receive a response from the server. There is even a chance you won't even get a response!

However, you don't want your entire WebPage or Javascript program waiting for that request to complete. You still want users to be able to use your Application and perform I/O (input/output) actions!

Moreover, if you entire application must wait for this request it will freeze or hang, this is known as [blocking](<https://en.wikipedia.org/wiki/Blocking_(computing)> and is really undesirable. [![img](https://github.com/masai-school/full-stack-dev/raw/master/course/week_08/day_5/RTT.png)](https://github.com/masai-school/full-stack-dev/blob/master/course/week_08/day_5/RTT.png)

**Threads:**

A solution to this problem that is popular in many languages is using multiple **threads**.

Imagine thread as small part of your overall program that runs in parallel with your main program. For example a specific function could be run on a separate thread.

This means that while your main program is always ready for user inputs and other work, you threads can do other work like HTTP requests in the background.

Most browsers implement this using [Web Workers API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers). NodeJS also has a implementation with service workers.

However, multi-threaded applications can get really complex to understand and implement as a beginner programmer.

### Asynchronous Programming

[![img](https://camo.githubusercontent.com/f1e3a5099e93cad6911f086221e60eaf121c33fc/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f6d61782f3534302f312a745f6f4379484273744d6e463857705a3637704b54672e6a706567)](https://camo.githubusercontent.com/f1e3a5099e93cad6911f086221e60eaf121c33fc/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f6d61782f3534302f312a745f6f4379484273744d6e463857705a3637704b54672e6a706567)

Source : An Introduction to Asynchronous Programming in Python [

https://medium.com/velotio-perspectives/an-introduction-to-asynchronous-programming-in-python-af0189a88bbb](https://medium.com/velotio-perspectives/an-introduction-to-asynchronous-programming-in-python-af0189a88bbb)



The alternative to using threads that is heavily used in JavaScript is Asynchronous programming.

In asynchronous programming, the main thread, in our case the event loop finishes all its primary work without being blocked.

In synchronous programming is that easy task that is started must be completed before another task can start.

On the other hand, in asynchronous programming, many tasks can start before other tasks are completed and when each task is done, it notifies the main thread. The above diagram illustrates this well.

**Asynchronous Programming in JavaScript:**

We have already done lots of asynchronous programming in JavaScript using methods that accept callbacks.

Since callbacks are pushed to the callback queue rather than the call stack, they will only begin execution after all the frames in the callstack have completed execution.

**Example of Synchronous vs Asynchronous:**

**Synchronous:**

```
let j = 0; 
while(j < 3){
    console.log(j);
    j++;
}

let i = 0; 
while(i < 3){
    console.log(i);
    i++;
}

console.log("Welcome to Masai.");
```

**Asynchronous:**

```
setTimeout(function() {
    let j = 0; 
    while(j < 3){
        console.log(i);
        j++;
    }
}, 0)


let i = 0; 
while(i < 3){
    console.log(i);
    i++;
}

console.log("Welcome to Masai.");
```





# Week 8 Day 5

## Callback Hell

The most significant problem associated with callbacks is nesting multiple callbacks.

**Example:**

```
fs.readdir(source, function (err, files) {
  if (err) {
    console.log('Error finding files: ' + err)
  } else {
    files.forEach(function (filename, fileIndex) {
      console.log(filename)
      gm(source + filename).size(function (err, values) {
        if (err) {
          console.log('Error identifying file size: ' + err)
        } else {
          console.log(filename + ' : ' + values)
          aspect = (values.width / values.height)
          widths.forEach(function (width, widthIndex) {
            height = Math.round(width / aspect)
            console.log('resizing ' + filename + 'to ' + height + 'x' + height)
            this.resize(width, height).write(dest + 'w' + width + '_' + filename, function(err) {
              if (err) console.log('Error writing file: ' + err)
            })
          }.bind(this))
        }
      })
    })
  }
})
```

You can already see how complicated this can become. JavaScript programmers affectionately call this **callback hell**.

How do we fix this ?

## Promise API

ES6 introduced the promise API which simplified callbacks and error handling within callbacks.

It is used in many libraries where asynchronous coding is required.

**But what is a promise?**

A Promise is just an object which represents the eventual completion oe failure of an asynchronous operation.

For example, when you make a request to a server, it could be successful and return the value or unsuccessful and return an error. When can then use the result of the promise to preform different operations.

**Creating a promise**

Lets say you have a function called bonus that checks your monthly performance and your bosses mood.

If your performance was `>50` and your boss was `"Happy"` you get a `bonus = performance * 10`. Otherwise you get no bonus and a reason.

However in either case you are still promised a result.

```
const bonus = (performance, mood) => new Promise((resolve, reject) => {
    if(performance > 50 && mood === "Happy"){
        let totalBonus = performance * 10;
        resolve(totalBonus);
    }
    else{
        let reason;
        if(performance <= 50){
            reason = "Terrible performance";
        }
        else{
            reason = "Boss was in a bad mood!";
        }
        reject(reason);
    }
});
```

**Consuming promises:** Here we actually use the promise function we made and if the promise is successful or resolved `then` we do something useful with the result like printing it to the console or we `catch` the error and print the reason we didn't get the bonus.

```
const bonus = (performance, mood) => new Promise((resolve, reject) => {
    if(performance > 50 && mood === "Happy"){
        let totalBonus = performance * 10;
        resolve(totalBonus);
    }
    else{
        let reason;
        if(performance <= 50){
            reason = "Terrible performance";
        }
        else{
            reason = "Boss was in a bad mood!";
        }
        reject(reason);
    }
});

let performance = 100;
let bossMood = "Happy"

bonus(performance, bossMood)
.then((response) =>{
  console.log(`My bonus for this month was ${response}!`);
})
.catch((error) =>{
  console.log(error)
});
```

**Chaining Promises:**

Lets say you wanted to do something else if you got a bonus. For example you would want to add some of it to your bank account.

You can make another

```
const bonus = (performance, mood) => new Promise((resolve, reject) => {
    if(performance > 50 && mood === "Happy"){
        let totalBonus = performance * 10;
        resolve(totalBonus);
    }
    else{
        let reason;
        if(performance <= 50){
            reason = "Terrible performance";
        }
        else{
            reason = "Boss was in a bad mood!";
        }
        reject(reason);
    }
});

const addToBank = amount =>{
    return Promise.resolve(`You added ${amount} to your bank account`);
};

let performance = 100;
let bossMood = "Happy";

bonus(performance, bossMood)
.then((response) =>{
  console.log(`My bonus for this month was ${response}!`);
  return response;
})
.then(addToBank)
.then((response) =>{
  console.log(response)
})
.catch((error) =>{
  console.log(error);
});
```

You could chain multiple promises just like this!

There is a lot more to learn about the promise API which you can read about here <https://www.promisejs.org/>. This website is just about the promise API!

Also scan through the MDN docs <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise>

## Axios and making HTTP requests in ReactJS

Front end applications that don't communicate with server seems a bit redundant. So lets connect our React Apps to a server.

While we could use the good old `XMLHttpRequest`, its lack of inbuilt support for promises makes this a less than ideal option.

Another viable option is the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) introduced in ES6 and expanded in ES7.

However I have chosen to go with the [Axios](https://github.com/axios/axios) package because of its various advantages. If you want to know why I prefer Axios over Fetch, [this medium post](https://medium.com/@jeffrey.allen.lewis/http-requests-compared-why-axios-is-better-than-node-fetch-more-secure-can-handle-errors-better-39fde869a4a6) explains it perfectly.

**Installing Axios:**

```
npm install axios
```

**Writing your first request with Axios:**

I love weather API's for some reason so lets try and get the local weather using the [FCC weather API](https://fcc-weather-api.glitch.me/).

```
const axios = require('axios'); // This is an alternative to import statements, don't worry about it!

axios.get('https://fcc-weather-api.glitch.me/api/current?lat=35&lon=139')
    .then(response => console.log(response))
    .catch(err => console.log(err));
```

The most powerful part of Axios it the ability to pass request configuration through a JavaScript object literal.

```
const axios = require('axios'); 
const requestParam = {
        method: 'get',
        url: 'https://fcc-weather-api.glitch.me/api/current',
        params : {
            lat : 12.9716,
            lon : 77.5946
        }
}
axios(requestParam)
     .then(response => console.log(response))
     .catch(err => console.log(err));
```

### Using Axios with React

The ideal place to place a http request is usually in `componentDidMount()`.

This because all your components are already mounted into the DOM and are waiting to receive some data.

You could also do it in `componentDidUpdate()` after some user input.

But **beware** using `setState` within `componentDidUpdate()` could cause an infinite loop since it once again invokes `componentDidUpdate()`.

To prevent this, make sure you are passing different props like this:

```
componentDidUpdate(prevProps) {
  // Typical usage (don't forget to compare props):
  if (this.props.userID !== prevProps.userID) {
    this.fetchData(this.props.userID);
  }
}
```

My example weather app is located here <https://github.com/masai-school/full-stack-dev/tree/master/course/week_8/day_5/axios_weather>.





# Week 9 - Day 1

## Introduction to Routing with react

While writing real applications, you won't just be writing single page apps.

What I mean by this is that your application will have many different routes with different views.

A common example would be a social networking website where you will have different routes like:

- Login
- Register
- Profile
- UserName
- Feed
- Explore

While there are many routing solutions for a react application, the most popular is `React Router`.

Within React Router nearly everything is a component which is really great since this is core to the react philosophy.

React router also supports dynamic routing, we will talk about this great feature in a later class.

Lastly react router allows our application to only make the required DOM changes without having to reload the entire application when we switch to a new route.

Also take a look at the documentation <https://reacttraining.com/react-router/web/guides/quick-start>

## Writing our first React App with Routing

To add react router to any react app just install it with the following command

```
npm install react-router-dom
```

For this application we will implement 3 routes that you might encounter in any generic website:

1. Home
2. About
3. Contact

Each route will have it's own unique view.

For now, I will write app my code right into the App component:

**Index.js**:

```
import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';
import {BrowserRouter, Route} from 'react-router-dom';

ReactDOM.render(
    <BrowserRouter>
        <App />
    </BrowserRouter> 
    ,document.getElementById('root'));
```

**App.js**

```
import React from 'react';
import {Route} from 'react-router-dom';


const Home = () =>{
    return <div>This the home page!</div>
}

const About = () =>{
    return <div>This is the about page!</div>
}

const Contact = () =>{
    return <div>This is the contact page!</div>
}

export default class App extends React.Component {
    render(){
        return (
            <React.Fragment>
                    <Route path = "/" exact component = {Home} />
                    <Route path = "/about" component = {About} />
                    <Route path = "/contact" component = {Contact} />
            </React.Fragment>
        );
    }
} 
```

**Browser Router Component:**

The most important part of the above code is the `<BrowserRouter>` component we used.

You can see its documentation here <https://reacttraining.com/react-router/web/api/BrowserRouter>.

**What does it do ?**

This component is a container for your entire application. It creates a `history` object which keeps track of the current location of the page.

It also matches paths and updates the DOM with relevant components and JSX according to a given path.

You can ready more about the history object here <https://reacttraining.com/react-router/web/api/history>.

**Route Component:**

This is the most important component in React Router.

You can look at the documentation here <https://reacttraining.com/react-router/web/api/Route>

Its primary purpose is to match routing paths and render components based on the paths that are matched.

The `component` method or prop is used to signify which Components will be rendered by the `<Route>` component when a given path is matched.

## How route path matching works and the exact keyword.

Paths are matched starting from the first `/` character.

Paths continue to get matched based on keywords.

For example:

`/` : Will be matched by all routes by default. `/profile` : Will be matched by any routes containing `/` and then `profile`. So `/profile/user` will be matched and `/profile/user/masai` will also be matched.

**Exact Prop**

Setting the exact props in your route component means only routes containing that exact path will be matched.

Example:

```
<Route path="/one" component={About} />
```

The above will be matched by `/one` and `/one/two`

```
<Route exact path="/one" component={About} />
```

Will be matched by `/one` but will ***not*** be matched by `/one/two`.

### Using routes to create templates

We can take advantage of the above feature of routes dynamically render the Components we need and keep other elements of our page static.

Lets improve our website by adding a `h1` title to every route. You can simply do this by rendering it right into the App component!

**App.js**

```
export default class App extends React.Component {
    render(){
        return (
            <React.Fragment>
                    <h1> Masai School Blog </h1>      
                    <Route path = "/" exact component = {Home} />
                    <Route path = "/about" component = {About} />
                    <Route path = "/contact" component = {Contact} />
            </React.Fragment>
        );
    }
} 
```

We can also add subpaths within components.

Lets add a `/courses` routes and 2 subroutes `/courses/fullstack` and `courses/android`.

```
const CourseTemplate = () => {
    return (
        <React.Fragment>
            <h1> Courses </h1>
            <ol>
                <li> Full-Stack Development </li>
                <li> Android Development </li>
            </ol>
            <Route path = "/courses/fullstack" render = {() => <Course name = "fullstack" /> } />
            <Route path = "/courses/android" render = {() => <Course name = "android" /> } />
        </React.Fragment>
    );
}

const Course = (props) =>{
    if(props.name == "fullstack"){
        return(
            <React.Fragment>
                <h1> FullStack Development </h1>
                <h3> What you will learn: </h3>
                <ul>
                    <li> HTML </li>
                    <li> CSS  </li>
                    <li> JavaScript </li>
                </ul>
            </React.Fragment>
        );
    }
    if(props.name == "android"){
        return(
            <React.Fragment>
                <h1> Android Development </h1>
                <h3> What you will learn: </h3>
                <ul>
                    <li> Java </li>
                    <li> Kotlin </li>
                    <li> Android Studio </li>
                </ul>
            </React.Fragment>
        );
    }
}

export default class App extends React.Component {
    render(){
        return (
            <React.Fragment>
                    <h1> Masai School Blog </h1>      
                    <Route path = "/" exact component = {Home} />
                    <Route path = "/about" component = {About} />
                    <Route path = "/contact" component = {Contact} />
                    <Route path = "/courses" component = {CourseTemplate} />
            </React.Fragment>
        );
    }
} 
```

**Render prop:**

In the code above I used the render prop within `<Route path = "/courses/fullstack" render = {() => <Course name = "fullstack" /> } />`

You can read the documentation here <https://reacttraining.com/react-router/web/api/Route/render-func>.

This prop allows me to pass a function which returns a Component. The function then dynamically renders a component based on the `path`.

Moreover we can also pass props to the rendered component allowing us to perform some dynamic rendering.

You might ask why didn't we do this?

```
<Route path = "/courses/fullstack" component = {() => <Course name = "fullstack" /> } /> 
```

According to the docs this can have very negative performance implications:

> “When you use the component props, the router uses React.createElement to create a new React element from the given component. That means if you provide an inline function to the component attribute, you would create a new component every render. This results in the existing component unmounting and the new component mounting instead of just updating the existing component.”

### Links and why not to use anchor tags

Only thing missing from our App apart from some nice content is some navigation.

We have many routes in our applications so lets add some hyperlinks which can allow users to get around our application.

Your immediate thought might be use to a Anchor or `<a>` tag. This is a very bad idea in React Router.

Links from anchor tags cause the page to refresh. This means we lose useful data like the `history` object, `state` etc.

Moreover, this means that on every click, the entire Application will be re-rendered from scratch which can have negative performance implications. This is also counter to the very idea of react which is to make small changes to the DOM to improve overall performance.

**What is the solution?**

The `<Link>` component lets the user navigate the routes in our application without having to reload the page.

You can read the documentation here <https://reacttraining.com/react-router/web/api/Link>.

Lets add some navigation to the website an some links to the courses we made.

The final file should look like this:

```
import React from 'react';
import {Route} from 'react-router-dom';
import {Link} from 'react-router-dom';


const Home = () =>{
    return <div>This the home page!</div>
}

const About = () =>{
    return <div>This is the about page!</div>
}

const Contact = () =>{
    return <div>This is the contact page!</div>
}

const CourseTemplate = () => {
    return (
        <React.Fragment>
            <h1> Courses </h1>
            <ol>
                <li><Link to="/courses/fullstack">Full-Stack Development</Link></li>
                <li><Link to="/courses/android">Android Development</Link></li>
            </ol>
            <Route path = "/courses/fullstack" render = {() => <Course name = "fullstack" /> } />
            <Route path = "/courses/android" render = {() => <Course name = "android" /> } />
        </React.Fragment>
    );
}

const Course = (props) =>{
    if(props.name == "fullstack"){
        return(
            <React.Fragment>
                <h1> FullStack Development </h1>
                <h3> What you will learn: </h3>
                <ul>
                    <li> HTML </li>
                    <li> CSS  </li>
                    <li> JavaScript </li>
                </ul>
            </React.Fragment>
        );
    }
    if(props.name == "android"){
        return(
            <React.Fragment>
                <h1> Android Development </h1>
                <h3> What you will learn: </h3>
                <ul>
                    <li> Java </li>
                    <li> Kotlin </li>
                    <li> Android Studio </li>
                </ul>
            </React.Fragment>
        );
    }
}

export default class App extends React.Component {
    render(){
        return (
            <React.Fragment>
                    <h1> Masai School Blog </h1>
                    <div>
                        <Link to="/">Home</Link><br />
                        <Link to="/about">About</Link><br />
                        <Link to="/contact">Contact</Link><br />
                        <Link to="/courses">Courses</Link><br />
                    </div>  
                    <Route path = "/" exact component = {Home} />
                    <Route path = "/about" component = {About} />
                    <Route path = "/contact" component = {Contact} />
                    <Route path = "/courses" component = {CourseTemplate} />
            </React.Fragment>
        );
    }
} 
```

You can find the example project here <https://github.com/masai-school/full-stack-dev/tree/master/course/week_9/day_1/router_example>

Note:** I wrote all my components in a single file. I **do not** recommend doing this. I did this so you could easily understand this tutorial. Please only have related components in the same file!



# Week 9 Day 2

## Introduction to Routing with React II

### The `match` object

This object contains useful information about the `<Route path>` matched from the URL.

You can read about it here <https://reacttraining.com/react-router/web/api/match>.

The properties I want you to take notice of are:

1. `params` : These are key/value pairs you can pass into the URL.
2. `path` : This returns the matched path string. We can use this to build nested `<Route>.`s.
3. `url` : This returns the matched portion of the URL. We can use this to build nested `<Link>`s.

Lets modify yesterday code with the match object.

I am going to modify the subpaths, `/courses/fullstack` and `/courses/android`using `match.path`.

I am also going to modify the links which open the above subpaths using `match.url`.

**App.js**

```
const CourseTemplate = ({match}) => {
    return (
        <React.Fragment>
            <h1> Courses </h1>
            <ol>
                <li><Link to={`${match.url}/fullstack`}>Full-Stack Development</Link></li>
                <li><Link to={`${match.url}/android`}>Android Development</Link></li>
            </ol>
            <Route path = {`${match.path}/fullstack`} render = {() => <Course name = "fullstack" /> } />
            <Route path = {`${match.path}/android`} render = {() => <Course name = "android" /> } />
        </React.Fragment>
    );
}

const Course = (props) =>{
    if(props.name == "fullstack"){
        return(
            <React.Fragment>
                <h1> FullStack Development </h1>
                <h3> What you will learn: </h3>
                <ul>
                    <li> HTML </li>
                    <li> CSS  </li>
                    <li> JavaScript </li>
                </ul>
            </React.Fragment>
        );
    }
    if(props.name == "android"){
        return(
            <React.Fragment>
                <h1> Android Development </h1>
                <h3> What you will learn: </h3>
                <ul>
                    <li> Java </li>
                    <li> Kotlin </li>
                    <li> Android Studio </li>
                </ul>
            </React.Fragment>
        );
    }
}

export default class App extends React.Component {
    render(){
        return (
            <React.Fragment>
                    <h1> Masai School Blog </h1>
                    <div>
                        <Link to="/">Home</Link><br />
                        <Link to="/about">About</Link><br />
                        <Link to="/contact">Contact</Link><br />
                        <Link to="/courses">Courses</Link><br />
                    </div>  
                    <Route path = "/" exact component = {Home} />
                    <Route path = "/about" component = {About} />
                    <Route path = "/contact" component = {Contact} />
                    <Route path = "/courses" component = {CourseTemplate} />
            </React.Fragment>
        );
    }
} 
```

### Dynamic Routing using the `match` object

Till now we have been **hard-coding** routes. But often in large Web Applications you will want to be generating routes dynamically.

For example lets say our website has some products. These products may have individual pages.

While the template and the HTML for the products might be the same, the data and assets(images etc.) to be displayed for each product will be different.

Each product should also have a unique route/path so users can share the URL to a particular product or even access it at a later time.

Moreover in larger websites we may be adding new products at any given time and our website must scale accordingly.

**Adding Dynamic Routing to our Application:**

I am going to add a route called `/products` in the App component. Which will generate a bunch of components containing products from a object literal I defined.

Each of these products will have click able links which leads to a Product page for any given product.

In a real Application the product data could come from an external API.

```
const productArr = [
        {
            name : "SmartPhone",
            price: 30,
            id : 0
        },
        {
            name : "Watch",
            price : 20,
            id : 1
        },
        {
            name : "Shirt",
            price : 50,
            id : 2
        },
        {
            name : "Pants",
            price : 100,
            id : 3
        }
]

const AllProducts = (props) =>{
    return (
        <React.Fragment>
            <h2> Products </h2>
            <div style = {{border : "1px solid black"}}>
                {props.productArr.map(element =>{
                    return (
                        <div key = {element.id} style = {{border : "1px solid black"}}>
                            <p> Name : {element.name} </p>
                            <Link to = {`${props.match.url}/${element.id}`}> Click to see the product </Link>
                        </div>
                    );
                })}
            </div>
        </React.Fragment>
    );
}

const Product = (props) =>{
    console.log(props)
    const productObj = productArr.find((element) => element.id == props.match.params.id) //This line makes sure that products are only displayed if they are found!
    if(productObj){
        return(
            <React.Fragment>
                <div style = {{border : "1px solid black"}}>
                    <p> Name : {productObj.name} </p>
                    <p> Price : {productObj.price} </p>
                </div> 
            </React.Fragment>
        )
    }
    else{
        return(
            <React.Fragment>
                <h1> Product not found, invalid id </h1>
            </React.Fragment>
        );
    }
}

export default class App extends React.Component {
    render(){
        return (
            <React.Fragment>
                    <h1> Masai School Blog </h1>
                    <div>
                        <Link to="/">Home</Link><br />
                        <Link to="/about">About</Link><br />
                        <Link to="/contact">Contact</Link><br />
                        <Link to="/courses">Courses</Link><br />
                        <Link to="/products">Products</Link>
                    </div>  
                    <Route path = "/" exact component = {Home} />
                    <Route path = "/about" component = {About} />
                    <Route path = "/contact" component = {Contact} />
                    <Route path = "/courses" component = {CourseTemplate} />
                    <Route path = "/products" exact render = {props => <AllProducts productArr = {productArr} {...props} /> }/>
                    <Route path = "/products/:id" render = {props => <Product {...props} />} />
            </React.Fragment>
        );
    }
} 
```

## Switch component

The `<Switch>` component renders the first `<Route>` that matches the route path.

The is really useful when you have several paths and you want to render the first match. Moreover if there are no matches you can even render an error page.

You can read the documentation here <https://reacttraining.com/react-router/web/api/Switch>

Lets add a Switch component to the App component.

```
export default class App extends React.Component {
    render(){
        return (
            <React.Fragment>
                    <h1> Masai School Blog </h1>
                    <div>
                        <Link to="/">Home</Link><br />
                        <Link to="/about">About</Link><br />
                        <Link to="/contact">Contact</Link><br />
                        <Link to="/courses">Courses</Link><br />
                        <Link to="/products">Products</Link>
                    </div> 
                    <Switch>
                        <Route path = "/" exact component = {Home} />
                        <Route path = "/about" component = {About} />
                        <Route path = "/contact" component = {Contact} />
                        <Route path = "/courses" component = {CourseTemplate} />
                        <Route path = "/products" exact render = {props => <AllProducts productArr = {productArr} {...props} /> }/>
                        <Route path = "/products/:id" render = {props => <Product {...props} />} />
                    </Switch>
            </React.Fragment>
        );
    }
} 
```

## No match

Till now we have seen paths that match. But what if our users go to a path that does not match ?

Right now any non-matching path will be returned the basic `index.html` file we have within our public folder.

However what we really need to match any such path and return an error or 404 not found page.

We can easily add a component called `NotFound` which will render for any invalid route.

```
<Switch>
    <Route path = "/" exact component = {Home} />
    <Route path = "/about" component = {About} />
    <Route path = "/contact" component = {Contact} />
    <Route path = "/courses" component = {CourseTemplate} />
    <Route path = "/products" exact render = {props => <AllProducts productArr = {productArr} {...props} /> }/>
    <Route path = "/products/:id" render = {props => <Product {...props} />} />
    <Route component = {NotFound} />
</Switch>
```

You can see the example from class here <https://github.com/masai-school/full-stack-dev/tree/master/course/week_9/day_2/router_example_day_2>





# Week 9 Day 3

## Introduction to Routing with React III

### Authentication and Redirect

While the front end is not used for authentication we might still want some routes to be protected.

If a user visits once of these routes, they should be redirected to the login page or the home page, if they are not authenticated.

To do this we can use the `<Redirect>` component from react router.

You can read the documentaiton here <https://reacttraining.com/react-router/web/api/Redirect>

To start out with lets create a `<Login>` component and a `/admin` route.

If the user is not logged in, they will be redirected to the login page. If the are logged in, they can access the admin page.

First lets create a `fakeAuth` object literal which will tell the application is a user is logged in or not. In a real application this information would be coming from the backend API.

**Do not use this kind of function/login for security in a production environment!**

```
const fakeAuth = {
  isAuthenticated: false,
  authenticate(cb) {
    this.isAuthenticated = true;
    setTimeout(cb, 100); // fake async
  },
  signout(cb) {
    this.isAuthenticated = false;
    setTimeout(cb, 100);
  }
};
```

Next we can make components for `Admin` and `Login`.

```
const Admin = (props) => {
    return (
        <React.Fragment>
            <h1> This is the admin page with some confedential information </h1>
            <p> Number of sales : 2 </p>
            <p> Number of users : 100 </p>
            <button onClick = {() => fakeAuth.signout()} > Sign Out </button>
        </React.Fragment>
    );
}

const Login = (props) =>{
    return (
        <React.Fragment>
            <h1> This is the login page </h1>
            <button onClick = {() => fakeAuth.authenticate()} > Sign In </button>
        </React.Fragment>
    );
}
```

Finally in the App component we can write the logic for the sign in and sign out.

```
<Route path = "/admin" render = {props =>{
                        return fakeAuth.isAuthenticated ? 
                            <Admin {...props} /> :
                            <Redirect to = {{pathname : "/login", state: {from :props.location}}} />
                    }} />
                    <Route path = "/login" component = {Login} />
```

### Using Regular Expressions for dynamic routing

The `path` property of the `<Route>` component can accept regular expressions for dynamic routing.

For this tutroial we will not be diving deep into Regular Expressions or regex. However, if you are curious and want to learn more <https://regexone.com/> provides a great tutorial on this subject.

For example lets say we have an array of items that are sold on our website, users may want to order these items by price, color etc.

We can assign dynamic routes for each of these in a single line and render components accordingly.

In our application we might want to order the products within the `/products` route by both ascending and descending price.

An easy way to do this might be a `/products/asc` route and a `/products/desc` route. This is fine for 2 different routes but often we must have many more routes which makes our code needlessly complicated.

Instead we can modify the existing `/products` route with a Regular Expression.

```
<Route path = "/products/:orderBy(asc|desc)" component = {Products} />
```

We also have to modify the `AllProducts` component to account for this change.

```
const AllProducts = (props) =>{
    let arr = [...props.productArr];
    if(props.match.params.order == "asc"){
        arr.sort((a, b) => a.price - b.price);
    }
    else if(props.match.params.order == "desc"){
        arr.sort((a, b) => b.price - a.price);
    }
    return (
        <React.Fragment>
            <h2> Products </h2>
            {props.match.params.order == "asc" ?
                <Link to = "desc"> Order By Descending Price</Link>:
                <Link to = "asc"> Order By Ascending Price</Link>
            }
            <div style = {{border : "1px solid black"}}>
                {arr.map(element =>{
                    return (
                        <div key = {element.id} style = {{border : "1px solid black"}}>
                            <p> Name : {element.name} </p>
                            <p> Price : {element.price} </p>
                            <Link to = {`product/${element.id}`}>Click to see product </Link>
                        </div>
                    );
                })}
            </div>
        </React.Fragment>
    );
}
```

Now users can easily order by price, either ascending or descending. The default value is left as ascending.



# Week 10 Day 1

### Introduction to Redux

**What is redux?**

Redux is a predictable state container for ***any*** JavaScript application. For our purpose we are going to use Redux to manage a React Application.

However, Redux has nothing to do with React JS, you can write applications that use Redux in plain JavaScript and direct DOM updates. Redux can also be used with any Front End or Backend framework like AngularJS, EmberJS, VueJS etc.

**Why should my application use Redux?**

You may have noticed that writing large applications in plain react, handling state can become needlessly complicated.

Take the example of a simple todo App:

[![img](https://github.com/masai-school/full-stack-dev/raw/master/course/week_10/day_1/todo.png)](https://github.com/masai-school/full-stack-dev/blob/master/course/week_10/day_1/todo.png)

Now lets look at the flow of data in the todo App:

[![img](https://github.com/masai-school/full-stack-dev/raw/master/course/week_10/day_1/todo_data.png)](https://github.com/masai-school/full-stack-dev/blob/master/course/week_10/day_1/todo_data.png)

We can already see that managing state is already getting very complicated. Even though we are working with a very small number of components that need to get updated.

The problem is compounded by the fact that in order to pass state updates from a child component to a parent component or from a component to its sibling, you must pass it through a callback to a parent.

Redux simplifies this entire spiderweb of passing state across your application.

## Core parts of Redux

We will learn Redux by creating a simple counter application, first without react. Tomorrow we will tackle react + redux applications.

1. To start, create a react app and delete all the files from the src folder.
2. Create a file called index.js.
3. Type `npm install redux` to install redux.

### The Redux Store

The solution to this is a single place to store and retrieve your applications state/data. Redux offers this in a place called the "store".

[![img](https://github.com/masai-school/full-stack-dev/raw/master/course/week_10/day_1/Redux_Todo.png)](https://github.com/masai-school/full-stack-dev/blob/master/course/week_10/day_1/Redux_Todo.png)

Documentation <https://redux.js.org/api/store>

Lets create a store in our index.js

```
import { createStore } from 'redux'

const store  = createStore();
```

### Redux Actions and Action creators

Actions are used to send data from your App to the store, this is the only way for your app to send and receive data/modify state from the store.

Actions are sent to the store via `store.dispatch()` function. Don't worry about this right now.

Actions are just regular JavaScript Object literals.

However, every action **must** have a `type` property which describes the action that is being performed.

The value of `type` is string and it is usually declared as a constant as it should never be modified.

Lets create simple actions for our counter application.

To start out with make a JavaScript file called `action.js` and write the code below there.

```
const INC_COUNTER = "INC_COUNTER"; // This is the type of the action

const action = {
	type : INC_COUNTER
}
```

**Action Creator:**

While declaring static actions could be fine, to send dynamic actions to the store you have to declare a **action creator**.

An action creator is just a function that returns an action.

In our code lets substitute the `const action` with an action creator function.

Our action creator will increment by the input argument `amount`.

I will also add a `DEC_COUNTER` action which should decrement our counter.

```
const INC_COUNTER = "INC_COUNTER"; // This is the type of the action

const DEC_COUNTER = "DEC_COUNTER";

const incrementCounter = (amount) =>{
	return {
		type : INC_COUNTER,
		amount
	}
}

const decrementCounter = (amount) =>{
	return {
		type : DEC_COUNTER,
		amount
	}
}
```

### Reducers

We have created actions but these don't do anything yet. **Reducers** are functions that specify how state changes in response to actions that are sent to the store.

From the react docs, "Remember that actions only describe what happened, but don't describe how the application's state changes."

This means actions don't do much else other than telling the store that we want to perform some change. Reducers actually implement the logic behind the actions.

Reducers also store the initial state of your application.

To start out make file called reducer.js .

First we are going to write the initial state object literal.

```
const initialState = {
    count : 0
}
```

Next we are going to add an export the reducer function.

```
const INC_COUNTER = "INC_COUNTER"; // This is the type of the action

const DEC_COUNTER = "DEC_COUNTER"; // This is the type of the action


const initialState = {
    count : 0
}

const counter = (state = initialState, action) =>{
    switch(action.type){
        case INC_COUNTER:
            return {
                count : state.count  + action.amount
            }
        case DEC_COUNTER:
            return {
                count : state.count - action.amount
            }
        default : 
            return state
    }
}

export default counter; 
```

Our reducer is unaware of the action it may be receiving, it may receive 2 or more different types of actions and must handle them appropriator.

It is very common in Redux to use a switch statement to check the action type and return the new state accordingly.

Again an important reminder that we are not directly modifying state, rather we are just returning `state+action.amount`

## Using store functions

A Redux store has 3 main functions:

1. `getState()` which returns the current state tree of the application.
2. `dispatch(action)` which allows us to update state via actions.
3. `subscribe(listener)` which allows us register listener functions. The subscribed listener function is called any time an action modifies the state.

You the `subcribe()` function also returns a function which you can call later to unregister the listener.

Think of the subscriber function kind of like `addEventListener` and `removeEventListener`.

You can read about all 3 [here](https://redux.js.org/api/store#store).

Lets use these functions in our `index.js` file to get, modify and print the state to the browser console.

```
import { createStore } from 'redux';
import counter from './reducer';
import {incrementCounter, decrementCounter} from "./actions";

const store  = createStore(counter);

console.log(store.getState()); // Log the initial state

// This subscriber that logs the state to the console every time state changes
// The subsribe() function returns an function to also unsubscribe or unregister the listener

const logState = () =>{
    console.log(store.getState());
}

const unsubscribe = store.subscribe(logState);

//Here we dispatch actions to the store

//Here we use actions created by the action producers

store.dispatch(incrementCounter(10));
store.dispatch(incrementCounter(20));
store.dispatch(decrementCounter(5));
store.dispatch(decrementCounter(20));

//However we can also create actions manually since actions are just object literals
store.dispatch({
    type : "INC_COUNTER",
    amount : 100
});

unsubscribe() // Now we can stop listening for state updates 
```

You can see the code for this counter project here <https://github.com/masai-school/full-stack-dev/tree/master/course/week_10/day_1/redux_counter>

## A visual representation of the Redux lifecycle:

If all of that was too confusing, this amazing GIF explains it better.

[![img](https://github.com/masai-school/full-stack-dev/raw/master/course/week_10/day_1/redux_basic.gif)](https://github.com/masai-school/full-stack-dev/blob/master/course/week_10/day_1/redux_basic.gif)

Source : <https://github.com/reduxjs/redux/issues/653>

## The three core principles of Redux

**Single Source of Truth:**

The store in redux is known as the single source of truth. This is because there is only one store in redux and it holds all the application state. Any state that need to be read in redux can only be done from the store.

**State is READ only**

You cannot modify state directly in Redux like you do within a React application using `setState()`.

According to the Redux Docs, "The only way to change the state is to emit an action, an object describing what happened."

Only modify state in Redux using actions and reducers!

**Changes in Redux are made with pure functions:**

Pure functions are functions that **do not** modify their arguments. Instead they create copies of the arguments and modify and change those copies to be returned later.

Moreover for any given input, pure functions will always return the same value.



# Week 10 Day 2

## Integrating Redux to React and React-Redux

Yesterday we made a simple counter application whose state was stored with Redux.

Now we need to add some react components who's state is controlled through Redux.

First install the **React-Redux** package with the command `npm install react-redux`.

You can see the documentation for the above library here [https://react-redux.js.org](https://react-redux.js.org/).

### The provider component

First we need to link our redux store with the react app.

React-Redux gives us a `<Provider>` component that makes our store available to any components nested below it.

We can add the provider to the `index.js` file by rendering it as a parent of our `<App>` component.

We also have to pass the store as props to the provider.

```
index.js
import { createStore } from 'redux';
import counter from './reducer';
import {incrementCounter, decrementCounter} from "./actions";

import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App'

import { Provider } from 'react-redux'; // Here we import the provider component

const store  = createStore(counter);

ReactDOM.render(
    <Provider store = {store} > // The provider is rendered first with the store passed as a prop
        <App /> //App is a child of the provider component
    </Provider>,
    document.getElementById('root')
);
```

Next we need to write the code for our `<App>` component and its children, `<Display>`, and `<CounterInput>`.

Display will display the current value of the counter and CounterInput will render 2 buttons and an input box which can be used to increment and decrement the counter.

Code for `App.js`:

```
import React from 'react';
import Display from './Display';
import CounterInput from './CounterInput'

export default class App extends React.Component{
    render(){
        return(
            <React.Fragment>
                <h1> Counter Application with React and Redux </h1> 
                <Display/>
                <CounterInput/>
            </React.Fragment>
        );
    }
}
```

Code for `Display.js`:

```
import React from 'react';

export default class Display extends React.Component{
    render(){
        return(
            <p> Counter : </p>
        );
    }
}
```

Code for `CounterInput.js`:

```
import React from 'react';

export default class CounterInput extends React.Component{
    render(){
        return(
            <span>
                <label htmlFor = "amount"> Amount: </label>
                <input type = "text" /> 

                <button> Increment </button>
                <button> Decrement </button>
            </span>
        );
    }
}
```

### Using the connect function

Now we have a some components rendered to the DOM but they don't do anything.

First we need to display the default `state.counter` in the display component.

To get the state from Redux we need to use the `connect` function from React-Redux to connect our component to the store.

You can read the documentation for the connect function here <https://react-redux.js.org/api/connect>.

Lets connect the display to the store:

Display.js

```
import React from 'react';
import {connect} from 'react-redux';

class Display extends React.Component{
    render(){
        return(
            <p> Counter : </p>
        );
    }
}


export default connect()(Display)
```

Notice how we export the connect function not the Display component directly.

### Extracting state data with the `mapStateToProps` function

Now to get the state we need to request the data that we need from the store.

We can request this data though the `mapStateToProps` function.

You can read the documentation here <https://react-redux.js.org/using-react-redux/connect-mapstate>

The `mapStateToProps` function can be named anything really but we name it mapStateToProps by convention.

The function must return an object literal which contains the data that we want to use from the Redux state. The `mapStateToProps` does what it says really, it maps the Redux State to a components props.

Display.js

```
import React from 'react';
import {connect} from 'react-redux';

class Display extends React.Component{
    render(){
        return(
            <p> Counter : {this.props.count} </p>
        );
    }
}

const mapStateToProps = state =>{
    return {
        count : state.count
    }
}


export default connect(mapStateToProps)(Display);
```

Finally we also render the state from the Display component as `this.props.count`.

**Important:** Whenever any state update occurs, the `mapStateToProps` will be called to fetch the new state.

## Dispatching actions using `mapDispatchToProps`

Next we need to be able to use the actions we defined in the `<CounterInput>` component.

First we import the actions from `actions.js`. Next we define a object literal that contains all of our actions. You could call it whatever you wanted, the documentation suggests calling it `actionCreators` or `mapDispatchToProps`.

You can read about `mapDispatchToProps` here <https://react-redux.js.org/using-react-redux/connect-mapdispatch#defining-mapdispatchtoprops-as-an-object>.

After we define the actions in a object, we can then pass it to the connect function as the second argument.

Finally we can dispatch these actions from buttons within our component when an `onClick` event occurs.

CounterInput.js:

```
import React from 'react';
import {incrementCounter, decrementCounter} from '../actions';
import {connect} from 'react-redux';

class CounterInput extends React.Component{
    render(){
        return(
            <span>
                <label htmlFor = "amount"> Amount: </label>
                <input type = "text" /> 

                <button onClick = {() => this.props.incrementCounter(5)}> Increment </button>
                <button onClick = {() => this.props.decrementCounter(5)}> Decrement </button>
            </span>
        );
    }
}

const actionCreators = {
    incrementCounter,
    decrementCounter
}

export default  connect(null, actionCreators)(CounterInput)
```

## Using local state along with redux

You may have noticed that in the above code, we called `incrementCounter(5)` and `decrementCounter(5)`.

However, what we really want do is to increment and decrement based on the input number.

To do this, we need a controlled input. The question now becomes, **where do i put the input box state?**

The answer is within the `CounterInput` component itself! If state does not need to be shared between components, it does not need to be in Redux.

Moreover, it is recommended you store any state/data that is not shared between components locally.

Now lets update the component with local state.

CounterInput.js:

```
import React from 'react';
import {incrementCounter, decrementCounter} from '../actions';
import {connect} from 'react-redux';

class CounterInput extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            input : ""
        }
    }
    render(){
        return(
            <span>
                <label htmlFor = "amount"> Amount: </label>
                <input type = "text" value = {this.state.input} onChange = {(e) => {
                    this.setState({
                        input : e.target.value
                    });
                }} /> 

                <button onClick = {() => this.props.incrementCounter(Number(this.state.input))}> Increment </button>
                <button onClick = {() => this.props.decrementCounter(Number(this.state.input))}> Decrement </button>
            </span>
        );
    }
}

const actionCreators = {
    incrementCounter,
    decrementCounter
}

export default  connect(null, actionCreators)(CounterInput) 
```

You can see the entire example project here <https://github.com/masai-school/full-stack-dev/tree/master/course/week_10/day_2/redux_counter_d2>