class Property:
    def __init__(self, name: str):
        self.name = name.strip()

    def is_equal(self, name: str) -> bool:
        return self.name.lower() == name.lower().strip()
    
    def __eq__(self, item) -> bool:
        if isinstance(item, Property):
            return self.is_equal(item.name)
        return False
    def get_name(self) -> str:
        return self.name