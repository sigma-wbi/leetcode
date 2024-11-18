SELECT today.id id
FROM Weather today
JOIN Weather yesterday
ON DATEDIFF(today.recordDATE, yesterday.recordDATE) = 1
AND today.temperature > yesterday.temperature;