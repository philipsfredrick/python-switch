class Customer:
    def set_name(self,name):
        self.name = name
    def set_id(self,id):
        self.id = id
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
c = Customer()
c.set_name("Bulaba")
c.set_id(1)
print(c.name)
print("My name is: ", c.get_name())
print("My id is: ", c.get_id())

# class methods in python
# class Pizza:
#     radius = 200
#     @classmethod
#     def get_radius(cls):
#         return cls.radius
# print(Pizza.get_radius())