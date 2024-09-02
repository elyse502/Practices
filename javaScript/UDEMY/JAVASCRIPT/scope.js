let globalvariable = " i am a global";

function exampleFunction() {
  let localVariable = "i am a local";
  console.log(globalvariable);
  console.log(localVariable);
}

exampleFunction();
console.log(globalvariable);


if(true){
    let blockLetVariable = "i'm block-scoped with let";
    const blockConstVariable = "i'm block-scoped with const";
}


function exampleFunctionVar() {
    if(true){
        var functionScopedVariable = "i'm function-scoped with var!";
    }
    console.log(functionScopedVariable);
}
exampleFunctionVar();
// console.log(functionScopedVariable); // ReferenceError: functionScopedVariable is not defined