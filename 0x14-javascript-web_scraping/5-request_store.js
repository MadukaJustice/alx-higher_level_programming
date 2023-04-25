#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const path = process.argv[3];

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.writeFile(path, body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
