DROP TABLE IF EXISTS prints;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    image_pathway VARCHAR(255)
);

CREATE TABLE prints (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    artist_id INT REFERENCES artists(id) ON DELETE CASCADE,
    size VARCHAR(255),
    price INT,
    printing_cost INT,
    stock INT,
    image_print_pathway VARCHAR(255)
);