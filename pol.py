thing = (input("what will you be selling (only 1 thing)"))
cost = int(input(f"what is the cost of {thing} "))
sellingprice = int(input (f"at what price will you be selling{thing}"))
if (cost < sellingprice):
 print("it is a profit of ruppees",sellingprice - cost)
else :
 print ("it is loss sell at higher price",cost - sellingprice)

