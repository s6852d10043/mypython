# มี parameter มี return

def calSqareArea(widths, longs) :
    return widths * longs

def func_info(id, name) :
    print("Hi...")
    return (f'สวัสดี {id} คุณ {name}')

print(f"พท. กว้าง 20 ยาว 30 เท่ากับ {calSqareArea(20, 30)}")
print(f"พท. กว้าง 15 ยาว 200 เท่ากับ {calSqareArea(15, 200)}")

print(func_info("666", "สมชาย"))
print(func_info("888", "สมหญิง"))