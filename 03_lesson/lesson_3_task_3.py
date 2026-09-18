from address import Address
from mailing import Mailing
#создаём адрес-отправитель
address_from = Address("<109559>", "<Москва>", " < Ставропольская > ","<64k2>","<199к.2>")
#создаём  любой адресс_получатель
address_to = Address("<191024>","<Санкт Петербург>","<Невский проспект>", "<28>", "<1эт>")
#print(address_to.get_address_info())
#создаём экземпляр Mailling и передаём в него объекты адресов.
# а также стоимость и трек-номер 
mailing1 = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=900,
    track="TRACK12345"
)
# вывод посылки
print(
    f"Отправление {mailing1.get_mailing_track()}"
    f" из {mailing1.get_mailing_from_address().get_address_index()},"
    f" {mailing1.get_mailing_from_address().get_address_city()},"
    f" {mailing1.get_mailing_from_address().get_address_street()},"
    f" {mailing1.get_mailing_from_address().get_address_house()} - "
    f" {mailing1.get_mailing_from_address().get_address_apartment()}"
    f" в {mailing1.get_mailing_to_address().get_address_index()},"
    f" {mailing1.get_mailing_to_address().get_address_city()},"
    f" {mailing1.get_mailing_to_address().get_address_street()},"
    f" {mailing1.get_mailing_to_address().get_address_house()} -"
    f" {mailing1.get_mailing_to_address().get_address_apartment()}."
    f" Стоимость {mailing1.get_mailing_cost()}рублей. "
)












