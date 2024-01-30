#!/usr/bin/node
const fs = require('fs');
// script that reads and prints the content of a file
fs.readFile(process.argv[2], 'utf-8', (error, content) => {
  if(error) {
    console.log(error);
  } else {
    console.log(content);
  }
})
