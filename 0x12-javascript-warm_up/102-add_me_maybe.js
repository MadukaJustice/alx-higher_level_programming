#!/usr/bin/node
// increments a number, and passes it to a function

exports.addMeMaybe = function (number, theFunction) {
  number += 1;
  theFunction(number);
};
