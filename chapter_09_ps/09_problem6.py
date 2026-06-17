# Write a program to mine a log file and find out whether it contains ‘python’.

with open("chapter_09_ps/log.txt") as f:
    content = f.read()

if("python" in content):
    print("python is present")

else :
    print("python is not present")