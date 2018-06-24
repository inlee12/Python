d=int(input())
days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY", "SUNDAY"]
if ( d >= 1 ) & ( d <= 7 ) :
    print(days[d-1])
else:
    print("input error")
