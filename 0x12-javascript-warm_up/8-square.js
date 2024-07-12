#!/usr/bin/node
i = parseInt(process.argv[2]);
if (is(NaN)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < i; j++) {
    console.log('X' * i);
  }
}
