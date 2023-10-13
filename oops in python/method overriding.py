class P:
    def properties_status(self):
        print("Money, Land, Gold")
    def to_marry(self):
        print("Nonso")
class C(P):
    def study_status(self):
        print("Studies done waiting for job")
    def to_marry(self):
        print("Meghan")

c = C()
c.properties_status()
c.to_marry()
c.study_status()