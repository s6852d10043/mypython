# เขียนโปรแกรมคำนวณพื้นที่วงกลม และเส้นรอบวงกลม โดยรับค่ารัศมีทางแป้นพิมพ์ แล้วแสดงผลพื้นที่และเส้นรอบวงกลมที่คำนวณได้ทางหน้าจอ

# แสดงชื่อโปรแกรม
# รับค่ารัศมี
# คำนวนพื้นที่
# คำนวณเส้นรอบวง
# แสดงผล พื้นที่ และเส้นรอบวง

def showProgramName() :
    print("+++++++++++++++++++++++++++++++")
    print(" Calucator of Circle ")
    print("+++++++++++++++++++++++++++++++")

def inputRadius() :
    radius = float(input("ป้อนรัศมี : "))
    return radius

def calArea( r ) :
    return 3.1416 * r * r

def calLine( r ) :
    return 2 * 3.1416 * r

def showAareAndLine(area,line) :
    print(f"พื้นที่วงกลม : {area:,.2f}")
    print(f"เส้นรอบวงกลม : {line:,.2f}")

showProgramName()
r = inputRadius()
print("+++++++++++++++++++++++++++++++")
area = calArea( r )
line = calLine( r )
showAareAndLine(area,line)
print("+++++++++++++++++++++++++++++++")
showAareAndLine(calArea(r),calLine(r))
print("+++++++++++++++++++++++++++++++")