class management:
    def first(self):
        print("abi")
class management2(management):
    def first(self):
        super().first()
        print("aswin")
class management3(management2):
    def first(self):
        super().first()
        print("rr")
class management4(management3):
    def first(self):
        super().first()
        print("ghgh")
obj=management4()
obj.first()
