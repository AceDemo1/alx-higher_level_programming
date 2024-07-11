#!/usr/bin/node
const i = parseInt(process.argv[2]);
console.log(!isN(i) ? 'My number: ' + i : 'Not a number');
