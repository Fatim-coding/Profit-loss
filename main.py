costprice =int(input("enter the costprice:"))
sellingprice =int(input("enter the sellingprice:"))

if(sellingprice>costprice):
   print("profit")
   profit=sellingprice-costprice
   print(profit)
else :
    print("no profit")