#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const p = Number(process.argv[2]);
  let j = 0;
  while (j < p) {
    console.log('X'.repeat(x));
    j++;
  }
}
