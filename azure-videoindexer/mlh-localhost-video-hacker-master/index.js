const express = require('express');
const path = require('path');
const logger = require('morgan');
const request = require('request-promise');
const cookieParser = require('cookie-parser');

const app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use('/public', express.static(path.join(__dirname, 'public')));

const port = process.env.PORT || 3000;
const accountId = process.env.ACCOUNT_ID || "ACCOUNT_ID";
const subscriptionKey = process.env.SUBSCRIPTION_KEY || "SUBSCRIPTION_KEY";

app.get('/', function (req, res) {
  res.render('index.html');
});

app.get('/search', function (req, res) {
  getAccessToken().then(accessToken => {
    const query = req.query.query;
    return request.get({
      url: ` https://api.videoindexer.ai/trial/Accounts/${accountId}/Videos/Search?query=${query}&accessToken=${accessToken}`,
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

function getAccessToken() {
  return request.get({
    url: `https://api.videoindexer.ai/auth/trial/Accounts/${accountId}/AccessToken`,
    transform: function(response) {
      return JSON.parse(response)
    },
    headers: {
      "Ocp-Apim-Subscription-Key": subscriptionKey
    }
  });
}

app.listen(port, '0.0.0.0', () => console.log(`App listening on port ${port}!`));
