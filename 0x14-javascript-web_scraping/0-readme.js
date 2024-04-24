#!/usr/bin/node
const fs = require('fs');
const path = process.argv[2];
fs.readFile(path, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});