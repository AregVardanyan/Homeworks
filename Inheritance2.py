class Hotel:
    def __init__(self, hotel_name, place, rooms_mid, mid_room_price, rooms_lux_, lux_room_price, *args, **kwargs):
        self.hotel_name = hotel_name
        self.place = place
        self.rooms_mid = rooms_mid
        self.mid_room_price = mid_room_price
        self.rooms_lux = rooms_lux_
        self.lux_room_price = lux_room_price
        super().__init__(*args, **kwargs)

    @property
    def hotel_present(self):
        return f"The hotel {self.hotel_name} in {self.place}.\n" \
               f"Our rooms:\n" \
               f"   Mid rooms {self.rooms_mid} --- price - {self.mid_room_price}$\n" \
               f"   Lux rooms {self.rooms_lux} --- price - {self.lux_room_price}$\n"

    def book(self, room_type):
        if room_type == "mid":
            for i in self.rooms_mid:
                if self.rooms_mid[i] == "free":
                    self.rooms_mid[i] = "busy"
                    print(f"You booked mid room -- {i}")
                    break
        elif room_type == "lux":
            for i in self.rooms_lux:
                if self.rooms_lux[i] == "free":
                    self.rooms_lux[i] = "busy"
                    print(f"You booked lux room -- {i}")
                    break

    def available_room_check(self, room_type):
        count = 0
        if room_type == "mid":
            for i in self.rooms_mid:
                if self.rooms_mid[i] == "free":
                    count += 1
            print(f"There is {count} available mid rooms")
        elif room_type == "lux":
            for i in self.rooms_lux:
                if self.rooms_lux[i] == "free":
                    count += 1
            print(f"There is {count} available lux rooms")

    def discount(self, percent):
        self.mid_room_price *= percent / 100
        self.lux_room_price *= percent / 100


class Taxi:
    def __init__(self, taxi_name, type_price, *args, **kwargs):
        self.taxi_name = taxi_name
        self.type_price = type_price
        super().__init__(*args, **kwargs)

    @property
    def taxi_present(self):
        return f"The taxi {self.taxi_name}\n" \
               f"Prices --- {self.type_price}\n"

    def discount(self, percent):
        for i in self.type_price:
            self.type_price[i] *= percent / 100


class Tour(Hotel, Taxi):
    def __init__(self, tour_name, *args, **kwargs):
        self.tour_name = tour_name
        super().__init__(*args, **kwargs)
        self.price_lux = max(self.type_price.values()) + self.lux_room_price
        self.price_mid = min(self.type_price.values()) + self.mid_room_price

    @property
    def present(self):
        return f"Hello we offer {self.tour_name} tour:\n" \
               f"Programs:\n" \
               f"Lux tour which include---\n" \
               f"   Lux hotel room {self.lux_room_price}$ and lux taxi ||| total --- {self.price_lux}$\n" \
               f"Mid tour which include---\n" \
               f"   Mid hotel room {self.mid_room_price}$ and lux taxi ||| total --- {self.price_mid}$\n"


Tour1 = Tour("YourSummer", "SunCoast", "California", {"room1": "free", "room2": "free", "room3": "free"}, 50,
               {"room1": "free", "room2": "free", "room3": "free"}, 150, "International", {"eco": 10, "lux": 20})
print(Tour1.hotel_present)
print(Tour1.taxi_present)
print(Tour1.present)
