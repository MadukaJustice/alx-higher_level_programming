#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  let i = 0;
  const films = JSON.parse(body).results;
  for (const f of films) {
    for (const c of f.characters) {
      if (c.includes('18')) {
        i++;
      }
    }
  }
  console.log(i);
});
