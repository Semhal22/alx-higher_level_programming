#!/usr/bin/node
const { argv } = require('process');
const first = parseInt(argv[2]);
console.log(factorial(first));
function factorial (num) {
  if (!num) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
