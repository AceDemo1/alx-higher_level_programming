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
request(options, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body).results;
    let total = 0;
    for (const i in movies) {
      const people = movies[i].characters;
      for (const j in people) {
        if (people[j].includes('18')) {
          total++;
        }
      }
    }
    console.log(total);
  }
});
