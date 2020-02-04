#!/usr/bin/node
const list = process.argv;
if (list[3]) {
  console.log(list[2] + ' is ' + list[3]);
} else if (list[2]) {
  console.log(list[2] + ' is undefined');
} else {
  console.log('undefined is undefined');
}
