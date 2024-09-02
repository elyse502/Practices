/* var myVar = 10;
let myLet = 'hello';
const myConst = true; */

let person = {
    firstName: 'John',
    lastName: 'Smith',
    age: 25,
    greet: function() {
        console.log('hello, ' + this.firstName + ' ' + this.lastName + '');
    }
};
person.greet();