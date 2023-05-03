$.get('https://swapi-api.alx-tools/api/films/?format=json', (data) => {
  for (const i in data.results) {
    $('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
  }
});
