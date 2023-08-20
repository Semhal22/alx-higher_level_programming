#!/usr/bin/node
const Parent = require('./5-square');
class Square extends Parent {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let value = '';
      for (let j = 0; j < this.width; j++) {
        value += c;
      }
      console.log(value);
    }
  }
}
module.exports = Square;
