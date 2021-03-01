txt = 'In February 1991, Van Rossum published the code (labeled version 0.9.0) to alt.sources.'

# ord, chr
for i in txt:
    if(ord(i) >= 48 and ord(i)<=57):
        print(i)


# input A1B2C3 - Output B2C3D4
x = ""
print('A1B2C3')
for i in 'A1B2C3':
    num = ord(i)+1
    x = x+chr(num)

print(x)