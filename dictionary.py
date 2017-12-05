dict = {'user':'vatsal','password':'0000#'}
print(dict['user'])

dict["id"] = '0064110'
print (dict)
if dict['user'] == 'vatsal':
    if dict['password'] =='0000#':
        print("Login Sucessful ")
    else:
        print(" Are you " + dict['user'])
else:
    print("data dooes Exist")
del dict ['id']
print (dict.get('user'))

for key, val in dict.items():
    print(key," = -> " , val)

dict ['user'] = 'jay'

count={}
for elements in dict:
    count[elements] = count.get(elements,0)+1
print(count)
print(dict )
dict.items()
