out = []
in1 = []
in2 = []

with open("input1.txt", "r") as file:
  in1 = file.read().strip().split()

with open("input2.txt", "r") as file:
  in2 = file.read().strip().split()

length1 = len(in1)
length2 = len(in2)

while length1 != 0:
  out.append(in1[length1-1])
  length1 -= 1
  if length2 != 0:
    out.append(in2[length2-1])
    length2 -= 1

with open("output.txt", "w") as file:
  for i in out:
    file.write(i)
    file.write(" ")

with open("output.txt", "r") as file:
  print file.read()
