import re
txt = "use of python in machine learning"
x = re.search("^Use.*Learning$",txt)
if (x) :
    print("yes ! we have a match!")
else :
    print("no match")