li=[110,31,61,81,71,41]

mx=li[0]

for i in range(len(li)):
    if mx > li[i]:
        mx=li[i]

print(mx)