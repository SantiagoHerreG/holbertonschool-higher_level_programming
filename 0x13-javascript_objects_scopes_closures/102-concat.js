#!/usr/bin/node
const list = process.argv;
let i = 2;
const fs = require('fs');
let text = '';
for (; i < list.length - 1; i++) {
  text += fs.readFileSync('./' + list[i], 'utf-8');
}
fs.writeFileSync('./' + list[i], text);
