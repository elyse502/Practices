import { Person } from './person'; // This is how you import a class from another file
export class Teacher extends Person {
    constructor(name, degree) {
      super(name);
      this.degree = degree;
    }
  
    teach() {
      console.log('teach');
    }
  }
