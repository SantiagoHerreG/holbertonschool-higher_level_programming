#!/usr/bin/node
exports.addMeMaybe = function (num, f) {
  num++;
  f(num);
};
