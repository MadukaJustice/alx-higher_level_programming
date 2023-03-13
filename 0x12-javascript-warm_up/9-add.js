#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

if ((process.argv[2] === undefined) || (process.argv[3] === undefined) || (isNaN(process.argv[2])) || (isNaN(process.argv[3]))) {
  console.log('NaN');
} else {
  const num1 = (parseInt(process.argv[2]));
  const num2 = (parseInt(process.argv[3]));

  console.log(add(num1, num2));
}
