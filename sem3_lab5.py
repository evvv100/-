import sqlite3
import random
from datetime import datetime
from collections import Counter

class MarketplaceDB:
    """Класс для управления магазином"""
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("PRAGMA table_info(Users);")
        tuple1 = self.cursor.fetchall()
        columns1 = []
        for tup in tuple1:
            columns1.append(tup[1])
        self.fill_data("Users", columns1[1:], self.generate_1000_users())
        self.cursor.execute("PRAGMA table_info(Goods);")
        tuple1 = self.cursor.fetchall()
        columns1 = []
        for tup in tuple1:
            columns1.append(tup[1])
        self.fill_data("Goods", columns1[1:], self.generate_1000_goods())
    def fill_data(self, table_name, columns, data_list):
        """Метод для заполнения таблицы в базе данных"""
        query = "SELECT COUNT(*) FROM " + table_name
        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]
        if count > 0:
            return
        columns_str = ", ".join(columns)
        placeholders = ", ".join(["?"] * len(columns))
        sql_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders});"
        self.cursor.executemany(sql_query, tuple(data_list))
        self.connection.commit()

    def generate_1000_users(self):
        """Метод для генерации случайных 1000 пользователей. Возвращает список типа (str)"""
        list = []
        for i in range(1000):
            login = "user" + str(i + 1)
            list.append((login,))
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
        query_id = "SELECT ID FROM Users WHERE Login = ?"
        self.cursor.execute(query_id, (login,))
        rows = self.cursor.fetchall()
        if not rows:
            return False
        user_id = rows[0][0]
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_query = "INSERT INTO Orders (User_ID, Date) VALUES (?, ?)"
        self.cursor.execute(sql_query, (user_id, current_date))
        new_order_id = self.cursor.lastrowid
        query_orders = "INSERT INTO Order_rows (Order_ID, Good_ID, Quantity) VALUES (?, ?, ?)"
        query_id_goods = "SELECT ID FROM Goods WHERE Name = ?"
        ids = []
        for i in range(len(goods_list)):
            self.cursor.execute(query_id_goods, (goods_list[i],))
            row = self.cursor.fetchone()
            if row:
                ids.append(row)
        if not ids:
            return False
        goods_counts = Counter(ids)
        my_goods = []
        for good_id, count in goods_counts.items():
            my_goods.append((new_order_id, good_id[0], count))
        if not my_goods:
            return False
        self.cursor.executemany(query_orders, my_goods)
        self.connection.commit()
        return True

class ConsoleInterface:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    def start_console(self):
        while True:
            self.print_users(self.db_manager.get_20_random_users())
            print()
            self.print_goods(self.db_manager.get_20_random_goods())
            print()
            while True:
                choice = input(
                    "Введите логин пользователя и список товаров (пример: -user user1 -order товар1 товар2 товар1): ")
                if not choice:
                    print("Ввод пуст, попробуйте снова!")
                else:
                    list1 = choice.split()
                    if len(list1) >= 4:
                        if list1[0] == "-user" and list1[2] == "-order":
                            login = list1[1]
                            goods = []
                            for i in range(3, len(list1)):
                                goods.append(list1[i])
                            if not goods:
                                print("Список пустой, попробуйте ввести список товаров!")
                            else:
                                break
                        else:
                            print("Ввод неверный, попробуйте снова!")
                    else:
                        print("Неверный ввод, попробуйте снова!")
            #
            bb = self.db_manager.create_order(login, goods)
            if bb:
                print("Ваш заказ успешно создан!")
            else:
                print("К сожалению, заказ не был создан.")
            break

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


if __name__ == "__main__":
    db = MarketplaceDB(r"C:\ОСНОВА\КСП_База_Данных\CSP.db")
    app = ConsoleInterface(db)
    app.start_console()