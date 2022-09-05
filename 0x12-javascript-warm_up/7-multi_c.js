#!/usr/bin/node
const myArgs = process.argv;
if (!myArgs[2]) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myArgs[2]; i++) {
    console.log('C is fun');
  }
}
