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



def fetch_sales():
    print("sales are fetched")

def filterValidOrder():
    print("filterd valid order is fetched")

def Summarized_data():
    print("Summarized data is fetched")

def generate_report():
    print("report genrated: ")
    fetch_sales()
    filterValidOrder()
    Summarized_data()


generate_report()