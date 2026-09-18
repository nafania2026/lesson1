class Smartphone:

    def __init__(self,brand_phone,model_phone,subscriber_number):
        self.smartphone_brand_phone=brand_phone
        self.smartphone_model_phone=model_phone
        self.smartphone_subscriber_number=subscriber_number

    def get_smartphone_brand_phone(self):
        return self.smartphone_brand_phone

    def get_smartphone_model_phone(self):
        return self.smartphone_model_phone

    def get_smartphone_subscriber_number(self):
        return self.smartphone_subscriber_number

    def get_smartphone_info(self):
        return (f" <марка> - <модель>: {self.smartphone_brand_phone} - {self.smartphone_model_phone} . " 
                f"<номер телефона>: {self.smartphone_subscriber_number}")

smartphone=Smartphone("<Samsung Galaxy>", "<A17>", " < 89256251750 > " )
print(smartphone.get_smartphone_info())




