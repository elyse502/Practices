
/**
 * Factory Functions (a.k.a Factory Pattern)
 * - A function that returns an object
 * - We can create multiple objects using a factory function
 * - We can pass arguments to a factory function to create different objects
 * - We can use factory functions to create objects with different properties
 * - We can use factory functions to create objects with different methods
*/

// Factory Function
function createCircle(radius) {
    return {
        radius,
        draw: function() {
            console.log('draw');
        }
    };
}

const circle = createCircle(1);
circle.draw();
