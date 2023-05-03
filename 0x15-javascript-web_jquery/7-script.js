$.get('https://swapi-api.alx-tools/api/people/5/?format=json', (data) => {
  $('DIV#character').text(data.name);
});
