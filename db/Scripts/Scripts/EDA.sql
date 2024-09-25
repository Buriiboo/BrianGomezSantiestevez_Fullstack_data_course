SELECT * FROM youtube;


SELECT DISTINCT(category) FROM youtube;

SELECT COUNT(*) FROM youtube;

SELECT
	category,
	COUNT(*)
FROM
	youtube
GROUP BY
	category;