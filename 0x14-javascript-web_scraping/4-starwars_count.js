#!/usr/bin/node
const request = require('request');
request('https://swapi.co/api/people/18/', function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  console.log(JSON.parse(body).films.length);
});
