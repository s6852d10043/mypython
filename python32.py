# สร้างโปรแรกมเครื่องคำนวณของ 2 จำนวณ ที่รับทางแป้นพิมพ์ ได้แก่ + - * / โดย ทำเป็นเมนูให้ผู้ใช้เลือก
# ผู้ใช้เลือกเมนูไหนให้คำนวณตามเมนูนั้นๆ แล้วแสดงผล

# แสดงชื่อโปรแกรม
# รับค่าตัวเลข 2 จำนวน
# แสดงเมนุให้ผู้ใช้เลือก
# คำนวณตามเมนู 
# แสดงผลลัพธืที่ได้จากการคำนวณ
def printpa():
    print("+++++++++++++++++++++++++++++++")

def showHeader():
    printpa()
    print("         เครื่องคิดเลข")
    printpa()


def showMenu():
    print("1 บวก")
    print("2 ลบ")
    print("3 คูณ")
    print("4 หาร")
    menu = float(input("ป้อนเมนูที่ต้องการคำนวณ : "))
    printpa()
    return menu

def cal():
    menu = showMenu()
    num1 = float(input("ป้อนตัวเลขที่ 1 : "))
    num2 = float(input("ป้อนตัวเลขที่ 2 : "))
    if menu == 1 :
        print(f"{num1} + {num2} = {num1 + num2}")
    elif menu == 2 :
        print(f"{num1} - {num2} = {num1 - num2}")
    elif menu == 3 :
        print(f"{num1} * {num2} = {num1 * num2}")
    elif menu == 4 :
        print(f"{num1} / {num2} = {num1 / num2}")
    else :
        print("คุณเลือกเมนูไม่ถูกต้อง")
    printpa()

showHeader()
cal()
     
