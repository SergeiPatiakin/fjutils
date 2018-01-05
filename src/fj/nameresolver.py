class NameResolver:
    """Dictionary where each value has multiple keys, one of which is marked preferred"""
    def __init__(self, backwards_dict):
        """
        Args:
             backwards_dict: dict mapping value to list of names/keys. The first name/key is marked as preferred.
        """
        self.forwards_dict = {}
        self.reverse_dict = {}
        for value, keys_list in backwards_dict.items():
            self.setnames(value, keys_list)

    def __getitem__(self, item):
        return self.forwards_dict[item]

    def setnames(self, value, keys_list):
        self.reverse_dict[value] = keys_list[0]
        for key in keys_list:
            self.forwards_dict[key] = value

    def values(self):
        return self.reverse_dict.keys()

    def keys(self):
        return self.forwards_dict.keys()

    def __iter__(self):
        return iter(self.keys())

    def items(self):
        """Iterate over (preferred_name, value) tuples"""
        for v, k in self.reverse_dict.items():
            yield k, v