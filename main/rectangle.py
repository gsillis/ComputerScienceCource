width = int(input("Digite a largura: "))
height = int(input("Digite a altura: "))

line = 0

while line < height: 
  column = 0
  while column < width: 
    print("#", end="")
    column += 1
  print()
  line += 1