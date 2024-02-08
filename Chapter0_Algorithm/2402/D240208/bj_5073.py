result = []

while(1):
    xyz = list(map(int, input().split(" ")))
    if(sum(xyz)==0) :
        break

    xyz.sort()

    if(xyz[2] >= xyz[0]+xyz[1]) :
        #print("Invalid")
        result.append("Invalid")
    else :
        xyz_set = list(set(xyz))
        n = len(xyz_set)
        # if(xyz[2] == xyz[0] == xyz[1]) :
        #     print("Equilateral")
        if(n==1) :
            #print("Equilateral")
            result.append("Equilateral")
        elif(n==2) :
            #print("Isosceles")
            result.append("Isosceles")
        else :
            #print("Scalene")
            result.append("Scalene")

print("\n".join(result))