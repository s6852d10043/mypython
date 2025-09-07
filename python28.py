#  ค่าที่ return มีได้มากกว่า 1 ค่า มีเฉพาะ py

def func_dti(n1, n2):
    print("Wow....")
    print("Wee....")
    print("Woo....")
    return n1 * 10 , n2 *20 , "Hello..."

a, b, c = func_dti(10, 20)
print(a)
print(b)
print(c)