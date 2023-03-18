#!/usr/bin/node
// searches the second biggest integer in the list of arguments

const getSecondMax = (arr) => {
  let max = parseInt(arr[2]);
  let secMax = parseInt(arr[2]);
  
  if ((arr.length === 2) || (arr.length === 3)) {
    return (0);
  }
    for (let i = 3; i < arr.length; i++) {
      if (parseInt(arr[i]) >= max) {
        secMax = max;
        max = parseInt(arr[i]);
      } else if (parseInt(arr[i]) > secMax) {
        secMax = parseInt(arr[i]);
      }
    }
    return (secMax);
  };

console.log(getSecondMax(process.argv));
