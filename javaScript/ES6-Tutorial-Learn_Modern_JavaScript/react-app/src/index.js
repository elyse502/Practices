// var -> function-scoped
// let -> block-scoped
// const -> block-scoped


// var is function-scoped
console.log('var is function-scoped');
function start() {
  for (var i = 0; i < 2; i++) {
    console.log(i);
  }
console.log(i);
}
start();


// let is block-scoped
console.log('let is block-scoped');
function sayHello() {
  for (let i = 0; i < 5; i++) {
    console.log(i);
  }
}

sayHello();


// The difference between let and const is that const is constant and cannot be changed
const x = 1;
// x = 2; // This will throw an error
console.log(x);


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

const square1 = number => number * number; // This is an arrow function(New JavaScript)
console.log(square1(5));

// Now let's see where these arrow function are really useful
const jobs = [
  { id: 1, isActive: true },
  { id: 2, isActive: true },
  { id: 3, isActive: false }
];

const activeJobs = jobs.filter(function(job) { return job.isActive; }); // This is a regular function(Old JavaScript)
const activeJobs1 = jobs.filter(job => job.isActive); // This is an arrow function(New JavaScript)
console.log(activeJobs1);
