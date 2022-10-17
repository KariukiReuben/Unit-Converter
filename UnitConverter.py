num1 = input("Enter the value:")
unit1 = input("Current unit:")
unit2 = input("Unit to convert to:")
if unit1 =="cm" and unit2=="m":
    ans= float(num1)/100
    print(ans, "m")

elif unit1 =="mm" and unit2=="cm":
    ans= float(num1)/10
    print(ans, "cm")

elif unit1 =="m" and unit2=="cm":
    ans= float(num1)*100
    print(ans, "cm")

elif unit1 =="cm" and unit2=="mm":
    ans= float(num1)*10
    print(ans, "mm")

elif unit1 =="mm" and unit2=="m":
    ans= float(num1)/1000
    print(ans, "m")

elif unit1 =="m" and unit2=="mm":
    ans= float(num1)*1000
    print(ans, "mm")

elif unit1 =="km" and unit2=="m":
    ans= float(num1)*1000
    print(ans, "m")

elif unit1 =="km" and unit2=="mm":
    ans= float(num1)*1000
    print(ans, "mm")

elif unit1 =="m" and unit2=="km":
    ans= float(num1)*100000
    print(ans, "km")

elif unit1 =="mm" and unit2=="km":
    ans= float(num1)/100000
    print(ans, "km")

elif unit1 =="ft" and unit2=="cm":
    ans= float(num1)*30.48
    print(ans, "cm")

elif unit1 =="ft" and unit2=="mm":
    ans= float(num1)*304.8
    print(ans, "mm")

elif unit1 =="ft" and unit2=="inch":
    ans= float(num1)*12
    print(ans, "inch")

elif unit1 =="inch" and unit2=="cm":
    ans= float(num1)*2.54
    print(ans, "cm")

elif unit1 =="inch" and unit2=="mm":
    ans= float(num1)*25.4
    print(ans, "mm")

elif unit1 =="cm" and unit2=="inch":
    ans= float(num1)/2.54
    print(ans, "inches")

elif unit1 =="cm" and unit2=="km":
    ans= float(num1)/100000
    print(ans , "KM") 

elif unit1 =="miles" and unit2=="km":
    ans= float(num1)*1.60934
    print(ans , "miles") 

elif unit1 =="km" and unit2=="miles":
    ans= float(num1)/1.60934
    print(ans , "km") 