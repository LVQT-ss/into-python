file_path = r'C:\Users\Final stage\Desktop\python\python\filedexuly.txt'  # Replace with the actual path

try:
    file_object = open(file_path, 'r')  # 'r' for reading

    data = file_object.read()  # Read the first character
    file_object.seek(50)
    data2 = file_object.read()  # Read the next 5 characters
    file_object.close()  # Close the file after you're done reading
    print(data)
    print(data2)

except FileNotFoundError:
    print("The file 'filedexuly.txt' does not exist.")
