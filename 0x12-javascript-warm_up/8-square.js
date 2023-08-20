#!/usr/bin/node
const { argv } = require('process');
const size = parseInt(argv[2]);
let i = 0;
let j = 0;
if (!size) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    let row = '';
    for (j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
