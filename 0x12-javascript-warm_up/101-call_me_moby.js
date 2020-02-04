#!/usr/bin/node
exports.callMeMoby = function (x, f) {
  let i = 0;
  for (; i < x; i++) {
    f();
  }
};
