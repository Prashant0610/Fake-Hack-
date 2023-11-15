import time

a = str(input("Enter your phone number: "))
b = len(a)
if b > 10:
    print("You're a scammer!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    countdown = 0
elif b < 10:
    print("You're a scammer!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    countdown = 0
elif b == 10:
    print("Thanks for giving me your personal information!")
    countdown = 0
print("Starting Brute force method .../")
while countdown <= 10:
    time.sleep(1.0)
    countdown += 1
    print("# Attempt: ", countdown)
    print("# Attempt failed, Retrying")
time.sleep(1)
print("# Attempt:  12")
print("# Attempt successful .../")
time.sleep(2.0)
print("# Getting your IP Address .../")
time.sleep(2.0)
print("# Address snatched .../")
time.sleep(0.6)
print("# Updating Hackers.forum.odg Port: 5500 .../")
time.sleep(0.5)
print("# Thank you for your info .../")
time.sleep(0.3)
print("# Exiting .../")