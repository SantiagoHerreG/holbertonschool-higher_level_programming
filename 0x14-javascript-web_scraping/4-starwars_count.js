#!/usr/bin/node
const list = process.argv;
const request = require('request');
request(list[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  let i = 0;
  let j;
  let count = 0;
  let actors;
  const movies = JSON.parse(body).results;
  for (; i < movies.length; i++) {
    actors = movies[i].characters;
    for (j = 0; j < actors.length; j++) {
      if (actors[j] === 'https://swapi.co/api/people/18/') {
        count++;
      }
    }
  }
  console.log(count);
});
