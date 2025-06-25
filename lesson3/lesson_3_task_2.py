from smartphone import Smartphone

catalog = [
    Smartphone("iPhone", 16, "+79098081212"),
    Smartphone("Samsung", "S25 Ultra", "+79825465555"),
    Smartphone("Honor", "X9c", "+79145204545"),
    Smartphone("Xiaomi", "Redmi Note 14", "+79244045050"),
    Smartphone("realme", "14Pro+", "+79940762020")
]

for smartphone in catalog:
    print(smartphone.brand, smartphone.model, smartphone.number)