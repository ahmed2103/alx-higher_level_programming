#!/usr/bin/node
const fs = require('fs');

const f1Arg = fs.readFileSync(process.argv[2]).toString();
const f2Arg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], f1Arg + f2Arg);
