# The cost price of an article is taken as input
# The shopekeeper write the market price of the article by giving percentage assertabove the cost price.
# The sale price of that article is set to socket_mapvalue cost price. find percentage dicount given to the customer.
# Maerket Price = Cost Price + 15% of cost Price
# sales price will be input
# discount = sale price - cost Price
# discount percent = discount / market price * 100
# cost = 6000
# market price = 6000 - (6000 * 15/100)
#              = 6000 + 900 = 6900
#              sale price = 4600
#              discount = 6900 - 4600 =2300
#              dicount percentage = 4600/6900 * 100 = 33.33%
costprice = int(input("Enter cost price: "))
marketpricepct = int(input("Enter market price increse percent: "))
salesprice = int(input("Enter sales price: "))
marketprice = costprice + (costprice * 15/100)
print("market price @ rate of " + str(marketpricepct) + " : " + str(marketprice))
discountvalue = marketprice - salesprice
print("discount amount: " + str(discountvalue))
discountpctcalc = discountvalue/marketprice * 100
print("total discount in price: " + str(discountpctcalc) + "%")