# มี parameter ไม่มี return
# parameter ถือเป็นตัวแปรประเภทหนึ่ง ใช้ได้ในฟังก์ชันนั้นเท่านั้น


def sumNumber(aa,bb) :
    print(f"ผลรวมของ {aa} และ {bb} เท่ากับ {aa + bb}")
    print("ok นะจ้ะ ^_^")

def avarageNumber(n1,n2,n3,n4) :
    print(f"ค่าเฉลี่ยของเลข {n1}, {n2}, {n3}, {n4} คือ {(n1 + n2 + n3 + n4) / 4}")
   
sumNumber(10, 20 ) # ข้อมูลที่ส่งให้ พารามิเตอร์ เรียก Argument
sumNumber(100, 200 )
avarageNumber(10, 20, 30 , 40 )
