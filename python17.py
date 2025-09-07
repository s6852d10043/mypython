# if-elif

score = int(input('ป้อนคะแนน: '))

if score >= 80 :
    print('A')
elif score >= 70 :
    print('B')
elif score >= 60 :
    print('C')
elif score >= 50 :
    print('D')
else : # ไม่จำเป็นต้องมี if
    print('F')

print('Bye bye...')
