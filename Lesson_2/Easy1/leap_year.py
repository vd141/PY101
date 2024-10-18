# Leap Years (Part 1)

def is_leap_year(year):
    # if we wanted to account for the year of adoption by country/region, we 
    # could add an additional input for a country/region code
    # we could then add a dictionary that stores the country/region codes as
    # keys mapped to their respective year of adoption
    
    if year >= 1752: # use Gregorian calendar 
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        elif year % 4 == 0:
            return True
        else:
            return False
    else: # use Julian calendar
        return year % 4 == 0
    
# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)