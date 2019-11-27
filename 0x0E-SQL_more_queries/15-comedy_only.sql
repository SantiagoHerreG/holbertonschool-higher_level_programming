-- lists all Comedy shows in the database hbtn_0d_tvshows
-- using double join
SELECT S.title
FROM tv_shows S
JOIN tv_show_genres SG ON S.id = SG.show_id
JOIN tv_genres G ON SG.genre_id = G.id and G.name = "Comedy"
ORDER BY S.title;
