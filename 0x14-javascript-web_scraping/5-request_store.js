#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const myArgs = process.argv.slice(2);
const options = {
  url: myArgs[0],
  method: 'GET',
  headers: {
    'Accept-Charset': 'utf-8'
  }
};
request(options, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(myArgs[1], body, 'utf-8', (err, data) => {
      if (err) console.log(err);
    });
  }
});
