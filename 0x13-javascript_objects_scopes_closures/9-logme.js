#!/usr/bin/node
let ncall = 0;

exports.logMe = function (item) {
    console.log(ncall+ ': ' + item);
    ncall++;
}