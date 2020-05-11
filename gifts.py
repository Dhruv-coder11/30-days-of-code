sweaterPrice = 68
sweaterCount = 3
computerGamePrice = 75
computerGameCount = 1
braceletPrice = 43
braceletCount = 2

#discount And Rebate
returnBraceletCount = 1
rebateOnComputerGame = 10

# calculation part

totalGiftPrice = (sweaterPrice * sweaterCount) + (computerGamePrice * computerGameCount)
discountAndRebate = (braceletPrice * returnBraceletCount) + rebateOnComputerGame

finalGiftPrice = totalGiftPrice - discountAndRebate

print("final gift price is", finalGiftPrice)