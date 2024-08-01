#!/usr/bin/node

const fs = require('fs');
const myArgs = process.argv.slice(2);
fs.readFile(myArgs[0], 'utf-8', (err, data) => {
  if (err) { console.log(err); }
  console.log(data);
});
