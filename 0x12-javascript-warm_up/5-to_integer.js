#!/usr/bin/node

if (isNaN(process.argv[2])) {
    console.log("Not a number");
} else {
    const integ = Math.floor((Number(process.argv[2])));
    console.log(`My number: ${integ}`);
}
