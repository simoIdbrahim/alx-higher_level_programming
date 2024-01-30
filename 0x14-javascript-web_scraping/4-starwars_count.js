#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
const characterId = '18';
let count = 0;

req.get(url, (err, res, body) => {
  if(err) {
    console.log(err);
  } else {
    JSON.parse(body).results.forEach((film) => {
      film.characters.forEach((character) => {
        if(character.includes(characterId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
