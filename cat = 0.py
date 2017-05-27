# phone_book = {
#     "Sarah Hughes": "01234 567890",
#     "Tim Taylor": "02345 678901",
#     "Sam Smith":  "03456 789012"
# }

# try:
# 	phone_book["Jamie Theakston"]
# except:
# 	print("I guess he's not in there?")

import sys

print("The name of this script is {}".format(sys.argv[0]))
print("User supplied {} arguments at run time".format(len(sys.argv)))

for arg in sys.argv[1:]:
  print(arg)
  print (type(arg))

print(type(int('1')))