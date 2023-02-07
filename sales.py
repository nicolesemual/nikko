name = input ("Please Enter Your Name : ")
greeting = "Hello" + " " + name
print(greeting)
price = float(input("Please Enter Your Price = RM "))
tax = float(input("Please Enter Your Tax % = "))
#sales amount = total sales + sales tax
sales_tax = (price * (tax/100))
Total_Amount_To_Pay = price + sales_tax
print("Total = "+ str(Total_Amount_To_Pay) )