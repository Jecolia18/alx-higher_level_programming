#!/usr/bin/node
function fact (a) {
  if (a < 0) {
    return (-1);
  } else if (a === 0 || isNaN(a)) {
    return (1);
  }
  return (fact(a - 1) * a);
}
console.log(fact(Number(process.argv[2])));
