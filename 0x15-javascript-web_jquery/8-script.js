$.get('https://swapi.co/api/films/?format=json', function (data) {
  const moviesList = data.results;
  let i = 0;
  for (; i < moviesList.length; i++) {
    $('UL#list_movies').append($('<li></li>').text(moviesList[i].title));
  }
});
