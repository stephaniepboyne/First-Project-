from db.run_sql import run_sql
from models.artist import Artist
from models.print import Print 

def save(artist):
    sql = "INSERT INTO artists (name, image_pathway) VALUES (%s, %s) RETURNING *"
    values = [artist.name, artist.image_pathway]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['image_pathway'], row['id'])
        artists.append(artist)
    return artists 

def select(id):
    artist = None

    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id] 

    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'], result['image_pathway'], result['id'])
    return artist 

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def prints(artist):
    prints = []

    sql = "SELECT * FROM prints where artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        print = Print(row['title'], row['artist_id'], row['size'], row['price'], row['printing_cost'], row['stock'], row['id'])
        prints.append(print)
    return prints



