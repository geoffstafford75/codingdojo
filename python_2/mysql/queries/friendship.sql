USE FRIENDSHIP_SCHEMA;

INSERT INTO USERS (FIRST_NAME, LAST_NAME) 
VALUES
("Amy","Giver"),("Eli","Byers"),("Marky","Mark"),("Kermit","The Frog"),("Big","Bird"),("Oscar","The Grouch");

SELECT * FROM USERS;

INSERT INTO FRIENDSHIPS (USER_ID,FRIEND_ID) VALUES
(1,2),(1,4),(1,6),(2,1),(2,3),(2,5),(3,2),(3,5),(4,3),(5,1),(5,6),(6,2),(6,3);

SELECT * FROM FRIENDSHIPS;

SELECT * FROM users 
JOIN friendships ON USERS.ID = FRIENDSHIPS.USER_ID
LEFT JOIN users as user2 ON USER2.ID = FRIENDSHIPS.FRIEND_ID;

SELECT USERS.FIRST_NAME, USERS.LAST_NAME, USER2.first_name as friend_first_name, USER2.last_name as friend_last_name
FROM USERS
JOIN friendships ON USERS.ID = FRIENDSHIPS.USER_ID
LEFT JOIN users as user2 ON USER2.ID = FRIENDSHIPS.FRIEND_ID;

SELECT USERS2.FIRST_NAME as first_name, USERS2.last_name, users.first_name as friends
FROM USERS
JOIN friendships ON USERS.ID = FRIENDSHIPS.USER_ID
LEFT JOIN users as USERS2 ON USERS2.ID = FRIENDSHIPS.FRIEND_ID
WHERE USERS.ID = 1;

SELECT COUNT(*) FROM FRIENDSHIPS;

SELECT USER_ID, USERS.FIRST_NAME, USERS.LAST_NAME, count(USER_ID) AS num_of_friends from friendships
JOIN users on USERS.ID = FRIENDSHIPS.USER_ID
GROUP BY USER_ID
ORDER BY num_of_friends
LIMIT 1;

SELECT users2.first_name as first_name,  users2.last_name as last_name, users.first_name as friends_with
FROM USERS
JOIN friendships ON USERS.ID = FRIENDSHIPS.USER_ID
LEFT JOIN users as USERS2 ON USERS2.ID = FRIENDSHIPS.FRIEND_ID
WHERE USERS.ID = 3
ORDER BY last_name ASC;






