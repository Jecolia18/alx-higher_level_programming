#!/usr/bin/node
if ((process.argv.length <= 2) || (Number(process.argv[2]) === 1)) {
  console.log('0');
} else {
  let max = Number(process.argv[2]);
  let maxt;
  for (let i = 3; i <= Number(process.argv.length); i++) {
    if (Number(process.argv[i]) > max) {
      maxt = max;
      max = process.argv[i];
    }
  }
  console.log(maxt);
}
