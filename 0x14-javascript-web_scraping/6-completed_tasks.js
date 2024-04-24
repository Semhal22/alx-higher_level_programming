#!/usr/bin/node
const request = require('request');
const api = process.argv[2];
request(api, function (err, response, body) {
  if (err) {
    return;
  }
  const tasks = JSON.parse(body);
  const completed = {};

  tasks.forEach(task => {
    if (task.completed) {
      const userId = task.userId;
      completed[userId] = (completed[userId] || 0) + 1;
    }
  });
  console.log(completed);
});
