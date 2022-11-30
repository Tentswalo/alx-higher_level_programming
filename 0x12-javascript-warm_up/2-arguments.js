#!/usr/bin/node
// JS to check arguments passed into script

if (process.argv.length < 3) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Best Argument found');
} else {
  console.log('Best School Arguments found');
}
