#!/usr/bin/node
exports.esrever = function (list) {
  let last;
  let i = 0;
  const res = [];
  last = list.length - 1;
  for (; last >= 0; last--) {
    res[i] = list[last];
    i++;
  }
  return res;
};
