-- list all genres not linked to the show Dexter
-- Using double join
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.title = 'Dexter' and tv_show_genres.show_id = tv_shows.id
ORDER BY tv_genres.name) res
ON tv_genres.name = res.name
WHERE res.name IS NULL;
