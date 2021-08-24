SELECT activity
FROM Friends
GROUP BY activity
HAVING COUNT(activity) > (SELECT MIN(act) FROM (SELECT COUNT(activity) act FROM Friends GROUP BY activity) T1) AND
       COUNT(activity) < (SELECT MAX(act) FROM (SELECT COUNT(activity) act FROM Friends GROUP BY activity) T2);
-- HAVING COUNT(*) > (SELECT COUNT(*) FROM Friends GROUP BY activity ORDER BY 1 ASC LIMIT 1) AND
--        COUNT(*) < (SELECT COUNT(*) FROM Friends GROUP BY activity ORDER BY 1 DESC LIMIT 1);

-- ORDER BY 1 is known as an ordinal where we sort by the 1st column in the query result