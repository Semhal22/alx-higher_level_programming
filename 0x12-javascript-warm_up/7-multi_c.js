#!/usr/bin/node
const { argv } = require('process');
const x = parseInt(argv[2]);
let i = 0;
if (!x) {
  console.log('Missing number of occurrences');
} else {
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
