#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const tasks = {};
  JSON.parse(body).map((task) => {
    if (task.completed) {
      if (tasks[task.userId] === undefined) {
        tasks[task.userId] = 1;
      } else {
        tasks[task.userId] += 1;
      }
    }
  });
  console.log(tasks);
});