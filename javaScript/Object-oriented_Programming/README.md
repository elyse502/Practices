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

![Screenshot 2024-04-29 113612](https://github.com/elyse502/Practices/assets/125453474/82c44f33-9511-44f1-a05c-58965f14d381) ![Screenshot 2024-04-29 113739](https://github.com/elyse502/Practices/assets/125453474/e5d53c1f-bf16-4823-8bd5-14cad979cfce)

**Object-oriented Programming**

![Screenshot 2024-04-29 113917](https://github.com/elyse502/Practices/assets/125453474/a990d5d3-c11b-4ae8-ac30-fd4cce85ed1b)

Here's is an _**example**_:

Think of a `car`, a **car** is an object with **`properties`** such as `make, model` and `color` and **`methods`** like `start(), stop()` and `move()`. Now you might say what we don't have `cars` in our `programs`, give me a real programming `example`. Okay think of _**`local storage object`**_ in your `browser's`, every `browser` has a `local storage object` that allows you to store `data locally`. This **local storage object** has a `property` like `length` which returns the number of `objects` in the storage and `methods` like `set item` and `remove item`.

![Screenshot 2024-04-29 114120](https://github.com/elyse502/Practices/assets/125453474/36b4bd05-1ecc-4b25-a6d1-36de4c3d17e6)

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
We can have an `employee object` with 3 **`properties:`** `baseSalary`, `overtime` and `rate` and a **`method`** called `getWage`, now why is this better? well first of all look at the `getWage function`, this `function` has no `parameters`. In contrast in a _**`procedural example`**_ our `getWage function` has 3 `parameters`, the reason in the other **implementation** we don't have any parameters is because all those parameters(`baseSalary`, `overtime` and `rate`) are actually modeled as `properties` of that **object(`employee`)**. All those `properties` and `getWage function` they are highly related, so they are part of one _**`unit`**_. So one of the `symptons` of the **procedure** code is `functions` with so many `parameters`, when you write **code** in **`object-oriented`** way your `functions` end up having fewer and fewer `parameters`. As **`Uncle Bob`** says "the best `functions` are those with no `parameters`", The **fewer** the number of `parameters` the **easier** it is to use and maintain that `function`. So that's **`Encapsulation`**.

![Screenshot 2024-04-29 113455](https://github.com/elyse502/Practices/assets/125453474/7925d938-2f34-42ea-b9db-ec64166005db)

Now let's look at **`Abstraction:`**

---

### 2. Abstraction
Think of a `DVD player` as an `object`, this `DVD player` has a complex **logic board** on the inside and a few **buttons** on the outside that you interact with, you simply press the `play button` and you don't care what happens on the inside, all that `complexity` is hidden from you. This is **`abstraction`** in practice, we can use the same `technique` in our objects so we can hide some of the `properties` and `methods` from the outside and this gives us a couple of **benefits**, first is that we'll make the `interface` of those `objects` simpler. Using an understanding an `object` with a few `properties` and `methods` is **easier** than an `object` with several `properties` and `methods`. The second **benefit** is that it helps us reduce the impact of **change**, let's imagine that tomorrow we change these **inner** or **private** `methods` none of these **changes** will leak to the outside because we don't have any **code** that touches these `methods` outside of their containing `object`, we may **delete** a `method` or **change** its `parameters` but none of these **changes** will impact the rest of the `applications code`. So with `abstraction` we reduce the impact of **change**.

![Screenshot 2024-04-29 113316](https://github.com/elyse502/Practices/assets/125453474/9a01f05e-e1a6-49b8-befb-3036e5b5c584)

---

### 3. Inheritance
**`Inheritance`** is a mechanism that allows you to eliminate the `redundant code`. Here is an example:

Think of `HTML` **elements** like `TextBoxes`, `Drop-down lists`, `CheckBoxes` and so on.... All these `elements` have a few things in common, they should have `properties` like `hidden` and `innerHTML` and `methods` like `click()` and `focus()`. Instead of redefining all those `properties` and `methods` for every **type** of `HTML` **element** we can define them once in a generic `object` call it `HTMLElement` and have other `objects` inherit these `properties` and `methods`, so **`inheritance`** helps us eliminate `redundant code`.

![Screenshot 2024-04-30 081722](https://github.com/elyse502/Practices/assets/125453474/5c77f26a-6fcb-4991-ba84-62dd123145cc)

---

### 4. Polymorphism
`poly` means `many` & `morph` means `form`, so `polymorphism` means `many forms`. In **Object-oriented Programming** `polymorphism`is a technique that allows you to get rid of long `if` and `else` or `switch` and `case` **statements**, so back to our `HTML` **elements** example:

![Screenshot 2024-04-29 111831](https://github.com/elyse502/Practices/assets/125453474/dfff2d30-7118-48b8-8bf0-20f59b6269ad)

All those `objects` should have the ability to be **rendered** on a **page**, but the way each **element** is rendered is different from others. If we want to **render** multiple `HTML` **elements** in a `procedural` way our code would probably look like this:

```groovy

switch (...) {
  case `select`: renderSelect();
  case `text`: renderTextBox();
  case `checkbox`: rederCheckBox();
  case ...
  case ...
  case ...
}

```

But with `object-orintation` we can implement a render `method` in each of those `objects`: 

![Screenshot 2024-04-29 112841](https://github.com/elyse502/Practices/assets/125453474/1fb4befe-5126-42bd-901c-2181c6b69e3d)

And the render `method` will behave differently depending on the type of the `object` we are referencing, so we can get rid of that nasty `switch` and `case` and use one line of code like this:

```groovy

element.render();

```

---

## BENEFITS OF OOP
### 1. Encapsulation
Using `encapsulation` we group related `variables` and `functions` together and this way we can reduce `complexity`. Now we can reuse these `objects` in different parts of a **program** or in different **programs**.

### 2. Abstraction
With `abstraction` we hide `details` and the `complexity` and show only the `essentials`.

### 3. Inheritance
With `inheritance` we can eliminate `redundant code`

### 4. Polymorphism
With `polymorphism` we can **refactor** ugly `switch`  `case` **statements**

![Screenshot 2024-04-29 114430](https://github.com/elyse502/Practices/assets/125453474/bcc72d8f-17b6-42a1-b6f2-e0bcbe42f2af)

---

## value vs Reference Types
In `JavaScript` we have two categories of `types`, on one side we have **value types** also called **primitives** and the other side we have **reference types**.








