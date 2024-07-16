#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    for (let i = 0; i < this.h; i++) {
      console.log('X'.repeat(this.w))
    }
}
module.exports = Rectangle;
