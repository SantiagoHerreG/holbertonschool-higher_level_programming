#!/usr/bin/node
const square = require('./5-square');
module.exports = class Square extends square {
  charPrint (c) {
    let i = 0;
    let j = 0;
    let string = '';
    let ch;
    if (c) {
      ch = c;
    } else {
      ch = 'X';
    }
    for (; i < this.height; i++) {
      string = '';
      for (j = 0; j < this.width; j++) {
        string += ch;
      }
      console.log(string);
    }
  }
};
