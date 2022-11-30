#!/usr/bin/node
// JS to check arguments passed into script

const process = require('process');
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
