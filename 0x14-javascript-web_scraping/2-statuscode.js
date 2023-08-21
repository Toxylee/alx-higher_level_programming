#!/usr/bin/node

// This script displays the status code of a GET request.

const url = process.argv[2];

// This line imports the request module
const req = require('request');

req(url, (err, res) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
