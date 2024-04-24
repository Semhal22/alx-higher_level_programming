#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const path = process.argv[2];
const file = process.argv[3];
request(path, function (err, response, body) {
  if (err) {
    return;
  }
  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
