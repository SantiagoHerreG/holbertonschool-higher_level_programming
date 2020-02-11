#!/usr/bin/node
const list = require('./100-data').list;
const newArr = list.map(function (x, i) { return x * i; });
console.log(list);
console.log(newArr);
