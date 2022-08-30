

class Instance:
    def __init__(self, **kwargs):
        self.pkid: int = kwargs.get('pkid')
        self.ip_address: str = kwargs.get('ip_address')
        self.name: str = kwargs.get('name')
        self.country: str = kwargs.get('country')
        self.is_online: bool = kwargs.get('is_online')
        self.discount = kwargs.get('discount')