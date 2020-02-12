#!/usr/bin/node
const list = process.argv;
const request = require('request');
request(list[2], function (error, response, body) {
  if (error) {
    return console.error('error:', error);
  }
  let i = 0;
  const todo = JSON.parse(body);
  const res = {};
  for (; i < todo.length; i++) {
    if (todo[i].completed) {
      if (res[todo[i].userId]) {
        res[todo[i].userId]++;
      } else {
        res[todo[i].userId] = 1;
      }
    }
  }
  console.log(res);
});
