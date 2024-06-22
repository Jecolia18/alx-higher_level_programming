#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (isNaN(num) || num === undefined) {
  console.log('Missing number of occurences');
} else {
  for (let i = 1; i <= num; i++) {
    console.log('C is fun');
  }
}
