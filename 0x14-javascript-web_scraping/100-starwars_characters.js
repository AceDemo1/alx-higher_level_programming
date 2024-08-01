#!/usr/bin/node

const request = require('request');
const myArgs = process.argv.slice(2);
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + myArgs[0],
  method: 'GET',
  headers: {
    'Accept-Charset': 'utf-8'
  }
};
request(options, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const chars = (JSON.parse(body).characters);
    chars.forEach(urlPage => {
      request(urlPage, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
