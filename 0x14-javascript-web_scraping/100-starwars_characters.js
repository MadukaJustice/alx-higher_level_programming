#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const film = JSON.parse(body);
  for (const c of film.characters) {
    request.get(c, (err, res, body) => {
      if (err) {
        console.error(err);
      }
      const ch = JSON.parse(body);
      console.log(ch.name);
    });
  }
});
