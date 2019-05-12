fout = open("queries.txt", "w")

tableName  = input("Enter table name: ")
fin = open("all_tables/"+tableName.lower()+".txt", "r")

n = int(input("No. of attributes: "))

print("Enter data types in order...")
l = []
for i in range(n):
    l.append(input())

for line in fin:
    attributeList = line.split(",")
    s = "INSERT INTO " + tableName +" VALUES (" 
    for j in range(n):
        if j == n-1:
            attributeList[j] = attributeList[j][:-1]
        if l[j].lower() == "varchar" or l[j].lower() == "time":
            s+= '"' + attributeList[j]+'"'
        else:
            s+= attributeList[j]
        if j<n-1:
            s+=", "
    s += ");\n"
    print(s)
    fout.write(s)

fin.close()
fout.close()