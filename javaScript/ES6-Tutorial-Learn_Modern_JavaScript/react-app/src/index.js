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
person[targetMember.value] = 'Eric';
console.log(person.name); // Eric