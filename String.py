# s1 = "instagram"
# s2 = 'insta'
# s3 = '''insta3121@%&^#$&^'''
# s4 = """ menu:
#             1.Tea
#             2.Coffee
#             3.Juice
#      """
# print(s1, type(s1), len(s1))
# print(s2, type(s2), len(s2))
# print(s3, type(s3), len(s3))
# print(s4, type(s4), len(s4))

s = "instagram"

# >----Indexing

# print(s[1])
# print(s[5])
# print(s[-8])

# v1 = s[0]
# v2= s[-9]
# print(v1,v2)

# print(s[8])
# print(s[len(s)-1])
# print(s[-1])

# print(s[9])      >----IndexError


# r1 = s[2]
# r2 = s[3]
# r3 = s[4]
# r4 = s[5]
# print(type(r1))
# print(r1,r2,r3,r4)

# res = r1+r2+r3+r4
# print(res, type(res))

# r1 = s[0]
# r2 = s[1]
# r3 = s[2]
# r4 = s[3]
# r5 = s[4]
# res1 = r1+r2+r3+r4+r5
# print(res1, type(res1))

# r6 = s[-9]
# r7 = s[-8]
# r8 = s[-7]
# r9 = s[-6]
# r10 = s[-5]
# res2 = r6+r7+r8+r9+r10
# print(res2, type(res2))


# insta and atsni
res3 = s[0]+s[1]+s[2]+s[3]+s[4]
print(res3)

res4 = s[-9]+s[-8]+s[-7]+s[-6]+s[-5]
print(res4)

res5 = s[-5]+s[-6]+s[-7]+s[-8]+s[-9]
print(res5)

# ram and mar
res6 = s[6]+s[7]+s[8]
print(res6)

res7 = s[-3]+s[-2]+s[-1]
print(res7)

res8 = s[-1]+s[-2]+s[-3]
print(res8)

# tag and gat
res9 = s[3]+s[4]+s[5]
print(res9)

res10 = s[-6]+s[-5]+s[-4]
print(res10)

res11 = s[-4]+s[-5]+s[-6]
print(res11)