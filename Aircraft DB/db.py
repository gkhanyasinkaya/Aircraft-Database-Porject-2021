inputFile = open("inputFile.txt","r")

Aircraft2Performance = open("aircraft2performance.txt","w")
Segment = open("segment.txt","w")
PerformanceTypes = open("performanceTypes.txt","w")


fileToList = inputFile.read().split("\n")
firstLine = fileToList[0].split(",")
j = 1
while j < 13:
    PerformanceTypes.write(str(j)+","+firstLine[j]+"\n")
    j+=1

for i in fileToList[1:]:
    i=i.split(",")
    j = 1
    while j < 13:
        Aircraft2Performance.write(i[0]+","+str(j) + "," + i[j]+"\n")
        j += 1
    Segment.write(i[-5]+","+i[-4]+","+i[-3]+","+i[-2]+","+i[-1]+"\n")



inputFile.close()
Aircraft2Performance.close()
Segment.close()
PerformanceTypes.close()