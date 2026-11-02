"""Python File Handling Lab Sheet 07 solution."""
# Create a text file and write text into it.
filename = "sample.txt"
text = input("Enter text to write into the file: ")
try:
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text + "\\n")
    print("Text written successfully to", filename)
except OSError as error:
    print("File error:", error)
