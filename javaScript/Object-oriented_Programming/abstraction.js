/**
 * Abstraction: hide the details and complexity and show only the essentials
    * reduce complexity
    * reduce impact of change
    * increase reusability
    * increase maintainability
    * increase flexibility
    * increase security
    * increase performance
    * increase productivity
    * increase scalability
    * increase reliability
    * increase availability
    * increase usability
    * increase testability
    * increase readability
    * increase extensibility
*/


// Let's introduce some complexity in this example. Abstraction will help us to reduce the complexity.
function Circle(radius) {
    this.radius = radius;

    this.defaultLocation = { x: 0, y: 0 };

    this.computeOptimumLocation = function(factor) { // this method is not part of the interface
        // ...
    }


    this.draw = function() {
        this.computeOptimumLocation(0.1); // this method is not part of the interface
        console.log('draw');
    }
}

const circle = new Circle(10); // this object has too many details
