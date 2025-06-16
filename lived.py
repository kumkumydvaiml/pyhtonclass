age_years=int(input("Enter your age in years :"))

#calculate seconds in a year (approximate,not counting leap years)
seconds_in_a_year=365*24*60*60

total_seconds = age_years * seconds_in_a_year

#display result
print(f"you have lived approximately{total_seconds:,}seconds in {age_years}years!")