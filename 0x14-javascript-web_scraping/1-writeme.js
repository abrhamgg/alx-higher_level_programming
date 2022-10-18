#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

fs.writeFile(args[3], args[2], (err) => {
  if (err) { console.log(err); }
});
