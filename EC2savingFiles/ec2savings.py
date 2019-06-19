fo = open("/Users/Taha/Desktop/ec2savings.csv")
total = 0
count = 0
for line in fo:
    count = count + 1
    if (count > 1):
    #clean /n froms lines
        nline = line.replace("\n", "")
        nnline = nline.replace("$", "")
    #change the strings into arrays /n means new line
        arr = nnline.split(",")
        total = total + float(arr[4])
print("total:", total)