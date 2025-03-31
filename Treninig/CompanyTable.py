from sqlalchemy import create_engine
from sqlalchemy.sql import text

class CompanyTable:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_active_companies(self):
        with self.engine.connect() as connection:
            result = connection.execute("select * from company where \"is_active\" = true and deleted_at is null")
            return result.fetchall()

