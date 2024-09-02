import { Person } from './person'; // This is how you import a class from another file

export function promote() { // Named export
  console.log('promote');
}

export default class Teacher1 extends Person { // Default export
    constructor(name, degree) {
      super(name);
      this.degree = degree;
    }
  
    teach() {
      console.log('teach');
    }
  }
