#!/usr/bin/node
exports.function addMeMaybe (number, theFunction) {
  theFunction(number++);
}
