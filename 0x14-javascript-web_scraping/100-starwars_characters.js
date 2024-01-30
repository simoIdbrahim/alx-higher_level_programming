#!/usr/bin/node

const req = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

req.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }

  JSON.parse(body).characters.forEach(character => {
    req.get(character, (error, response, body) => {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
