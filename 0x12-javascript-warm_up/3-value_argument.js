#!/usr/bin/node
const i = process.argv;
console.log(i[2] === undefined ? 'No argument' : i[2]);
