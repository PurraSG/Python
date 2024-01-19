import requests, json, datetime
timezone = "EET"
latitude = 57.4216
longitude = 25.9030
date = datetime.date.today()

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = result.json()
#print(json.dumps(user, indent=2))

maxt = user['daily']['temperature_2m_max'][0]
mint = user['daily']['temperature_2m_min'][0]

wmo = user['daily']['weathercode']

def weather(wmo):
  code = wmo[0]
  if code == 0:
      return "Clear sky"
  elif code in [1, 2, 3]:
      return "Mainly clear, partly cloudy, and overcast"
  elif code in [45, 48]:
      return "Fog and depositing rime fog"
  elif code in [51, 53, 55]:
      return "Drizzle: Light, moderate, and dense intensity"
  elif code in [56, 57]:
      return "Freezing Drizzle: Light and dense intensity"
  elif code in [61, 63, 65]:
      return "Rain: Slight, moderate and heavy intensity"
  elif code in [66, 67]:
      return "Freezing Rain: Light and heavy intensity"
  elif code in [71, 73, 75]:
      return "Snow fall: Slight, moderate, and heavy intensity"
  elif code == 77:
      return "Snow grains"
  elif code in [80, 81, 82]:
      return "Rain showers: Slight, moderate, and violent"
  elif code in [85, 86]:
      return "Snow showers slight and heavy"
  elif code == 95:
      return "Thunderstorm: Slight or moderate"
  elif code in [96, 99]:
      return "Thunderstorm with slight and heavy hail"
  else:
      return "Something went wrong"

print("WEATHER FOR SMILTENE, LATVIA")
print(date)
print()
print(weather(wmo))
print()
print("Min temperature 🧊")
print(mint)
print("Max temperature ☀")
print(maxt)
print()
