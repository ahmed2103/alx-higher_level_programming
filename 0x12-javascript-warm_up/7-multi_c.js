#!/usr/bin/node

if (process.argv[2] === undefined || Number.isInteger(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(process.argv[2]);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
