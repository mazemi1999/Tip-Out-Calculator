#Welcome to the VPA claim calculator -Mergim Azemi

weekday=input("Did you work at all mon-thur?")
if weekday=="yes":
    print("How many hours:")
    mon = float(input("Monday:"))
    tue = float(input("Tuesday:"))
    wen = float(input("Wensday:"))
    thur =float(input("Thursday"))

    claimMon= (1.6 * mon)
    claimTue= (1.6 * tue)
    claimWen= (1.6 * wen)
    claimThur= (1.6 * thur)

    print( "You worked "+str(mon)+" hours on Monday, claim "+str(claimMon))
    print( "You worked "+str(tue)+" hours on Tuesday, claim "+str(claimTue))
    print( "You worked "+str(wen)+" hours on Wednesday, claim "+str(claimWen))
    print( "You worked "+str(thur)+" hours on Thursday, claim "+str(claimThur))


  
weekend=input("Did you work on the weekend?")
if weekend=="yes":
    print("How many hours:")
    
    fri = float(input("Friday:"))
    sat = float(input("Saturday:"))
    sun = float(input("Sunday:"))

    claimFri = 2.7 * fri
    claimSat = 2.7 * sat
    claimSun = 2.7 * sun

    print( "You worked "+str(fri)+" hours on Friday, claim "+str(claimFri))
    print( "You worked "+str(sat)+" hours on Saturday, claim "+str(claimSat))
    print( "You worked "+str(sun)+" hours on Sunday, claim "+str(claimSun))

 
    
