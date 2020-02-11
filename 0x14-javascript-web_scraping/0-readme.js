#!/usr/bin/node

const list = process.argv;
const fs = require('fs');
try {
  process.stdout.write(fs.readFileSync(list[2], 'utf-8'));
} catch (error) {
  console.log(error);
}
