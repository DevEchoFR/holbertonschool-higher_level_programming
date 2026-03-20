#!/usr/bin/node
const parsedNumber = Number.parseInt(process.argv[2]);

if (Number.isNaN(parsedNumber)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parsedNumber);
}
