#!/usr/bin/node
const list = process.argv;
let i = 2;
const fs = require('fs');
let text;
for (; i < list.length; i++) {
  try {
    text = fs.readFileSync(list[i], 'utf-8');
    process.stdout.write(text);
  } catch {
    continue;
  }
}
