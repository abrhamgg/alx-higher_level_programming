-- count genre by shows
SELECT name, COUNT(*) AS number_of_shows FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY name ORDER BY number_of_shows DESC;
