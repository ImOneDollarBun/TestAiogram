import aiosqlite as aio


class DataBase:
    def __init__(self, db_url):
        self.url = db_url

    async def create_db(self):
        async with aio.connect(self.url) as conn:
            cursor = await conn.cursor()
            await cursor.execute('''
                CREATE TABLE IF NOT EXISTS zuzu (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    url TEXT,
                    xpath TEXT
                )
            ''')

    async def add_data(self, title, url, xpath):
        async with aio.connect(self.url) as conn:
            cursor = await conn.cursor()
            await cursor.execute("INSERT INTO zuzu (title, url, xpath) VALUES (?, ?, ?)",
                                 (title, url, xpath))
            await conn.commit()
