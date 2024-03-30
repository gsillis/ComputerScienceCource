def remove_repetidos(array):
  nova_lista = []
  seen = set()
  for item in array:
    if item not in seen:
      nova_lista.append(item)
      seen.add(item)
  return sorted(nova_lista)


      