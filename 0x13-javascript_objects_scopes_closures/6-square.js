#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let raw = '';
      c = c === undefined ? raw = 'X' : raw = c;
      for (let j = 1; j < this.width; j++) {
        raw += c;
      }
      console.log(raw);
    }
  }
}
