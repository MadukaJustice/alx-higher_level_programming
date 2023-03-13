#!/usr/bin/node

const arr = process.argv.slice(2);
function secondBiggest (arr) {
  if (arr.length < 2) {
    return (0);
  } else {
    arr.sort((i, j) => i - j);
    arr.pop();
    return (arr.pop());
  }
}
console.log(secondBiggest(arr));
