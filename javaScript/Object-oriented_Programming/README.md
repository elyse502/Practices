# Object-oriented Programming 💻
**Object-oriented Programming** is a programming `paradigm` centered around `objects` rather than functions. **OOP** is `not` a programming language or tool!, it's a style of programming or a programming `paradigm`. There are several `programming languages` out there that support **object-oriented programming** such as **c-sharp**, **Java**, **Ruby**, **Python**, **JavaScript** and more....

`JavaScript` is a little bit controversial!. It may interest you to know that many of the popular `frameworks` out there that you might be using are actually designed with **Object-oriented Programming** concepts in mind. `Angular` is an example of these `frameworks`. So **`Object-oriented Programming`** is a popular style of programming and it comes up in many technical **interviews**, so if you really want to be a `serious developer` you need to understand **`Object-oriented Programming`**. 

## 4 pillars(Core Concepts) of `Object-oriented Programming` 🏗️
* `Encapsulation`
* `Abstraction`
* `Inheritance`
* `Polymorphism`

### Let's look at each of these concepts:
Before **Object-oriented Programming** we had `Procedure Programming` that divided a program into a set of **functions**, so we have `data` stores in a bunch of `variables` and `functions` that operate on the data. This `style` of **programming** is very simple and straightforward, often it's what you learn as part of your first **programming subject** at a `university` but as your programs grow it will end up with a bunch of **functions** that are all over the place, you might find yourself **copying** and **pasting** lines of code over and over, you make a change to one function and then a several other **functions** break. That's what we call _`spaghetti code`_, there's so much **interdependence** btwn all these `functions`, it becomes problematic. **Object-oriented Programming** came to solve this **problem**, `object-oriented Programming` we combine a **group** of related `variables` and `functions` into a **`unit`**, we call that `unit` an _**`object`**_. We refer to these `variables` as **`properties`** and the `functions` as **`methods`**.

Here's is an _**example**_:

Think of a `car`, a **car** is an object with **`properties`** such as `make, model` and `color` and **`methods`** like `start(), stop()` and `move()`. Now you might say what we don't have `cars` in our `programs`, give me a real programming `example`. Okay think of _**`local storage object`**_ in your `browser's`, every `browser` has a `local storage object` that allows you to store `data locally`. This **local storage object** has a `property` like `length` which returns the number of `objects` in the storage and `methods` like `set item` and `remove item`.

### 1. Encapsulation
So in **`Object-oriented Programming`** we group related `variables` and `functions` that operate on them into _**`objects`**_, and this is what we call `encapsulation`. Let me show you an `example` of this in action:

```javascript

let baseSalary = 30_000;
let overtime = 10;
let rate = 20;

function getWage(baseSalary, overtime, rate) {
  return baseSalary + (overtime * rate);
}

```
So here we have 3 `variables:` `baseSalary`, `overtime` and `rate` below these we have a `function` to calculate the `wage` for **an employee**. We refer to this kind of implementation as _**`procedural`**_, so we have `variables` on one side and `functions` on the other side, they're hard decoupled. Now let's take a look at the **object-oriented** way to solve this `problem` above:

```javascript

let baseSalary = 30_000;
let overtime = 10;
let rate = 20;

function getWage(baseSalary, overtime, rate) {
  return baseSalary + (overtime * rate);
}

let employee = {
  baseSalary = 30_000,
  overtime = 10,
  rate = 20,
  getWage: function() {
    return this.baseSalary + (this.overtime * this.rate);
  }
};
employee.getWage();

```
We can have an `employee object` with 3 **`properties:`** `baseSalary`, `overtime` and `rate` and a **`method`** called `getWage`, now why is this better? well first of all look at the `getWage function`, this `function` has no `parameters`. In contrast in a _**`procedural example`**_ our `getWage function` has 3 `parameters`, the reason in the other **implementation** we don't have any parameters is because all those parameters(`baseSalary`, `overtime` and `rate`) are actually modeled as `properties` of that **object(`employee`)**. All those `properties` and `getWage function` they are highly related, so they are part of one _**`unit`**_. So one of the `symptons` of the **procedure** code is `functions` with so many `parameters`, when you write **code** in **`object-oriented`** way your `functions` end up having fewer and fewer `parameters`. As **`Uncle Bob`** says "the best `functions` are those with no `parameters`", The **fewer** the number of `parameters` the **easier** it is to use and maintain that `function`. So that's **`Encapsulation`**, now let's look at **`Abstraction:`**

### 2. Abstraction














