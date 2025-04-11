str = input()
newStr = ""
for a in str:
    if(
        a=="a"
    or  a=="e"
    or  a=="i"
    or  a=="o"
    or  a=="u"
    or  a=="A"
    or  a=="E"
    or  a=="I"
    or  a=="O"
    or  a=="U"
    ):
        continue
    else:
        newStr = newStr+a
print(newStr)

# for a in str:      .....code to remove the consonent......
#     if(
#         a=="a"
#     or  a=="e"
#     or  a=="i"
#     or  a=="o"
#     or  a=="u"
#     or  a=="A"
#     or  a=="E"
#     or  a=="I"
#     or  a=="O"
#     or  a=="U"
#     ):
#        newStr = newStr+a
# print(newStr)