# การแปลงข้อมูล
# Fundamental
# แปลงข้อมูลใดๆ เป็น string ใช้ฟังก์ ชัน str( )
# แปลงข้อมูล string เป็น number 
# -> เลขจำนวณเต็มใช้ฟังก์ชัน int( )
# -> เลขจำนวณทศนิยมใช้ฟังก์ชัน float( )
#+++++++++++++++++++++++++++++++++++++++++
# print( ) แสดงผลข้อมูล
# input( ) รับข้อมูลที่เป็น string เท่านั้น
#+++++++++++++++++++++++++++++++++++++++++
# สร้างโปรแกรมคำนวณเงินเดือนสุทธิที่ต้องจ่ายหลังจากหักภาษีแล้ว 7% ของเงินเดือน และหักค่าประกันสังคม 3% ของเงินเดือน
# โดยรับค่ารหัสพนักงาน ชื่อพนักงาน เงินเดือน ทางเเป้นพิมพ์ และแสดงผลข้อมูลที่รับมา
# พร้อมกับรายละเอียดว่าต้องเสียภาษีกี่บาท หักประกันสังคมกี่บาท และต้องจ่ายเงินเดือนสุทธิกี่บาท

print('----------------------------')
print('---โปรแกรมคำนวณเงินเดือนสุทธิ---')
print('----------------------------')
employee_id = input('ป้อนรหัสพนักงาน: ')
employee_name = input('ป้อนชื่อพนักงาน: ')
employee_salary = input('ป้อนเงินเดือน: ')
print('----------------------------')
employee_tax = float(employee_salary)* 7 / 100 
employee_insur = float(employee_salary)* 3 / 100 
employee_salary_total = float(employee_salary) - employee_insur - employee_tax
print(f'รหัสพนักงาน:{employee_id} คุณ {employee_name}')
print(f'เงินเดือนก่อนหักค่าใช้จ่าย: {float(employee_salary):,.2f}')
print(f'เงินเดือนหักภาษี 7%: {employee_tax:,.2f} บาท')
print(f'เงินเดือนหักประกันสังคม 3%: {employee_insur:,.2f} บาท')
print(f'เงินเดือนสุทธิที่ได้รับ: {employee_salary_total} บาท')
print('----------------------------')
# ใช้ เมธอด format
print('รหัสพนักงาน:{} คุณ {}'.format(employee_id,employee_name))
print('เงินเดือนก่อนหักค่าใช้จ่าย: {:,.2f}'.format(float(employee_salary)))
print('เงินเดือนหักภาษี 7%: {:,.2f} บาท'.format(employee_tax))
print('เงินเดือนหักประกันสังคม 3%: {} บาท'.format(employee_insur))
print('เงินเดือนสุทธิที่ได้รับ: {} บาท'.format(employee_salary_total))
print('----------------------------')
# ใช้ เมธอด ,
print('รหัสพนักงาน:',(employee_id),'คุณ',(employee_name))
print('เงินเดือนก่อนหักค่าใช้จ่าย',(employee_salary))
print('เงินเดือนหักภาษี 7%:',(employee_tax), 'บาท')
print('เงินเดือนหักประกันสังคม 3%:',(employee_insur),'บาท')
print('เงินเดือนสุทธิที่ได้รับ:',(employee_salary_total),'บาท')
print('----------------------------')
# ใช้ เมธอด+
print('รหัสพนักงาน:' +str((employee_id))+' คุณ '+str((employee_name)))
print('เงินเดือนก่อนหักค่าใช้จ่าย'+str((employee_salary)))
print('เงินเดือนหักภาษี 7%:'+str((employee_tax))+ 'บาท')
print('เงินเดือนหักประกันสังคม 3%:'+str((employee_insur))+'บาท')
print('เงินเดือนสุทธิที่ได้รับ:'+str((employee_salary_total))+'บาท')
print('----------------------------')