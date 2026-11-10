import sqlite3
import random
from datetime import datetime

class MarketplaceDB:
    """Класс для управления магазином"""
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")

    def fill_data(self, table_name, columns, data_list):
        """Метод для заполнения таблицы в базе данных"""
        if self.cursor.fetchall() is None:
            return
        columns_str = ", ".join(columns)
        placeholders = ", ".join(["?"] * len(columns))
        sql_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders});"
        self.cursor.executemany(sql_query, data_list)
        self.connection.commit()

    def generate_1000_users(self):
        """Метод для генерации случайных 1000 пользователей. Возвращает список типа (str)"""
        list = []
        for i in range(1000):
            login = ""
            for j in range(6):
                num = random.randint(0, 2)
                if num == 0:
                    kod = chr(random.randint(65, 90))
                elif num == 1:
                    kod = chr(random.randint(97, 122))
                else:
                    kod = random.randint(0,9)
                login+=str(kod)
            list.append(login)
        return list

    def generate_1000_goods(self):
        """Метод для генерации 1000 товаров. Возвращает список типа ((str, int))"""
        list = []
        for i in range(1000):
            name = "Товар"+str(i+1)
            price = random.randint(100, 1000)
            list.append((name, price))
        return list

    def get_20_random_users(self):
        sql_query = "SELECT ID, Login FROM Users ORDER BY RANDOM() LIMIT 20;"
        self.cursor.execute(sql_query)
        return self.cursor.fetchall()

    def get_20_random_goods(self):
        sql_query = "SELECT ID, Name, Price FROM Goods ORDER BY RANDOM() LIMIT 20;"
        self.cursor.execute(sql_query)
        return self.cursor.fetchall()

    def create_order(self, login, goods_list):
        pass

class ConsoleInterface:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    def start_console(self):
        pass
    def print_users(self, user_list):
        if user_list is None:
            return
        print("ID\tLogin")
        print("-"*20)
        for user in user_list:
            user_id, login = user
            print(f"{user_id}\t{login}")

    def print_goods(self, good_list):
        if good_list is None:
            return
        print("ID\tName\tPrice")
        print("-" * 25)
        for good in good_list:
            good_id, name, price = good
            print(f"{good_id}\t{name}\t{price}")

