#!/usr/bin/node
const i = require('./100-data').list;
const j = i.map((i, j) => i * j);
console.log(i);
console.log(j);
