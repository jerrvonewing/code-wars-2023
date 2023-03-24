x = 0
# Add up all odd numbers between 10 and 20
for i in range(11,20,2):
    x+=i
print(x)


for i in range(1,21):
    if(i == 4 or i == 13):
        print(f"{i} is unlucky")
    elif(i % 2 == 0):
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

count = input("How many times do I have to tell you?\t")
for i in range(int(count)):
    print("GO CLEAN YOUR ROOM!")