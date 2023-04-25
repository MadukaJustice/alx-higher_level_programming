#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const ch = JSON.parse(body).characters;
  printCh(ch, 0);
});

function printCh (ch, i) {
  request.get(ch[i], (err, res, body) => {
    if (err) {
      console.error(err);
    }
    console.log(JSON.parse(body).name);
    if (i + 1 < ch.length) {
      printCh(ch, i + 1);
    }
  });
}

/* Alternative method using Promises */

/* #!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }
    const film = JSON.parse(body);
    const ch = film.characters;
    const chPromise = ch.map(c => {
        return new Promise((resolve, reject) => {
            request(c, (error, response, body) => {
                if (error) {
                    reject(error);
                } else {
                    resolve(JSON.parse(body).name);
                }
            });
        });
    });
    Promise.all(chPromise)
        .then(names => {
            names.forEach(name => console.log(name));
        })
        .catch(error => console.error(error));
});
*/
