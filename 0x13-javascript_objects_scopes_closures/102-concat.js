#!/usr/bin/node
const fs = require('fs');

const fArg1 = fs.readFileSync(process.argv[2]).toString();
const fArg2 = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fArg1 + fArg2);
