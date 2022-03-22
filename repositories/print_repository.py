from db.run_sql import run_sql
from models.artist import Artist
from models.print import Print 
import repositories.artist_repository as artist_repository 

def save(print):
    sql = "INSERT INTO prints (title, artist_id, size, price, printing_cost, stock, image_print_pathway) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [print.title, print.artist.id, print.size, print.price, print.printing_cost, print.stock, print.image_print_pathway]
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
        print = Print(row['title'], artist, row['size'], row['price'], row['printing_cost'], row['stock'], row['image_print_pathway'], row['id'])
        prints.append(print)
    return prints 

def select(id):
    print = None
    sql = "SELECT * FROM prints WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        print = Print(result['title'], artist, result['size'], result['price'], result['printing_cost'], result['stock'], result['image_print_pathway'], result['id'])
    return print

def delete_all():
    sql = "DELETE FROM prints"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM prints WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(print):
    sql = "UPDATE prints SET (title, artist_id, size, price, printing_cost, stock, image_print_pathway) = (%s, %s, %s, %s, %s, %s,%s) WHERE id = %s"
    values = [print.title, print.artist.id, print.size, print.price, print.printing_cost, print.stock, print.image_print_pathway, print.id]
    run_sql(sql, values)




