#!/usr/bin/node

const fs = require('fs');
// Import Node.js 'fs' module.

fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Use fs.readFile() to read the contents of a file specified argv
  // 'utf8' specifies the encoding of file being read

  if (error) {
    // If an error occurs during file read operation, the 'error' parameter will contain an error object.
    console.error('Error reading the file:', error);

  } else {
    // If the file is read successfully, the 'content' parameter will contain the contents of file as a string.
    console.log(content);
  }
});
