#!/usr/bin/node
const { argv } = require('process');
const input = argv.slice(2);
const len = input.length;
if (len === 0 || len === 1) {
  console.log(0);
} else {
  let max = findMax(input, len);
  let newArr = input;

  newArr = input.filter((arg) => {
    return +arg !== max;
  });
  max = findMax(newArr, newArr.length);
  console.log(max);
}
function findMax (input, len) {
  let max = +input[0];
  for (let i = 1; i < len; i++) {
    if (+input[i] > max) {
      max = +input[i];
    }
  }
  return max;
}
