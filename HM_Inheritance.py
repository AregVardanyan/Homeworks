class Country:
    def __init__(self, country_name: str, continent: str):
        self.country_name = country_name
        self.continent = continent

    def present(self):
        return f"{self.name} {self.continent}"


class Brand:
    def __init__(self, brand_name: str, start_date: str):
        self.brand_name = brand_name
        self.start_date = start_date

    def present(self):
        return f"{self.brand_name} {self.start_date}"


class Season:
    def __init__(self, season_name: str, average_temperature: str):
        self.season_name = season_name
        self.average_temperature = average_temperature

    def present(self):
        return f"{self.season_name} {self.average_temperature}"


class Product(Country, Brand, Season):
    def __init__(self, product_name, product_type, product_price, product_quantity,
                 country_name, continent, brand_name, start_date, season_name, average_temperature):
        self.product_name = product_name
        self.product_type = product_type
        self.product_price = product_price
        self.product_quantity = product_quantity
        Country.__init__(self, country_name, continent)
        Brand.__init__(self, brand_name, start_date)
        Season.__init__(self, season_name, average_temperature)

    def present(self):
        return f"{self.product_name} {self.product_type} from {self.country_name}({self.continent})" \
               f" price-{self.product_price}\nAbout brand --- {self.brand_name} - started in {self.start_date}"

    def discount(self, percent):
        self.product_price *= percent / 100

    def increase(self):
        self.product_quantity += 1

    def decrease(self):
        self.product_quantity -= 1


product_1 = Product("MacBook", "Computer", "1000$", 5, "China", "Asia", "Apple", "2000", "Spring", "50 C")
print(product_1.present())
