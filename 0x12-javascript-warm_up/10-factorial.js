#!/usr/bin/node
const myArgs = process.argv;
function factorial (a) {
if (a === 0 || a === 1 ) {
     return (1);
}
return (a * factorial(a - 1));
}
if (!myArgs[2]) {
  console.log(1);
} else {
  console.log(factorial(parseInt(myArgs[2])));
}
