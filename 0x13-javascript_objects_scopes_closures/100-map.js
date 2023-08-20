#!/usr/bin/node
const obj = require('./100-data');
const list = obj.list;
const newList = list.map((value, index) => value * index);
console.log(list);
console.log(newList);
