# ไม่มี parameter มี return
# มี return คือ มีคำสั่ง return ในตัวฟังก์ชันและมีข้อมูลส่งกลับไปที่จุดเรียกใช้

def funcWow() :
    return "Wow wow wow"

def funcHi() :
    print("Hi hi hi")
    return "สวัสดี..."

print( funcWow() )

dti = funcWow()

print(f"{dti} {dti} {dti}")

print(f'{funcHi()} สมชาย')