import requests

response = requests.post("https://getdjeb.herokuapp.com/predict/", json={
  "model_key": "Peugeot",
  "mileage":223269,
  "engine_power":120,
  "fuel": "diesel",
  "paint_color": "blue",
  "car_type": "convertible",
  "private_parking_available": True,
  "has_gps": True,
  "has_air_conditioning": False,
  "automatic_car": False,
  "has_getaround_connect": False,
  "has_speed_regulator": False,
  "winter_tires": True
  })
print(response.json())