#!/usr/bin/node
const i = require('./101-data').dict;
const k = {};
for (const l in i) {
  const j = i[l];
  if (!k[j]) {
    k[j] = [];
  }
  k[j][k[j].length] = l;
}
console.log(k);
