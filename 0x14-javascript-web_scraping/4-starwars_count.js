#!/usr/bin/node
const request = require('request');
const api = process.argv[2];
request(api, function (err, response, body) {
  if (err) {
    return;
  }
  const data = JSON.parse(body);
  const Wedge = data.results.filter(film =>
    film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
  );
  console.log(Wedge.length);
});
