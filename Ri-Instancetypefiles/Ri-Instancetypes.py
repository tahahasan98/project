def dict2():
    try:
        fo = open("/Users/Taha/Desktop/ri-instanceTypes (1).csv", "r")

        dnary = {}
        for line in fo:
            nline = line.replace("\n", "")
            al = nline.split(",")

            dnary.update({al[0]:al[8]})
        try:
            print(dnary["m3.xlarge"])

        except IOError:
            print("Could not fine m3.xlarge")
        try:
            (dnary.pop("t2.large"))
        except KeyError:
            print("cannot find t2.large")
    except IOError:
        print("Error could not read file")
    print(dnary)

dict2()
