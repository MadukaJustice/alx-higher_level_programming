#!/usr/bin/node

const fs = require('fs');

const srcA = process.argv[2];
const srcB = process.argv[3];
const dest = process.argv[4];

const contentA = fs.readFileSync(srcA, 'utf8');
const contentB = fs.readFileSync(srcB, 'utf8');
fs.writeFileSync(dest, contentA + contentB);
