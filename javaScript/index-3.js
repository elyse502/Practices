// reference types: Object, Array, Function

/* An object is a data structure that we use to represent 
a collection of key-value pairs. */


let person = {
  name: 'Elysee',
  age: 30
};

// Dot Notation
person.name = 'John';


// Bracket Notation
person['name'] = 'Mary';
// OR
let selection = 'name';
person[selection] = 'Mary';

console.log(person.name);