#!/usr/bin/node
const i = parseInt(process.argv[2]);
if (isNaN(i)) {
  console.log(1);
} else {
  function fac (i) {
    if (i == 0 || i == 1) {
      return 1;
    } else {
      return fac (i - 1) * i;
    }
  };
  console.log(fac(i));
}
