#!/usr/bin/node
const list = process.argv;
try {
  const num = Number(list[2]);
  if (!num) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + num);
  }
} catch {
  console.log('Not a number');
}
