#mixins are classes which add functionality to another class. not standalone classes

# class LogMixin:
#     # adds logging functionality
#     def log(self, message):
#         print(f"[{type(self).__name__}] {message}")

# class SerializeMixin:
#     # adds JSON - like serialization
#     def to_dict(self):
#         return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

# class AuditProduct(LogMixin, SerializeMixin):
#     def __init__(self, name, price):
#         # super().__init__()
#         self.name = name
#         self.price = price
#         self.log(f"Created product: {name}")

    
# p = AuditProduct('Widget', 10.00)
# print(p.to_dict())


# dunder (magic/ special) methods -> Double UNDERscore
# my_list = [1, 3, 5, "hello"]
# size = len(my_list)
# mylist.__len__()

class MetricSeries:
    """ a named series of numberic metric """
    
    def __init__(self, name, data=None):
        self.name = name
        self._data = list(data) if data else []

    # print a readable string
    def __str__(self):
        preview = self._data[:5]
        more = f" ... (+{len(self._data)-5} more)" if len(self._data) > 5 else ""
        return f"Metric Series('{self.name}': {preview}{more})"
    
    # retrieve data
    def __getitem__(self, key):
        return self._data[key]
    
    # setting data
    def __setitem__(self, key, value):
        self._data[key] = value

    def __mul__(self, scalar):
        return MetricSeries(f"{self.name} * scalar", [x * scalar for x in self._data])
    
    def __add__(self, other):
        if isinstance(other, MetricSeries):
            if len(self) != len(other):
                print("series must be same length for addition")
            else:
                return MetricSeries(f"{self.name}+{other.name}", [a+b for a, b in zip(self._data, other._data)])
        elif isinstance(other, (int, float)):
            return MetricSeries(f"{self.name}+{other}", [x + other for x in self._data ])
        else:
            print("Not implemented")

    def __len__(self):
        return len(self._data)


revenue = MetricSeries("revenue", [120, 30, 135, 90, 175])
costs = MetricSeries("costs", [90, 100, 80, 125, 130])

profit = revenue + costs.__mul__(-1)

print(f"Revenue items: {len(revenue)}")
print(f"Profit: {profit}")
