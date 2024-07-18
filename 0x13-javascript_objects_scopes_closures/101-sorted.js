#!/usr/bin/node
const i = require('./101-data').dict;
const k = {};
for (const i in dict) {
  const j = dict[i];
  if (!k[j]) {
    k[j] = [];
  }
  k[j][k[j].length] = i;
}
return k;
