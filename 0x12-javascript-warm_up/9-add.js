#!/usr/bin/node
const myArgs = process.argv;
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(myArgs[2], myArgs[3]);
