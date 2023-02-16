import json
# importing requests and json
import requests
class queue:

    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.insert(0, value)

    def pop(self):
        if len(self.queue) > 0:
            self.queue.pop(-1)
        else:
            print('the queue is already empty')

    def is_empty(self):
        if len(self.queue) == 0:
            print('the queue is already empty')
        else:
            print('the queue is not empty')

        inst = queue()
        inst.insert("hello1")
        inst.insert("hello2")
        inst.insert("hello3")
        inst.insert("hello4")
        inst.insert("hello5")
        print(inst.queue)
        inst.pop()
        inst.pop()
        inst.pop()
        inst.pop()
        inst.pop()
        inst.pop()
        print(inst.queue)
        ##############################################################


class queueTwo(queue):
    instats = {}

    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size
        queueTwo.instats[name] = self.queue

    def insert(self, value):
        if len(self.queue) < self.size:
            self.queue.insert(0, value)
        else:
            raise ValueError("QueueOutOfRangeException  Queue is full")

    @classmethod
    def get_queue(cls, value):
        return cls.instats[value]

    @classmethod
    def save(cls):
        with open("data.json", 'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data
            file_data.append(cls.instats)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file)

    @classmethod
    def load(cls):
        with open("data.json", 'r') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            return file_data


instTwo = queueTwo("instTwo", 2)
instTwo.insert("fly")
instTwo.insert("hello")
print(instTwo.get_queue("instTwo"))
# instTwo.insert("hello")
print(instTwo.queue)
print(instTwo.instats)
instTwo.save()
print(instTwo.load())


########################################################################################
class getWeather:

    def get_current_temperature(self,city):
        # HTTP request
        response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=6540e9a029e9476eb42165539231602&q={city}&aqi=no')
        # checking the status code of the request
        if response.status_code == 200:
           # getting data in the json format
           data = response.json()
           return f" {city}  current Temperature: {data['current']['temp_c']}"
        else:
           # showing the error message
           print("Error in the HTTP request")
    def get_lat_and_long(self,city):
        # HTTP request
        response = requests.get(
            f'http://api.weatherapi.com/v1/current.json?key=6540e9a029e9476eb42165539231602&q={city}&aqi=no')
        # checking the status code of the request
        if response.status_code == 200:
            # getting data in the json format
            data = response.json()
            return f" {city}  lon: {data['location']['lon'] } and lat: {data['location']['lat']}"
        else:
            # showing the error message
            print("Error in the HTTP request")
    def get_temperature_after(self,city, days, hour=None):
        # HTTP request
        if hour == None:
                response = requests.get(
                f'http://api.weatherapi.com/v1/forecast.json?key=6540e9a029e9476eb42165539231602&q={city}&days={days}')
                # getting data in the json format
                data = response.json()
                return data['forecast']['forecastday'][days - 1]['hour'][0]['temp_c']
        else:
            response = requests.get(
                f'http://api.weatherapi.com/v1/forecast.json?key=6540e9a029e9476eb42165539231602&q={city}&days={days}&hour={hour}')
            if response.status_code == 200:
                # getting data in the json format
                data = response.json()
                return data['forecast']['forecastday'][days - 1]['hour'][0]['temp_c']

# creating instants
inst=getWeather()

# [1] printing the current temperature
print(inst.get_current_temperature("london"))
# [2] printing the
print(inst.get_temperature_after('london', 5, 3))
# [3] printing the lan  temperature
print(inst.get_lat_and_long("london"))
