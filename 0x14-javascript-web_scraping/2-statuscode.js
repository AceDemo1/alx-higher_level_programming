#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);
const options = {
  url: myArgs[0],
  method: 'GET',
  headers: {
    'Accept-Charset': 'utf-8'
  }
};
request(options, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
