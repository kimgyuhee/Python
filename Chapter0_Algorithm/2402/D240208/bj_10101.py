
tri = []
x = int(input())
y = int(input())
z = int(input())

tri.append(x)
tri.append(y)
tri.append(z)

set_tri = list(set(tri))

# print(set_tri)

# if (set_tri[0]==60 and len(set_tri)==1) :
#     print("Equilateral")
# elif(len(set_tri) == 2) :
#     print("Isosceles")
# else :
#     if(sum(set_tri)==180) :
#         print("Scalene")
#     else :
#         print("Error")

# if(sum(set_tri)>180 or len(set_tri)==3) :
#     if(sum(set_tri)==180) :
#         print("Scalene")
#     else :
#         print("Error")
# elif(len(set_tri) == 2) :
#     print("Isosceles")
# else :
#    print("Equilateral") 

if(x+y+z == 180) :
    if (set_tri[0]==60 and len(set_tri)==1) :
        print("Equilateral")
    elif(len(set_tri) == 2) :
        print("Isosceles")
    else :
        print("Scalene")
else :
    print("Error")