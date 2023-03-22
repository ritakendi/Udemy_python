import requests
API_KEY = "46cf97484c2ebff587acdf157132f32d"


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return new_func(data)


def new_func(data):
    return data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))
