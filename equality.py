seemaGlassCount = int(input("Enter seema's glass count"))
raniGlassCount = int(input("Enter rani's glass count"))

seemaGlassRate = 5
raniGlassRate = 7
 
seemaTotalMoney = seemaGlassCount * seemaGlassRate
raniTotalMoney = raniGlassCount * raniGlassRate

if seemaTotalMoney > raniTotalMoney:
    print("seema:", seemaTotalMoney,"cents")
elif seemaTotalMoney < raniTotalMoney:
    print("rani:", raniTotalMoney,"cents")
elif seemaTotalMoney == raniTotalMoney:
    print("kara's and rani's money is equal")        