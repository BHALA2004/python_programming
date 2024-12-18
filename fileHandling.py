

file = open('example.txt','w')
content = input("Enter Content:")
file.write(content)
file.close()


file = open('example.txt','r')

content = file.read()

print(content)

file.close()
