#!/usr/bin/node
const myArgs = process.argv;
if (myArgs[2]) {
  console.log(myArgs[2]);
} else {
  console.log('No argument');
}
