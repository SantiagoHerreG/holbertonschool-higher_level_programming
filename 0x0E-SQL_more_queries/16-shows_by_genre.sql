-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
-- two previous task joined
SELECT S.title, G.name
FROM tv_shows S
LEFT JOIN tv_show_genres SG ON S.id = SG.show_id
LEFT JOIN tv_genres G ON SG.genre_id = G.id
ORDER BY S.title, G.name;
