class Business:
    def __init__(self, name, category, location, address=''):
        self.name = name
        self.category = category
        self.location = location
        self.address = address

    def get_info(self):
        return f"{self.name} - {self.category} ({self.location}) - {self.address}"