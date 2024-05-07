/*
function sayHello(name) {
    console.log("Hello, " + name);
}

sayHello("Elysee");


// Global Object
console.log(">> Global Object");
console.log(); // global object is the window object in the browser

// Examples of global object
setTimeout(); // setTimeout is a function of the global object, we use it to call a function after a certain amount of time
clearTimeout(); // clearTimeout is a function of the global object, we use it to cancel a timeout

setInterval(); // setInterval is a function of the global object, we use it to repeatedly call a function after a certain amount of time
clearInterval(); // clearInterval is a function of the global object, we use it to cancel an interval

window; // window is the global object that represents our global scope, so all the variables and functions defined globally. We can access them via this window object so we can call "window.console.log" or simply "console.log"

// Similarly all those "functions" mentioned above they belong to the "window object" so we can call:
window.setTimeout(); // or simply call it directly by using the "window" object "setTimeout()"

// By the same token
var message = "";
window.message; // that variable is also available via the "window object"

// However in "Node" we don't have that "window object" so we have to use "global" object instead
let message = "";

console.log(globalThis.message); */

// console.log(module); // module is an object that represents the current module


const logger = require('./logger'); // We use "const" to declare a constant variable, to avoid to accidentally over write the value of "logger" variable

// console.log(logger);
logger.log("message");


