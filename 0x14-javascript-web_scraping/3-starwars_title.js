#!/usr/bin/node
const list = process.argv;
const request = require('request');
request('http://swapi.co/api/films/' + list[2] + '/', function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  console.log(JSON.parse(body).title);
});
