#!/usr/bin/node

const SquareC = require('./5-square')

class square extends SquareC {
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

module.ecports = Square;

			
