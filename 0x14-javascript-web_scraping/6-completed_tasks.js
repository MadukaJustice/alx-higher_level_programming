#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const tasks = JSON.parse(body);
  const completedTasks = {};
  for (const t of tasks) {
    if (t.completed) {
      if (completedTasks[t.userId]) {
        completedTasks[t.userId]++;
      } else {
        completedTasks[t.userId] = 1;
      }
    }
  }
  console.log(completedTasks);
});
