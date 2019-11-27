-- lists all shows without the genre Comedy
-- Using nested selects
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN (SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.name = "Comedy" AND tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title) res
ON tv_shows.title = res.title
WHERE res.title IS NULL
ORDER BY tv_shows.title;
