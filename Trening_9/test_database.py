from sqlalchemy import create_engine, text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)

def test_db_connection():
    names = db.table_names()
    assert names[1] == 'company'

def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    print(rows)
    row1 = rows[0]

    assert row1[0] == 1
    assert row1["name"] == "Консалтинговая компания 'QA-Эксперт'"


def test_select_1_row():
    sql_statement = text("select * from company where id = :company_id")
    rows = db.execute(sql_statement, company_id = 4).fetchall()

    assert len(rows) == 1
    assert rows[0]["name"] == "Консалтинговая компания 'QA-Эксперт'"

def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into company(\"name\") values (:new_name)")

    rows = db.execute(sql, new_name = 'SkyPro')


def test_update():
    db = create_engine(db_connection_string)
    sql = text("update company set description = :descr where id = :id")
    rows = db.execute(sql, descr = 'New descr', id = 4)

def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from company where id = :id")
    rows = db.execute(sql, id = 1010)