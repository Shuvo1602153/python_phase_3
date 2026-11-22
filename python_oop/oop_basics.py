class Mobile:
    warrenty = "1 Year"
    store ="Tech hub"
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def show_Details(self):
        print(f"Mobile brand = {self.brand} | Price = {self.price} | Warrenty = {self.warrenty} | Store = {self.store}")
    def update_price(self, price):
        if price < 0:
            print("Price cannot be negative.")
            return
        self.price = price

class Smartphone(Mobile):
    def __init__(self, brand, price,ram):
        super().__init__(brand, price)
        self.ram = ram 
    def Show_smaetphone_info(self):
        print(f"Brand name {self.brand} | Price {self.price}BDT | Ram {self.ram}GB")

#m1=Mobile("Samsung" , 50000)
sp1 = Smartphone("Walton",30000,8)
sp1.update_price(25000)
sp1.Show_smaetphone_info()
# m1.show_Details()
# m1.update_price(40000)
# m1.show_Details()


# m2 = Mobile("Waltol", 30000)
# m2.show_Details()


# class Book:
#     def __init__(self,book,author):
#         self.book = book
#         self.author = author

# book1= Book("c++","shuvo")
# print(f"{book1.book } and {book1.author}")
# book2= Book("c#","Ripa")
# print(f"{book2.book } and {book2.author}")