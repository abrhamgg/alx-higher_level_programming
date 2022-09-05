#!/usr/bin/node
const myArgs = process.argv;
if (!myArgs[2]) {
  console.log(0);
} else if (myArgs.length === 3) {
  console.log(0);
} else {
  let max = 0;
  for (let i = 0; i < myArgs.length; i++) {
    if (parseInt(myArgs[i]) > max) {
      max = parseInt(myArgs[i]);
    }
  }
  let max2 = 0;
  for (let j = 0; j < myArgs.length; j++) {
    const num = parseInt(myArgs[j]);
    if (num > max2 && num < max) {
      max2 = num;
    }
  }
  console.log(max2);
}
