f = open("/home/vinod/VK_Scripts/Practices/demo_file.txt", "r")
for x in f:
    x = x.rstrip()
    print(x)
f.close()