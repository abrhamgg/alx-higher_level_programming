#!/usr/bin/node

const fs = require('fs');
const args = process.argv[2];
fs.readFile(args[0], 'utf8', function (err, data) {
  if (data) { console.log(data); } else { console.log(err); }
});
