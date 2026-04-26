# multi = 3

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(f"{i} * {multi} = {i * multi}")


# reverse 

# name = "om choudhary"
# reversedStr = ""

# for char in name:
#     reversedStr = char + reversedStr

# print(reversedStr)


# strName =  "shambhavi shree" 

# for char in strName:
#     if strName.count(char) == 1:
#         print("Char is :", char)
#         break
    
# number = 5
# fac = 1

# for num in range(1,number+1):
#     fac = fac * num
# print(fac)

# while number > 0 :
#     fac = fac * number 
#     number = number - 1 
#     print(fac)


# while True:
#     number = int(input("enter the number: ")) 
#     if number <= 10:
#         print("thanks")
#     else:
#         print("invalid num")


# items = ["apple" , "banana" , "orange", "apple", "mango"]

# for i in items:
#     if items.count(i) == 2:
#         print(i)

# cname = ["mohan", "alina", "anshu", "supriya"] 
# amount = [10,20,40,50] 

# for item in zip(cname,amount):
#     print(item)

# value = 10 

# if(remainder := value % 3):
#     print(remainder)

# row = 5

# for i in range(1,row-1):
#     print(i*"*")


# users = [
#     {"id": 1,
#      "total": 200,
#      "coupen": "F10"
#     },
#     {"id": 2,
#      "total": 400,
#      "coupen": "P10"
#     },
#     {"id": 2,
#      "total": 500,
#      "coupen": "D10"
#     }
# ]

# discounts = {
#     "F10": (0.2,0),
#     "P10": (0.3,0),
#     "D10": (0,10)
# }

# for user in users:
    
#     persentage , fixed = discounts.get(user["coupen"],(0,0)) 
#     discount = user["total"] * persentage + fixed 
#     print(f"{user["id"]} paid {user["total"]} and got discount for next visit of rupee {discount}")

# functions 

# def print_order(name,chai_type):
#     print(f"{chai_type} order sucessfull! for {name}")

# print_order("om", "masala chai")



# def fetch_sales():
#     print("sales are fetched")

# def filterValidOrder():
#     print("filterd valid order is fetched")

# def Summarized_data():
#     print("Summarized data is fetched")

# def generate_report():
#     print("report genrated: ")
#     fetch_sales()
#     filterValidOrder()
#     Summarized_data()


# generate_report()


# def calculate_bill(cups, price_per_cup):
#     total_cost_of_chai = cups * price_per_cup
#     return f"your total bill is {total_cost_of_chai}    "


# print(calculate_bill(5,10))
# print(calculate_bill(4,10))

# def add_vat(price,vat_rate):
#     total = (price * 2)/100
#     finalCost = total + price
#     print(f"after adding {vat_rate}% of vat the total cost is : {finalCost}") 

# orders = [499,299,599]

# for amount in orders:
#     add_vat(amount,2)

# scopes 

# def father():
#     name = "rohan"
#     def son():
#         nonlocal name
#         name = "mohit"
#         print(name)
#     son()
#     print("after updating the val: ", name)

# father()

# num = 10 
# def func():
#     global num
#     num = 20 
#     print(num)

# func()


# def stu_data(name,age,city):
#     print(f"name is {name}, age is {age}, city is {city}")

# stu_data(name="om",age=20,city="delhi") # keywords

# def stu_data(*stu_details , **parents_details):
#     print("stu_details: ",stu_details)
#     print("parents_details: ",parents_details)

# stu_data("om",20,"delhi",father="rohan",mother="rohan")

# def add(order=[]):
#     order.append("om")
#     print(order)

# add()
# add()
# add()

# def add(order=None):
#     if order is None:
#         order = []
#     order.append("om")
#     print(order)

# add()
# add()
# add()

# pure vs impure 

# def pure_price(price):
#     gst = 10
#     total = price + gst
#     return total

# print(pure_price(100))

# price = 150
# def impure_price():
#     gst = 10 
#     global price
#     price = price + gst 
#     return price    

# print(impure_price())
# print(price)

# recursive function

# def recu(n):
#     print(n)
#     if n == 0 or n==1:
#         return 1
#     else:
#         return n * recu(n-1)
    

# result = recu(5) 
# print(result)

# lambdas

# degree_type = ["primiry", "middle", "matric", "interdimiate", "graduation"]

# result = list(filter(lambda degree: degree!="primiry", degree_type))
# print(result) ;


# comprehentions 
# - list

# Student_name = [
#     "om choudhary",
#     "anshu choudhary",
#     "rupesh jha",
#     "ankan"
# ]

# # for item in Student_name:
# #     if "choudhary" in item:
# #         print(item)

# result = [stu for stu in Student_name if "choudhary" in stu]
# print(result)

# - set comprehention 

# fav_fruits = ["apple", "banana", "orange", "apple", "mango"]

# result = {fruit for fruit in fav_fruits if fruit == "apple"}
# print(result)     
# 
# 
# students = {
#     "class-9th": ["om", "anshu", "rupesh"],
#     "class-10th": ["om", "hari", "ani"],
#     "class-11th": ["om", "hari", "ani"],
#     "class-12th": ["kartik", "anshu", "ani"]
# }                                                  

# unique_stu = {name for batch in students.values() for name in batch}
# print(unique_stu)

# dict comprehention 

# price = {
#     "mango": 100,
#     "banana": 200,
#     "orange": 300,
#     "apple": 400,
#     "grapes": 500
# }

# result = {key: value for key, value in price.items() if value > 200}
# print(result)

# generator comprehention

# def name_gen():
#     yield "om choudhary"
#     yield "anshu"
#     yield "Rohan"
#     yield "mohan"


# name = name_gen()
# print(name)

# print(next(name))
# for name in name_gen():
#     print(name)

# infinte generator 

# def infinate_gen():
#     count = 1
#     while True:
#         yield f"refill the {count}"
#         count += 1

# refill = infinate_gen()

# for __ in range(5):
#     print(next(refill))

# send the val to generators 

# def NameStu():
#     print("welcome to admission management sys")
#     result = yield
#     while True:
#         print(f"ADDMISSON DONE: {result}")
#         result = yield


# result = NameStu()
# next(result)

# result.send("om choudhary")

# yeild from and close

# def localPerson():
#     yield "hari"
#     yield "om"

# def importedPerson():
#     yield "sanju"
#     yield "samson"

# def allPerson():
#     yield from localPerson()
#     yield from importedPerson()

# for person in allPerson():
#     print(person)

# close 
# def order():
#     try:
#         while True:
#             result = yield "wating for order"   
#     except:
#         print("store is closed now.....")

# data = order()
# print(next(data))

# data.close() #clean up memory

# decorator 

# from functools import wraps 
# def my_decoretor(func):
#     @wraps(func) 
#     def wrapper():
#         print("before the function run")
#         func()
#         print("after the function run")
#     return wrapper


# @my_decoretor 
# def hello():
#     print("hello world")

# hello()
# print(hello.__name__)

# build a logger with decoder 

# from functools import wraps

# def log_activity(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         print(f"sending order to {func.__name__}")
#         result = func(*args,**kwargs)
#         print(f"preparing your order {func.__name__}")
#         print(f"deliver order from {func.__name__}")
#         return result
#     return wrapper

# @log_activity
# def store(chai_type, price):
#     print(f"{chai_type} is ready! {price}₹")

# store("Masala Chai", 20)

# auth_decorator 

# from functools import wraps

# def requre_admin(func):
#     @wraps(func)
#     def wrapper(user_role):
#         if user_role != "admin":
#             print("access denied: Admin only")
#             return None # optional but important
#         else:
#             return func(user_role)
#     return wrapper


# @requre_admin
# def login(auth):
#     print("access granted to admin")

# login("admin")
# login("user")