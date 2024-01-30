#!/usr/bin/node

const req = require('request');
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;
let characters = [];

req.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  characters = data.characters;
  loadChar(0);
});

function loadChar (ind) {
  if (ind === characters.length) {
    return;
  }
  req.get(characters[ind], (err, response, body) => {
    if (err) {
      console.log(err);
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    loadChar(ind + 1);
  });
}
