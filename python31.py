def showProgramName() :
    print("+++++++++++++++++++++++++++++++")
    print(" Calucator of Circle ")
    print("+++++++++++++++++++++++++++++++")

def inputRadius() :
    radius = float(input("ป้อนรัศมี : "))
    return radius

def cal() :
    r = inputRadius()
    area = 3.1416 * r * r
    line = 2 * 3.1416 * r
    return area, line

def show() :
    a,l = cal()
    print("+++++++++++++++++++++++++++++++")
    print(f"พื้นที่วงกลม :{a}")
    print(f"เส้นรอบวงกลม :{l} ")
    print("+++++++++++++++++++++++++++++++")

showProgramName()
show()