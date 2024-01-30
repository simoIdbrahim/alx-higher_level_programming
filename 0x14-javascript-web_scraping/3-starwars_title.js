#!/usr/bin/node

const req = require('request');
const movieId = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

req.get(movieId, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
