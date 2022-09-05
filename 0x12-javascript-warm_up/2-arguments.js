#!/usr/bin/node
const myArgs = process.argv;
if (myArgs.length > 2){
	console.log('Arguments found');
} else {
	console.log('No argument');
}
