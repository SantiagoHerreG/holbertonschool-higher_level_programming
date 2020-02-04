#!/usr/bin/node
const list = process.argv;
let i, num;
if (!list[2] || !list[3]) {
  console.log('0');
} else {
  for (i = 2; i < list.length; i++) {
    num = Number(list[i]);
    list[i] = num;
  }
  list.sort(function (a, b) { return (b - a); });
  console.log(list[3]);
}
