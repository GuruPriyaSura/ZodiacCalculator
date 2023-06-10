Name = input('Enter your name: ')
Day = int(input('Enter your Birth day: '))
Month = input('Enter your Birth Month: ')
if (21 <= Day <= 31 and Month == "March") or (1 <= Day <= 19 and Month == "April"):
    print("You are an Aries!")
elif(20 <= Day <= 31 and Month == "April") or (1 <= Day <= 20 and Month == "May"):
    print("You are a Taurus!")
elif (21 <= Day <= 31 and Month == "May") or (1 <= Day <= 20 and Month == "June"):
    print("You are a Gemini!")
elif (21 <= Day <= 31 and Month == "June") or (1 <= Day <= 22 and Month == "July"):
    print("You are a Cancer!")
elif (23 <= Day <= 31 and Month == "July") or (1 <= Day <= 22 and Month == "August"):
    print("You are a Leo!")
elif (23 <= Day <= 31 and Month == "August") or (1 <= Day <= 22 and Month == "September"):
    print("You are a Virgo!")
elif (23 <= Day <= 31 and Month == "September") or (1 <= Day <= 22 and Month == "October"):
    print("You are a Libra!")
elif (23 <= Day <= 31 and Month == "October") or (1 <= Day <= 21 and Month == "November"):
    print("You are a Scorpio!")
elif (22 <= Day <= 31 and Month == "November") or (1 <= Day <= 21 and Month == "December"):
    print("You are a Sagittarius!")
elif (22 <= Day <= 31 and Month == "December") or (1 <= Day <= 19 and Month == "January"):
    print("You are a Capricorn!")
elif (20 <= Day <= 31 and Month == "January") or (1 <= Day <= 18 and Month == "February"):
    print("You are a Aquarius!")
elif (19 <= Day <= 29 and Month == "February") or (1 <= Day <= 20 and Month == "March"):
    print("You are a Pisces!")
else:
    print("Girl,I dont know")
