#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const p = Number(process.argv[2]);
  let j = 0;
  while (j < p) {
    console.log('C is fun');
    i++;
  }
}
