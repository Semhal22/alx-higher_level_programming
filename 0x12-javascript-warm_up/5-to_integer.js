#!/usr/bin/node
const { argv } = require('process');
const first = argv[2];
const num = parseInt(first);
if (!num) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
