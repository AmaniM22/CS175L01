#Joe bought 2,000 shares
#each share was $40.00
#commision rate is 0.03
# Joe sold each share for $42.75
# He sold all 2,000 shares
# The amount he recieved, he gave 0.03 of it to his stockbroaker as commission

#asking user to input information
NUM_SHARES= int(input('how many shares did you purchase?: '))
PURCHASE_PRICE=float(input('how much did you pay per stock?: '))
COMMISSION_RATE=float(input('How much was the commission rate?: '))
SELLING_PRICE=float(input('How much did you sell each share for?:'))

#calculations
amountPaidForStock=float(NUM_SHARES*PURCHASE_PRICE)
purchaseCommission=float(COMMISSION_RATE*amountPaidForStock)
totalPaid=float(amountPaidForStock + purchaseCommission)
stockSoldFor=float(NUM_SHARES*SELLING_PRICE)
sellingCommission=float(COMMISSION_RATE*stockSoldFor)
totalRecieved=float(stockSoldFor-sellingCommission)
profitOrLoss= float(totalRecieved-totalPaid)

#display results
print('The amount you paid for the stock is: $', amountPaidForStock)
print('Commission paid on the purchase: $', purchaseCommission)
print('The total amount the stock sold for: $', stockSoldFor)
print('Commission paid on the sale: $', sellingCommission)
print('profit(or loss if negative is: $', profitOrLoss)


