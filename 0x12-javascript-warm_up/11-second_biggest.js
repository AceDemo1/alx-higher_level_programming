#!/usr/bin/node
const i = process.argv;
if (i.length === 2 || i.length === 3) {
  console.log(0);
} else {
  i.sort((a, b) => b - a);
  console.log(i[3]);
}
