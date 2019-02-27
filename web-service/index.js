'use strict'
require('dotenv').load({
    path: '.env'
});

var express    = require('express');        // call express
var app        = express()               // define our app using express
const AWS = require('aws-sdk');

const dynamodb = new AWS.DynamoDB();

const param = {
    ReturnConsumedCapacity: "TOTAL",
    Item: {}
}
var port = process.env.PORT || 8080;        // set our port

// ROUTES FOR OUR API
// =============================================================================
var router = express.Router();              // get an instance of the express Router


router.get('/movie', function(req, res) {
    const movie = req.query.movie;
    dynamodb.getItem({
        TableName: process.env.TABLE_NAME,
        Key: {
            "movieTitle": {
              S: movie
            }
        }
    }, (err, data) => {
        if (err) {
            console.error(err)
            return res.send('Something went wrong!')
        }
        if (!data.Item) {
            return res.send('No recommendations found for ', movie)
        }
        console.log(data)
        const movies = data.Item
        res.send({
            code: 200,
            movies: movies.recommendations['SS']
        })
    })
});

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/api/1', router);

// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Server listening', port);
