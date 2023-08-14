#!/usr/bin/node
const { argv } = require('process');
const lenArr = argv.length;

if (lenArr === 2 || lenArr === 3) {
  console.log(0);
} else {
  let max = findMax(argv, lenArr);
  const newArr = argv;
  const index = newArr.indexOf(max);

  newArr.splice(index, 1);
  max = findMax(newArr, newArr.length);
  console.log(max);
}

function findMax (arr, len) {
  let max = arr[2];
  for (let i = 3; i < len; i++) {
    if (argv[i] > max) {
      max = argv[i];
    }
  }
  return max;
}
