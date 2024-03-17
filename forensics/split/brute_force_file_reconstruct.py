import itertools
import os
"""
The given files are pieces of a png file_name without overlap. 
The first one contains 'PNG' at the beginning.
The last one contains 'IEND' near the end.
The remaining ones are middle pieces.
This script creates all the possible images. One should be correct.
"""

given_files = os.listdir("file_pieces")
start = ""
middle = []
end = ""
for file_name in given_files:
    with open(os.path.join("file_pieces/", file_name), "rb") as test_file:
        test_file = test_file.read()
        if b"PNG" in test_file[:5]:
            if start != "":
                print("There are more than one possible start files.")
            start = os.path.join("file_pieces/", file_name)
        elif b"IEND" in test_file[-8:]:
            if end != "":
                print("There are more than one possible end files.")
            end = str(os.path.join("file_pieces/", file_name))
        else:
            middle.append(os.path.join("file_pieces/", file_name))

permutations = itertools.permutations(middle)

for i, this_middle in enumerate(permutations):
    file_start = open(start, "rb").read()
    file_middle = b""
    file_end = open(end, "rb").read()

    for file_name in this_middle:
        file_middle += open(file_name, "rb").read()

    file_contents = file_start + file_middle + file_end
    possible_file = open(str(i) + ".jpg", "wb").write(open(end, "rb").read())
