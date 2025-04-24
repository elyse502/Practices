#!/usr/bin/node
// Parse JSON string into an object
const jsonString = '{"name":"Elysée","age":25}';
const obj = JSON.parse(jsonString);
console.log(obj.name); // Output: Elysée

// Convert object to JSON string
const newStr = JSON.stringify(obj);
console.log('\n', newStr);

