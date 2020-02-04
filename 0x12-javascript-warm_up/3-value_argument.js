#!/usr/bin/node
const list = process.argv;
if (list[2]) {
  console.log(list[2]);
} else {
  console.log('No argument');
}
