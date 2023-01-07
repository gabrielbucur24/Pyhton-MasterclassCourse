filename = input("Enter your file name: ")

index = filename.index(".")
extension = filename[index + 1:]

print(f"Your file's extension is '{extension}'")
