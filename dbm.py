import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.close()

    def create_table(self, table_name, schema):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})"
        self.cursor.execute(query)
        self.conn.commit()

    def drop_table(self, table_name):
        query = f"DROP TABLE IF EXISTS {table_name}"
        self.cursor.execute(query)
        self.conn.commit()

    def insert_record(self, table_name, record):
        placeholders = ', '.join(['?'] * len(record))
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.cursor.execute(query, record)
        self.conn.commit()

    def update_record(self, table_name, record_id, updates):
        set_clause = ', '.join([f"{col} = ?" for col in updates.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE id = ?"
        self.cursor.execute(query, list(updates.values()) + [record_id])
        self.conn.commit()

    def delete_record(self, table_name, record_id):
        query = f"DELETE FROM {table_name} WHERE id = ?"
        self.cursor.execute(query, (record_id,))
        self.conn.commit()

    def get_record(self, table_name, record_id):
        query = f"SELECT * FROM {table_name} WHERE id = ?"
        self.cursor.execute(query, (record_id,))
        return self.cursor.fetchone()

    def get_all_records(self, table_name):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.conn.commit()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    def begin_transaction(self):
        self.conn.execute('BEGIN TRANSACTION')

    def commit_transaction(self):
        self.conn.commit()

    def rollback_transaction(self):
        self.conn.rollback()

    def table_exists(self, table_name):
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
        self.cursor.execute(query)
        return self.cursor.fetchone() is not None

    def get_last_insert_id(self):
        return self.cursor.lastrowid
