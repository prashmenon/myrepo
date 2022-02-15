#Sample loops
#while loop
x=0
while x < 100:
    print(x+1)
    x+=1
    
#for loop
for x in range(100):
    print(x+1)
    
    
dow=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
for i in dow:
    print (i)

# x='banana'
# for i in x:
#     if x[i]=='a':
#         x.remove(i)
#     else:
#         print (x[i])
# print(x)
        
#Sample verification checks

x=0

if x == 0:
    x=10
    print (x)
else:
    print ("No")
    
ans=input("Do you like coffee")
if ans.lower() == 'y':
    print ('Coffee Coffee Coffee')
elif ans.lower() == 'yes':
    print ('Coffee Coffee Coffee')
else:
    print ('Tea dirinker')