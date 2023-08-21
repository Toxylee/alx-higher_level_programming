#!/usr/bin/node

// This script reads and prints the content of a file

const filepath = process.argv[2];

// imports the file storage module
const fs = require('fs');

fs.readFile(filepath, 'utf8', (err, content) => {
  if (err) {
    console.log(err);
  } else {
    console.log(content);
  }
});
