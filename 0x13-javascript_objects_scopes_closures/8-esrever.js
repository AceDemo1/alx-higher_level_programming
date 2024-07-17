#!/usr/bin/node
exports.esrever = function (list) {
  const i = [];
  for (let j = list.length - 1, k = 0; j >= 0; j--, k++) {
    i[k] = list[j];
  }
  return i;
}
