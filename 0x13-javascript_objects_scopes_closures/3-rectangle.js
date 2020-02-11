#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j = 0;
    let string = '';
    for (; i < this.height; i++) {
      string = '';
      for (j = 0; j < this.width; j++) {
        string += 'X';
      }
      console.log(string);
    }
  }
};
