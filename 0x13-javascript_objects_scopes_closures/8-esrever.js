#!/usr/bin/node
// Returns the reversed version of a list

exports.esrever = function (list) {
  let newList = [];
  let index = list.length;
  while (index >= 0) {
    newList.push(list[index]);
    index--;
  }
  return (newList);
};
