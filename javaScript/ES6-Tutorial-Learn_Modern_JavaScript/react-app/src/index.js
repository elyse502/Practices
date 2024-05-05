import { Teacher1 } from './teacher'; // Used on line 248......
import { promote } from './teacher'; // Used on line 259......
// var -> function-scoped
// let -> block-scoped
// const -> block-scoped


// var is function-scoped
console.log('>> var is function-scoped');
function start() {
  for (var i = 0; i < 5; i++) {
    console.log(i);
  }
console.log(i);
}
start();


// let is block-scoped
console.log('>> let is block-scoped');
function sayHello() {
  for (let i = 0; i < 5; i++) {
    console.log(i);
  }
}

sayHello();


// The difference between let and const is that const is constant and cannot be changed
const x = 1;
// x = 2; // This will throw an error
console.log(`The value of "x" is constant(Doesn't change): ${x}`);


// Objects are reference types
const person = {
  name: 'Elysee',
  walk() {},
  talk() {}
};

person.talk();

person['name'] = 'John'; // This is how you can change the value of a property in an object
person.name = ''; // This is another way to change the value of a property in an object

// This is how you can access a property in an object using a variable
const targetMember = 'name';
person[targetMember.value] = 'Eric'; // This will change the value of the name property to Eric
console.log(person.name); // Eric


// The "This" keyword
console.log('>> The "This" keyword');
const person1 = {
  name: 'Elysee',
  walk() {
    console.log(this); // This will return the person object
  }
};

person1.walk(); // This will return a reference to the person object

const walk = person1.walk; // This will return a reference to the walk function
console.log(walk);
walk(); // This will return the global object which is the window object in the browser and the global object in Node.js


// Binding "This"
console.log('>> Binding "This"');
const person2 = {
  name: 'Elysee',
  walk() {
    console.log(this);
  }
};

person2.walk(); // This will return a reference to the person object

const walk2 = person2.walk.bind(person2); // With bind method, we can set the value of "this" permanently. So when we call bind on the walk function, we get a new walk function and in that walk function, the value of "this" is based on the argument that we pass to the bind method
walk2(); // This will return a reference to the person object


// Arrow functions
console.log('>> Arrow functions');
const square = function(number) { // This is a regular function(Old JavaScript)
  return number * number;
};
console.log(square(3));

const square1 = number => number * number; // This is an arrow function(New JavaScript)
console.log(square1(5));

// Now let's see where these arrow function are really useful
const jobs = [
  { id: 1, isActive: true },
  { id: 2, isActive: true },
  { id: 3, isActive: false }
];

const activeJobs = jobs.filter(function(job) { return job.isActive; }); // This is a regular function(Old JavaScript)
console.log(activeJobs);
const activeJobs1 = jobs.filter(job => job.isActive); // This is an arrow function(New JavaScript)
console.log(activeJobs1);


// Arrow functions and "This"
console.log('>> Arrow functions and "This"');
const person3 = {
  talk() {
    setTimeout(function() { // setTimeout is a function that takes a callback function and a delay in milliseconds
      console.log('this', this);
    }, 1000);
  }
};

person3.talk(); // This will return the window object because the "this" keyword in the setTimeout function is not referencing the person object

// To fix the issue above, we can use the bind method
const person4 = {
  talk() {
    var self = this; // This is a common pattern in JavaScript to store the reference to "this" in a variable called self and then use self in the inner function where "this" is not available or not what we expect it to be
    setTimeout(function() {
      console.log('self', self);
    }, 1000);
  }
};

person4.talk(); // This will return the person object

// Another way to fix the issue above is to use an arrow function
const person5 = {
  talk() {
    setTimeout(() => { // Arrow functions inherit the "this" keyword from the containing function which is the talk function in this case and that's why we don't have to use the bind method or the self variable to fix the issue above when using arrow functions in this case because the "this" keyword in the arrow function is referencing the person object which is what we expect it to be in this case and that's why we get the person object in the console when we run the code below and not the window object like we did in the code above when we used the regular function instead of the arrow function in the setTimeout function in the talk function in the person object above
      console.log('this', this);
    }, 1000);
  }
};

person5.talk(); // This will return the person object


// Array.map method
console.log('>> Array.map method');
const colors = ['red', 'green', 'blue'];
// Using a regular function
const items = colors.map(function(color) {
  return '<li>' + color + '</li>';
}); // This will return an array of strings
console.log(items);

// Using an arrow function
const items2 = colors.map((color) => `<li>${color}</li>`); // This will return an array of strings(Written in form of template literals)
console.log(items2);


// Object Destructuring
console.log('>> Object Destructuring');
const address = {
  street: '',
  city: '',
  country: ''
};

// This is repetitive
const street = address.street;
const city = address.city;
const country = address.country;

console.log(street, city, country); // This will return an empty string for each of the variables above

// This is a better way to do the same thing above
const { street: st, city: ct, country: cn } = address; // This is called object destructuring
console.log(st, ct, cn); // This will return an empty string for each of the variables above


// Spread Operator
console.log('>> Spread Operator');
const first = [1, 2, 3];
const second = [4, 5, 6];

// One way to combine the two arrays above
const combined = first.concat(second);
console.log(combined);

// Another way to combine the two arrays above using the spread operator
const combined2 = [...first, 'a', ...second, 'b']; // This is called the spread operator (You can even add new items to the array using the spread operator)
console.log(combined2);

// Using the spread operator to clone an array
const clone = [...first];
console.log(first);
console.log(clone);

// You also apply the spread operator to objects
const firstObj = { name: 'Elysee' };
const secondObj = { job: 'Software Developer' };

const combinedObj = { ...firstObj, ...secondObj, location: 'Rwanda' }; // This is called the spread operator
console.log(combinedObj);

// Similarly, you can use the spread operator to clone an object
const cloneObj = { ...firstObj };
console.log(firstObj);
console.log(cloneObj);


// Classes
console.log('>> Classes');
// This is a class declaration
class Person {
  constructor(name) {
    this.name = name;
  }

  walk() {
    console.log('walk');
  }
}

const person6 = new Person('Elysee'); // That new keyword is used to create an instance of a class
console.log(person6.name);
person6.walk();


// Inheritance OR Composition
console.log('>> Inheritance');
// This is a class declaration
class Teacher extends Person { // The extends keyword is used to inherit from another class
  constructor(name, degree) { // The constructor method is a special method for creating and initializing an object created with a class
    super(name); // The super keyword is used to call the constructor of the parent class
    this.degree = degree;
  }

  teach() {
    console.log('teach');
  }
}

const teacher = new Teacher('Elysee', 'MSc');
teacher.walk();
teacher.teach();
console.log(teacher.degree);


// Modules
console.log('>> Modules');
// This is a module declaration(On top of this file)

const teacher1 = new Teacher1('Elysee', 'MSc');
teacher1.walk();
teacher1.teach();
console.log(teacher1.degree);


// Named and Default exports
console.log('>> Named and Default exports');
// This is a module declaration(On top of this file)

const teacher2 = promote();
console.log(teacher2);

/* We can export one or more objects from a given "module", these objects are called "named exports". So what is exported has a name like the "promote" function or the "Teacher1" class.

Now apart from "named exports" we also have the concept of "default export" and that is the main object that is exported from a given "module". 

Typically we use "default exports" if there is only a single object that we want to export. */