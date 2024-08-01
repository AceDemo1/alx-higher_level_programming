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
const comp = {};
request(options, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      if (tasks[i].completed) {
        if (comp[tasks[i].userId]) {
          comp[tasks[i].userId] += 1;
        } else {
          comp[tasks[i].userId] = 1;
        }
      }
    }
  }
  console.log(comp);
});
