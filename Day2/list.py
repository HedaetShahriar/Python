names=["H","I","M","O","N"]
age=[10,11,12,13,14]

print(names[0]," : ",age[0])
print(names[1]," : ",age[1])
print(names[2]," : ",age[2])
print(names[3]," : ",age[3])
print(names[4]," : ",age[4])

shopingCart=["Apple","Banana","Mango","Jackfruit"]
print("List Total Element: ",len(shopingCart))
#item=input("Enter item name: ")
#shopingCart.append(item)
#item=input("Enter your item: ")
#shopingCart.append(item)
print("Items are: ",shopingCart)
shopingCart.remove("Apple")
print("Items are: ",shopingCart)
shopingCart.pop()
print("Items are: ",shopingCart)
shopingCart.clear()
if len(shopingCart)==0:
    print("List is emty")