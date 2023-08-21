#!/usr/bin/node

// This script reads and prints the content of a file

const filepath = process.argv[2];
const content = process.argv[3];

// imports the file storage module
const fs = require('fs');

// uses the writeFile function of the fs module

fs.writeFile(filepath, content, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
