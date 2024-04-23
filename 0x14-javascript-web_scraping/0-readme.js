#!/usr/bin/node
const fs = require('fs');
fileName = process.argv[2];
fs.readFile(fileName, 'utf-8', (er, x) => {
  if (er) { console.log(er); }
  console.log(x);
});
