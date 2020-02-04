#!/usr/bin/node
const list = process.argv;
let max, i;
if (!list[2] || !list[3]) {
  console.log('0');
} else {
  max = list[2];
  for (i = 3; i < list.length; i++) {
    if (list[i] > max) {
      max = list[i];
    }
  }
  console.log(max);
}
