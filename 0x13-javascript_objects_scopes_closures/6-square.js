#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
