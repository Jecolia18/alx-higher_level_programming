#!/usr/bin/node
if (process.argv.length <= 3) {
	console.log("0");
} else {
	const arr = process.argv.slice(2).map(Number);
	const snd = arr.sort(function (x, y) {return y - x;})[1];
	console.log(snd);
}
