Side_1  = int(input("Enter the value of Side 1"))
Side_2  = int(input("Enter the value of Side 2"))
Side_3  = int(input("Enter the value of Side 3"))
if Side_1 == Side_2 and Side_3 == Side_2:
    print("Traingle is Equilateral")
elif Side_1 == Side_2 or Side_1 == Side_3 or Side_2 == Side_3:
    print("Triangle is Isosceles")
else :
    print("Triangle is Scalen")
