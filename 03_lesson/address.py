class Address:

    def __init__(self,index,city,street,house,apartment):
        self.address_index=index
        self.address_city=city
        self.address_street=street
        self.address_house=house
        self.address_apartment=apartment
    def get_address_index(self):
        return self.address_index
    def get_address_city(self):
        return self.address_city
    def get_address_street(self):
        return self.address_street
    def get_address_house(self):
        return self.address_house
    def get_address_apartment(self):
        return self.address_apartment

    def get_address_info(self):
        return F"<индекс>:{self.address_index}, <город>:{self.address_city}, <улица>:{self.address_street}, <дом>-<квартира>:{self.address_house}-{self.address_apartment}"

address=Address("<109559>", "<Москва>", " < Ставропольская > ","<64k2>","<199к.2>" )

#print(address.get_address_info())