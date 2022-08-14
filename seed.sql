
DROP DATABASE IF EXISTS  adopt_db;

CREATE DATABASE adopt_db;

\c adopt_db

CREATE TABLE pets
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  species TEXT NOT NULL,
  photo TEXT,
  age INT,
  notes TEXT,
  available BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO pets
  (name, species, photo, age, notes, available)
VALUES
  ('Huskion', 'dog', 'https://avatarfiles.alphacoders.com/112/11296.jpg', 3, 'Lazy pup', 't'),
  ('Donald', 'bird', 'https://www.poultryshowcentral.com/images/Call-Duck-Head.jpg', 1, null, 't'),
  ('Blackie', 'cat', 'https://www.catster.com/wp-content/uploads/2015/06/tiny-meowing-black-kitten1.jpg', 2, 'Loud and Hungry', 't'),
  ('The Beak', 'bird', null, null, null, 't');

