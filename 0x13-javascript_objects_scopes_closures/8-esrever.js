#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let temp = 0;
  console.log(len);
  if (len % 2 === 0) {
    for (let i = 0; i <= list.length / 2; i++) {
      temp = list[i];
      list[i] = list[len];
      list[len] = temp;
      len--;
    }
  } else {
    for (let i = 0; i < list.length / 2; i++) {
      temp = list[i];
      list[i] = list[len];
      list[len] = temp;
      len--;
    }
  }
  return list;
};
