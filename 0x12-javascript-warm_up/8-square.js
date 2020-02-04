#!/usr/bin/node
let i = 0;
let j = 0;
let string = '';
const num = Number(process.argv[2]);
if (num) {
  for (; i < num; i++) {
    string = '';
    for (j = 0; j < num; j++) {
      string += 'X';
    }
    console.log(string);
  }
} else {
  console.log('Missing size');
}
