#!/usr/bin/node
i = ParseInt(process.argv[2]);
if (isNaN(i)) {
  console.log('Missing number of occurrences');
} else {
  for (let j = 0; j < i; j++) {
  console.log('C is fun');
  }
