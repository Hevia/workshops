// Importing the libaries
const express = require('express');
const path = require('path');
const logger = require('morgan');
const request = require('request-promise');
const cookieParser = require('cookie-parser');

// Creating our express object
const app = express();

// Configuring the properties for our express object
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use('/public', express.static(path.join(__dirname, 'public')));

// Configuring our project settings
const port = process.env.PORT || 3000; // This is a terenary operator. If youre deployed it will use that machines port, otherwise localhost:3000
const accountId = process.env.ACCOUNT_ID || "ACCOUNT_ID";
const subscriptionKey = process.env.SUBSCRIPTION_KEY || "SUBSCRIPTION_KEY";

// The main page
app.get('/', function (req, res) {
  res.render('index.html');
});

// The search request!
// req is the request we are making
// res is the response we get back from the server
app.get('/search', function (req, res) {

  // In our "then()" method we are passing it what is known as an anonymous function
  // This is common in ES6 JavaScript and beyond!
  getAccessToken().then(accessToken => {
    const query = req.query.query;

    // The "get()" method accepts an object 
    return request.get({
      // Objects can be boiled down to key/value pairs similar to HashTables you might have learned in CS2!
      url: ` https://api.videoindexer.ai/trial/Accounts/${accountId}/Videos/Search?query=${query}&accessToken=${accessToken}`,
      
      // The "key" is transform and the "value" is a function. 
      transform: function(response) {
        return JSON.parse(response)
      },
    })
  }).then((response) => {
    res.header('Content-Type' , 'application/json');
    res.json(response);
  }).catch((error) => {
    console.log('An error occurred: ' + error);
  });
});


// You might have noitced how "then" is called multiple times.
// This is what is known as a "Promise". This is a common pattern in programming
// You are basically making a promise that the website will eventually get data back
// Read more about it here: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then
app.get('/thumbnail', function (req, res) {
  getAccessToken().then(accessToken => {
    const videoId = req.query.videoId;
    const id = req.query.id;
    return request({
      url: `https://api.videoindexer.ai/trial/Accounts/${accountId}/Videos/${videoId}/Thumbnails/${id}?accessToken=${accessToken}`,
      method: 'GET',
      encoding: null
    })
  }).then((response) => {
    res.set('Content-Type', 'image/jpeg');
    res.send(response);
  }).catch((error) => {
    console.log('An error occurred: ' + error);
  });
});

// To clean up our code 
function getAccessToken() {
  return request.get({
    url: `https://api.videoindexer.ai/auth/trial/Accounts/${accountId}/AccessToken`, // This is whats known as a template string
    transform: function(response) {
      return JSON.parse(response)
    },
    headers: {
      "Ocp-Apim-Subscription-Key": subscriptionKey
    }
  });
}

app.listen(port, '0.0.0.0', () => console.log(`App listening on port ${port}!`));
