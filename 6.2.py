month_season = int(input("Enter the number of season: "))
if 3< month_season <6 :
    print("Spring")
elif 6<= month_season <9 :
    print("Summer")
elif 9<= month_season <12 :
    print("Autumn")
elif month_season == 12 or month_season == 1 or month_season == 2 :
    print("Winter")
else:
    print("Enter the month which you like the most")