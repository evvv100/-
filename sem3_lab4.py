from abc import ABC, abstractmethod
import argparse

class Order:
    def __init__(self, x):
        self.number = x

class User(ABC):
    def __init__(self,  lastname, firstname, telephone, address):
        self.firstname = firstname
        self.lastname = lastname
        self.telephone = telephone
        self.address = address

    @abstractmethod
    def create(self):
        pass

class Employee(User):
    def __init__(self, lastname, firstname,  telephone, address,  position, salary):
        super().__init__(lastname, firstname, telephone, address)
        self.position = position
        self.salary = salary
    def create(self):
        data = {
            "lastname": self.lastname,
            "firstname": self.firstname,
            "telephone": self.telephone,
            "address": self.address,
            "position": self.position,
            "salary": self.salary,
        }
        with open("users.txt", "a", encoding ="utf-8") as file:
            file.write(str(data) + "\n")
        print(f"Сотрудник {self.firstname} {self.lastname} успешно сохранен.")

class Client(User):
    def __init__(self,lastname, firstname,  telephone, address, order: Order):
        super().__init__(lastname, firstname,  telephone, address)
        self.order = order
    def create(self):
        data = {
            "lastname": self.lastname,
            "firstname": self.firstname,
            "telephone": self.telephone,
            "address": self.address,
            "order": self.order.number}
        with open("users.txt", "a", encoding ="utf-8") as file:
            file.write(str(data) + "\n")
        print(f"Клиент {self.lastname} успешно сохранен.")

class CArgparse:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description = "Модуль создания пользователей")
        self._configure_arguments()
    def _configure_arguments(self):
        self.parser.add_argument("-mode", choices=["auto", "handle"], default="auto", help="auto - автоматический, handle - ручной ввод")
        self.parser.add_argument("-lastname", help ="Фамилия")
        self.parser.add_argument("-firstname", help = "Имя")
        self.parser.add_argument("-telephone", help="Телефон")
        self.parser.add_argument("-address", help = "Адрес")
        self.parser.add_argument("-position", default = "инженер", help = "Должность сотрудника")
        self.parser.add_argument("-salary", type = int, default=0, help = "Зарплата сотрудника (число)")
        self.parser.add_argument("-order", help = "Номер заказа клиента (Пример: Order-123)")

    def parse(self):
        args = self.parser.parse_args()
        if args.mode == "handle":
            missing = []
            for n in ("lastname", "firstname", "telephone", "address"):
                if not getattr(args, n):
                    missing.append(n)
            if missing:
                self.parser.error("в режиме handle обязательны: " + ", ".join(missing))
        return args

class CScenario:

    @staticmethod
    def run(args):
        if args.mode == "auto":
            print("Выполняется сценарий: автоматический (auto)")
            Employee("Иванов", "Иван", "+79456541278",
                     "Красноярск, ул. Ак. Киренского, 26 к1", "инженер", 123).create()
            Client("Петров", "Петр", "+79457652389",
                   "Красноярск, пр. Свободный, 79", Order("Order-123")).create()
        else:
            print("Выполняется сценарий: ручной ввод (handle)")
            if args.order is None:
                user = Employee(
                    lastname=args.lastname,
                    firstname=args.firstname,
                    telephone=args.telephone,
                    address=args.address,
                    position=args.position,
                    salary=args.salary,
                )
                user.create()

            else:
                if not args.order:
                    print(
                        "Ошибка: Для создания клиента необходимо указать номер заказа через параметр --order"
                    )
                    return
                order_object = Order(args.order)
                user = Client(
                    lastname=args.lastname,
                    firstname=args.firstname,
                    telephone=args.telephone,
                    address=args.address,
                    order=order_object,
                )
                user.create()


def main():
    arg_parser = CArgparse()
    parsed_args = arg_parser.parse()
    CScenario.run(parsed_args)


if __name__ == "__main__":
    main()