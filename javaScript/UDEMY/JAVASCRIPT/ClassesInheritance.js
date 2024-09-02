class Animal{
    constructor(name){
        this.name = name;
    }
    makeSound(){
        console.log(`${this.name} makes a generic sound`);
    }
}

class Cat extends Animal{
    makeSound(){
        console.log(`${this.name} says meow!`);
    }
}

const myCat = new Cat('Whiskers');
myCat.makeSound();