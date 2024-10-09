import sqlite3


class DBManager:
    """Parent class for db connection context manager."""

    def __init__(self):
        self.con = None
        self.cur = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()


class DBManagerMariaDB(DBManager):

    def __init__(self):
        super().__init__()

    def __enter__(self):
        self.con = mariadb.connect(
            user=self.creds["MDB_USER"],
            password=self.creds["MDB_PWD"],
            host=self.creds["MDB_HOST"],
            database=self.creds["MDB_DB"]
        )
        self.cur = self.con.cursor()
        return self


class DBManagerSQLite(DBManager):
    """SQLite db manager: connect to db, execute queries."""

    def __init__(self, db_path, strategy, up_who):
        super().__init__()

    def __enter__(self):
        self.con = sqlite3.connect(self.db_path)
        self.cur = self.con.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.con.execute("VACUUM")
        self.con.close()
