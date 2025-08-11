from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://postgres:Rbvfytr2812@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_db_connection():
# Используем инспектор для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'subject'

def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM subject"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['subject_id'] == 1
    assert row1['subject_title'] == "English"

    connection.close()

def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO subject(subject_title) VALUES (:new_subject_title)")
    connection.execute(sql, {"new_subject_title": "Korean"})

    transaction.commit()
    connection.close()

def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE subject SET subject_title WHERE subject_title = ('Korean')")
    connection.execute(sql, {"new_subject_title": "Mongolian"})

    transaction.commit()
    connection.close()

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM subject WHERE subject_title = ('Korean')")
    connection.execute(sql, {"subject_title": 'Korean'})

    transaction.commit()
    connection.close()