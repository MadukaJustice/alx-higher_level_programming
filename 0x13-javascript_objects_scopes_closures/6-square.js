#!/usr/bin/node
// A class Square that defines a square and inherits from Rectangle

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint(c) {
    let letter = 'X';
    if (c) letter = c;
    for (let i = 0; i < this.height; i++) {
      let letter = '';
      for (let j = 0; j < this.width; j++) {
        letter += c;
      }
      console.log(letter);
    }
  }
}

module.exports = Square;
