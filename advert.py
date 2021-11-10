import json


class ColorizeMixin():
    def colorize(self, text: str, repr_colour_code: int):
        return f'\033[1;{repr_colour_code};20m {text}\n'


class Advert(ColorizeMixin):
    repr_colour_code = 32

    def __init__(self, json_dict: {}):
        self.json_dict = json_dict

        if 'price' in self.json_dict:
            if self.json_dict['price'] < 0:
                raise ValueError('price must be >= 0')

    def __getattribute__(self, name):
        if name == 'json_dict' or name == 'price' or name == '_price' or name == 'repr_colour_code':
            return object.__getattribute__(self, name)

        elif not isinstance(self.json_dict[name], dict):
            return self.json_dict[name]

        else:
            return Advert(self.json_dict[name])

    @property
    def price(self):
        if 'price' in self.json_dict:
            self._price = self.json_dict['price']
        else:
            self._price = 0
        return self._price

    def __repr__(self):
        return super().colorize(f'{self.title} | {self.price} ₽', self.repr_colour_code)


if __name__ == '__main__':
    example_string = """{
    "title": "python",
    "price": 300,
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская", "Таганская"]
        }
    }"""

    example = json.loads(example_string)
    example_ad = Advert(example)

    print(example_ad.location.metro_stations)
    print(example_ad.title)
    print(example_ad.price)
    print(example_ad)
