width = int(input("Digite a largura: "))
height = int(input("Digite a altura: "))

line = 1

while line <= height: 
  column = 1
  while column <= width: 
    if line == 1 or line == height or column == 1 or column == width:
      print("#", end="")
    else:
      print(" ", end="")
    column += 1
  print()
  line += 1