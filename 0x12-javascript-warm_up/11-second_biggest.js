#!/usr/bin/node
const { argv } = require('process');
const input = argv.slice(2);
const lenArr = input.length;

if (lenArr === 0 || lenArr === 1) {
  console.log(0);
} else {
  let max = findMax(input, lenArr);
  let newArr = input;
  // const index = newArr.indexOf(max);

  // newArr.splice(index, 1);
  newArr = input.filter((arg) => {
    return +arg !== max;
  });
  max = findMax(newArr, newArr.length);
  console.log(max);
}

function findMax (arr, len) {
  let max = +arr[0];
  for (let i = 1; i < len; i++) {
    if (+arr[i] > max) {
      max = +arr[i];
    }
  }
  return max;
}
