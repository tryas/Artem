# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
# и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь.


class Store:
    items = {}

    def push(self, key, value):
        self.items[key] = value
        print(self.items)

        pass


class Company:
    pass


class Department1(Company):
    pass


class Department2(Company):
    pass


class Equipment:
    def __init__(self, brand, model, serial_number):
        self.brand = brand
        self.model = model
        self.serial_number = serial_number


class Printer(Equipment):
    def __init__(self, brand, model, color, serial_number):
        super().__init__(brand, model, serial_number)
        self.color = color

    def print_obj(self):
        print(f'brand: {self.brand}, model:{self.model}, color: {self.color}, serial_number: {self.serial_number}')


class Scaner(Equipment):
    def __init__(self, brand, model, depth_color, serial_number):
        super().__init__(brand, model, serial_number)
        self.depth_color = depth_color


class Xerox(Equipment):
    def __init__(self, brand, model, document_feeder, serial_number):
        super().__init__(brand, model, serial_number)
        self.document_feeder = document_feeder


my_printer = Printer(brand='Epson', serial_number=123456789, color=None, model='FX100')
my_printer2 = Printer(brand='Canon', serial_number=None, color=True, model='R800')
print(my_printer, my_printer.brand, my_printer.model, my_printer.color, my_printer.serial_number)

my_scaner = Scaner('Canon', 'HG-18', 32, 987654321)
print(my_scaner, my_scaner.brand, my_scaner.model, my_scaner.depth_color, my_scaner.serial_number)

my_xerox = Xerox('Xerox', 'RT-19', True, 123498765)
print(my_xerox, my_xerox.brand, my_xerox.model, my_xerox.document_feeder, my_xerox.serial_number)

my_store = Store()
my_store.push(my_printer, 1)
my_store.push(my_printer2, 1)

my_printer.print_obj()
my_printer2.print_obj()