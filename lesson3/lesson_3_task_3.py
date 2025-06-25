from address import Address
from mailing import Mailing

to_address = Address("680031", "г. Хабаровск", "ул. Санитарная", "7", "54")
from_address = Address("680052", "г. Хабаровск", "ул. Воровского", "30", "29")

mailing = Mailing(to_address, from_address, 100, "123456")

print(mailing)