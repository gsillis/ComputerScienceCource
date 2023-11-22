inputSeconds = input("Por favor, entre com o número de segundos que deseja converter: ")

seconds = int(inputSeconds)

days = seconds / 86400
seconds %= 24 * 3600
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print(int(days), "dias,", int(hours), "horas,", int(minutes), "minutos", "e", int(seconds), "segundos.")