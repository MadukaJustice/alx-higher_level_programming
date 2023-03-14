#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};
for (const key in dict) {
  const i = dict[key];
  if (newDict[i] === undefined) {
    newDict[i] = [];
  }
  newDict[i].push(key);
}

console.log(newDict);
