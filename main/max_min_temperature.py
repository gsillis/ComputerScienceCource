def find_min_max_temperature(array):
  print("A temperatura minima foi de: ", min_temperature(array), "C.")
  print("A temperatura máxima foi de: ", max_temperature(array), "C.")

def min_temperature(temperature):
  min = 0
  index = 1

  while index < len(temperature):  
    if temperature[index] < min:
      min = temperature[index]
    index += 1
  return min

def max_temperature(temperature):
  min = 0
  index = 1

  while index < len(temperature):  
    if temperature[index] > min:
      min = temperature[index]
    index += 1
  return min