#!/usr/bin/node
const myArgs = process.argv;
if (myArgs.length > 3) {
  console.log('Arguments found');
} else if (myArgs.length === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
