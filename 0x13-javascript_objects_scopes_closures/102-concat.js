#!/usr/bin/node
const i = require('fs');
const [,, j, k, l] = process.argv;
const m = i.readFileSync(j).toString();
const n = i.readFileSync(k).toString();
i.writeFileSync(l, m + n);
