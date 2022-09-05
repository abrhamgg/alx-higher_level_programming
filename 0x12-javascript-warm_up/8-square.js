#!/usr/bin/node
const myArgs = process.argv;
if (!myArgs[2] || !Number.isInteger(myArgs[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myArgs[2]; i++) {
    for (let j = 0; j < myArgs[2]; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
