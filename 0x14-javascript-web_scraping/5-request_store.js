#!/usr/bin/node
const request = require('request');
const fs = require('fs');
url = process.argv[2];
fileName = process.argv[3];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  fs.writeFile(fileName, body, 'utf8', function (error) {
    if (error) {
      console.error(error);
    }
  });
});
