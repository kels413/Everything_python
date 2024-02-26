-- a sample database for managing my clothes
-- this db helps me to monitor my shirt, know the type of shirt -- it is, the shirt -- color, the shirt size and  how many times I have worn a cloth
-- so i can decide whether to give it out do someother stuff with the shirt.

-- create the DATABASE
CREATE DATABASE IF NOT EXISTS shirts_db;

USE shirts_db;

CREATE TABLE shirts (
  shirt_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  article VARCHAR(20) NOT NULL,
  color VARCHAR(20) NOT NULL,
  shirt_size VARCHAR(1) NOT NULL,
  last_worn INT NOT NULL
);

INSERT INTO
  shirts (article, color, shirt_size, last_worn)
VALUES
  ('t-shirt', 'white', 'S', 10),
  ('t-shirt', 'green', 'S', 200),
  ('polo shirt', 'black', 'M', 10),
  ('tank top', 'blue', 'S', 50),
  ('t-shirt', 'pink', 'S', 0),
  ('polo shirt', 'red', 'M', 5),
  ('tank top', 'white', 'S', 200),
  ('tank top', 'blue', 'M', 15);


-- SELECT ALL DATABASE

SELECT * FROM shirts;

-- insert using a single step
INSERT INTO shirts(article, color, shirt_size, last_worn) VALUES('polo-shirt', 'purple', 'M', 50);

-- SELECT ALL BUH PRINT ONLY ARTICLE AND COLOR

SELECT article, color
From shirts;

-- SELECT ALL MEDUIM SHIRTS BUH ONLY THE ID SHOULD BE PRINTED OUT

SELECT shirt_id
FROM shirts
WHERE shirt_size = 'M';

UPDATE shirts
SET shirt_size = 'L'
WHERE article = 'Polo shirt';