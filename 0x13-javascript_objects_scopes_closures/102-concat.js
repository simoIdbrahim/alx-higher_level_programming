#!/usr/bin/node
const fs = require('fs').promises;
const { argv } = require('process');
const fileOne = argv[2];
const fileTwo = argv[3];
const fileThree = argv[4];
async function concatTwoFiles () {
  try {
    const dataOne = await fs.readFile(fileOne);
    const dataTwo = await fs.readFile(fileTwo);
    fs.writeFile(fileThree, dataOne + dataTwo);
  } catch(err) {
    console.log(err);
  }
}
concatTwoFiles();
