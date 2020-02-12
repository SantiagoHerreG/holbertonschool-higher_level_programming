#!/usr/bin/node
const list = process.argv;
const fs = require('fs');
const request = require('request');
request(list[2], function (error, response, body) {
  if (error) {
    return console.error('error:', error);
  }
  fs.writeFile(list[3], body, 'utf-8', function (err) {
    if (err) {
      return console.log(err);
    }
  });
});
