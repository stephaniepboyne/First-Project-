from db.run_sql import run_sql
from models.artist import Artist
from models.print import Print 
import repositories.artist_repository as artist_repository 

def save(artist):
    sql = "INSERT INTO prints (title, artist, size, price) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [print.title, print.artist, print.size, print.price, print.printing_cost, print.stock]
    results = run_sql(sql, values)
    id = results[0]['id']
    print.id = id
    return print

def select_all():
    prints = []

    sql = "SELECT * FROM prints"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        print = Print(row['title'], artist, row['size'], row['price'], row['printing_cost'], row['stock'], row['id'])
        prints.append(print)
    return prints 

def delete_all():
    sql = "DELETE FROM prints"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM prints WHERE id = %s"
    values = [id]
    run_sql(sql, values)
