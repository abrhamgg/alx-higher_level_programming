const request = require('request');
const characterId = 18;
const url = "https://swapi-api.hbtn.io/api/films";
const characters = "https://swapi-api.hbtn.io/api/people/";
const req = characters + characterId;
var URL = url + "?characters=" + req;
URL = "https://swapi-api.hbtn.io/api/films/?characters=%22https://swapi-api.hbtn.io/api/people/18/"

request(URL, function(err, response, body) {
    if (err) {
        console.log(err);
    }
    else {
    }
    const object = (JSON.parse(body));
    const count = 0;
    const len = Object.keys(object['results']).length;
    const ch = object['results'];
    for ( i in object['results']){
        console.log(object['results'][i]['title']);
        console.log(ch)
    }

    console.log((object.results[0]['characters']));
})