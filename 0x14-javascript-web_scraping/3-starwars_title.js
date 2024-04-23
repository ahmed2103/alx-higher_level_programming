#!/usr/bin/node
const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  const film = JSON.parse(body);
  console.log(film.title);
});
