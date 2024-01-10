#!/usr/bin/node
const { argv } = require('process');
const num = parseInt(argv[2]);

console.log(factorial(num));

function factorial (num) {
  if (!num || num <= 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
