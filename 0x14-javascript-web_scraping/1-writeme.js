#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const writeContent = process.argv[3];

fs.writeFile(filename, writeContent, 'utf-8', (error) => {
  if(error) {
    console.log(error);
  }
});
