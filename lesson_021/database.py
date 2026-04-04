from pony.orm import Database

db = Database()

def init_db():
    db.bind(
        provider='mysql',
        host='localhost',
        user='root',
        password='',
        database='student_db',
        charset='utf8mb4'
    )
    db.generate_mapping(create_tables=True)