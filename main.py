# 1-misol
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}, summa balansga qo'shildi")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} summa balansdan yechildi")

    def info(self):
        print(f"egasi: {self.owner}, balance: {self.balance}")


u1 = BankAccount("Ali", 100000)
u1.info()

u1.deposit(70000)
u1.info()

u1.withdraw(20000)
u1.info()

# 2-misol
class OnlineShop:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        res = self.price * self.quantity
        print(f"Jami: {res} so'm")
        return res

    def apply_discount(self, percent):
        res = self.total_price()
        discounted = res * (1 - percent / 100)
        print(f"Chegirmadan keyin: {int(discounted)} so'm")
        return discounted


# Misol uchun ishlatish:
p = OnlineShop("Olma", 10000, 3)
p.total_price()
p.apply_discount(10)


# 3-misol
class StudentGrade:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def check_pass(self):
        if self.grade >= 60:
            print(f"{self.name} o'tdi")

        else:
            print(f"{self.name} yiqildi")


    def info(self):
        print(f"{self.check_pass()}")

s1 = StudentGrade("Ali", 61)
s1.info()


# 4-misol
class Carfuel:
    def __init__(self, model, fuel):
        self.model = model
        self.fuel = fuel

    def drive(self, km):
        self.fuel -= km
        print(f"{km} km yurildi, yoqilg‘i: {self.fuel}L")

    def refuel(self, amount):
        self.fuel += amount
        print(f"Yoqilg‘i to‘ldirildi: {self.fuel}L")


# Misol:
c = Carfuel("Chevrolet", 30)
c.drive(10)
c.refuel(10)


# 5-misol
class PasswordManager:
    def __init__(self, password):
        self.password = password

    def check_strength(self):
        if len(self.password) >= 6:
           print(f"Kuchli parol")
        else:
            print(f"Zaif parol")

    def change(self, new_password):
        self.password = new_password

p1 = PasswordManager("12345678")
p1.check_strength()
p1.change("87654321")

# 6-misol
class LibraryBook:
    def __init__(self, title, is_available):
        self.title = title
        self.is_available = is_available

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"Kitob olindi")
        else:
            print(f"band")

    def return_book(self):
        self.is_available = True
        print(f"Kitob qaytarildi")

l1 = LibraryBook("Pyhton", True)
l1.borrow()
l1.return_book()

# 7-misol
class FoodOrder:
    def __init__(self, food, price, is_delivered):
        self.food = food
        self.price = price
        self.is_delivered = is_delivered

    def deliver(self):
        self.is_delivered = True
        print(f"Buyurtma yetkazildi")

    def status(self):
        if self.is_delivered:
            print(f"Buyurtma yetkazildi")
        else:
            print(f"Hali yetgazilmadi")


f1 = FoodOrder("pizza", 45000, True)
f1.status()
f1.deliver()

# 8-misol
class UserLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, input_password):
        if self.password == input_password:
            print(f"xush kelibsiz")
        else:
            print(f"Parol xato")

u1 = UserLogin("Ali", "abcd")
u1.login("abdc")

# 9-misol
class PhoneBattery:
    def __init__(self, percent):
        self.percent = percent

    def use(self, amount):
        self.percent -= amount
        if self.percent <= 0:
            print("Quvvat tugadi")
        else:
            print(f"Batareya: {self.percent}%")

    def charge(self, amount):
        self.percent += amount
        if self.percent >= 100:
            print(f"Batareya: {self.percent}%")
b1 = PhoneBattery(30)
b1.use()
