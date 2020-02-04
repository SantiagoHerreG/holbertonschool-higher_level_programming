#!/usr/bin/node
const list = process.argv;
if (list[3]) {
  console.log('Arguments found');
} else if (list[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
