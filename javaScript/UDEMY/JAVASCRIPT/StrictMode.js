// enabling strict mode
"use strict";
// undeclaredVariable = 42;

function silentErrorFunction(){
    let obj = {prop: 42};
    with (obj){


        //console.log(prop);
    }
}
silentErrorFunction();