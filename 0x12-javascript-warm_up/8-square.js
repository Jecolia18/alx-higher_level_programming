#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size) === true) {
  console.log('Missing size')
} else {
  for (let i = 1; i <= size; i++) {
	  let part="";
	  for (let j = 1; j <= size; j++) {
		  part +="X";
	  }
	  console.log(part);
  }
}
