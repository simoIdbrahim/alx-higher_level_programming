#!/usr/bin/node
const req = require('request');

req.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = {};
    JSON.parse(body).forEach(task => {
      if (task.completed === true) {
        if (!data[task.userId]) {
          data[task.userId] = 1;
        } else {
          data[task.userId]++;
        }
      }
    });
    console.log(data);
  }
});
