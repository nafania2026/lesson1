class Mailing:

    def __init__(self,to_address,from_address,cost,track):
        self.mailing_to_address=to_address
        self.mailing_from_address=from_address
        self.mailing_cost=cost
        self.mailing_track=track
    def get_mailing_to_address(self):
        return self.mailing_to_address
    def get_mailing_from_address(self):
        return self.mailing_from_address
    def get_mailing_cost(self):
        return self.mailing_cost
    def get_mailing_track(self):
        return self.mailing_track


    






