#!/usr/bin/node

const squareC = require(./5-square)

class square extends squareC {
	charPrint(c) {
		if (c === undefined) {
			c = 'x';
		}
		for (let i = 0; i < this.height; i++) {
			let s = '';
			for (let j = 0; j < this.width; j++) {
				s += c;
			}
			console.log(s);
		}
	}
}

module.ecports = square;

			
