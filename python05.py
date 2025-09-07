# ทำโปรแกรมคำนวน พื้นที่สี่เหลี่ยม  รับค่ากว้าง ยาว ทางแป้นพิมพ์ แล้วแสดงผลออกมา
widths = int(input ('ป้อนความกว้าง : '))
longs = float(input ('ป้อนความยาว : '))
area = widths * longs 
print('----------')
print(f'สี่เหลี่ยมกว้าง {widths} ยาว {longs} มีพื้นที่ {area}') # ใช้ f- string
print('----------')
print('สี่เหลี่ยมกว้าง',widths,'ยาว',longs,'มีพื้นที่',area) # ใช้ ,
print('----------')
print('สี่เหลี่ยมกว้าง '+str(widths) +' ยาว '+str(longs)+' มีพื้นที่ '+str(area)) # ใช้ + 
print('----------')
print('สี่เหลี่ยมกว้าง {0} ยาว {1} มีพื้นที่ {2}'.format(widths,longs,area)) # ใช้ เมธอด format