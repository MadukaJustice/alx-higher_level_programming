#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const film = JSON.parse(body);
  console.log(film.title);
});
