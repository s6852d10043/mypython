# break และ continue ใน Loop
# break  ใน Loop ทำงานเมื่อใด ให้หยุดทำงานใน loop ทันที
# continue ใน Loop ทำงานเมื่อใด ถือว่าจบรอบนั้นแล้วและให้ข้ามไปท

for a in range(10) :
    print(f'{a+1} Hi...')
    if a == 3 :
      #break   
      continue
    print(f'{a+1} Hello...')