#!/usr/bin/node
exports.esrever = function (list) {
  let reverse = [];
  for (let i = 0; i < list.length; i++) {
    reverse.unshift(list[i]);
  }
  return reverse;
};
