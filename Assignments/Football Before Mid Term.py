file_name = input("Enter a file name:")
file_open = open(file_name, 'r')

while True:
    file_read = file_open.readline()
    if file_read == '':
        break
    else:
        print(file_read.rstrip())
