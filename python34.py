def pa():
    print("***************************")

def showHeader():
    pa()
    print("***     BMI Program     ***")
    pa()

def nAndy():
    n = input("ป้อนชื่อ : ")
    y = int(input("ป้อนปี พ.ศ. เกิด : "))
    x = 2568 - y
    return n,y,x

def wAndh():
    w = float(input("ป้อนน้ำหนัก :  "))
    print(f"\033[1A\033[2kป้อนน้ำหนัก: {w} กิโลกรัม")
    h = float(input("ป้อนส่วนสูง :  "))
    print(f"\033[1A\033[2kป้อนส่วนสูง: {h} เซนติเมตร")
    pa()
    return w,h

def cal():
     w,h = wAndh()
     bmi = (w /(( h / 100 ) ** 2))
     return bmi,w,h

def show():
     n,y,x = nAndy()
     bmi,w,h = cal()
     print(f"คุณ{n} เกิดปี พ.ศ. {y} อายุ {x} ปี")
     print(f"น้ำหนัก {w} กิโลกรัม ส่วนสูง {h} เซนติเมตร")
     print(f"ค่า BMI ที่คำนวณได้ คือ {bmi:,.2f}")
     if bmi >= 40 :
         print("แปลค่า BMI ที่คำนวณได้ คือ น้ำหนักเกิน (อ้วนระดับรุนแรงมาก)")
     elif bmi >= 30 :
         print("แปลค่า BMI ที่คำนวณได้ คือ น้ำหนักเกิน (อ้วนมาก)")
     elif bmi >= 25 :
         print("แปลค่า BMI ที่คำนวณได้ คือ น้ำหนักเกิน (อ้วนระยะเริ่มต้น)")
     elif bmi >= 23 :
         print("แปลค่า BMI ที่คำนวณได้ คือ น้ำหนักเกิน (ท้วม)")
     elif bmi >= 18.5 :
         print("แปลค่า BMI ที่คำนวณได้ คือ น้ำหนักปกติ")
     else :
         print("แปลค่า BMI ที่คำนวณได้ คือ น้ำหนักน้อยไป")
     pa()

showHeader()
show()