class Customer:
    def __init__(self, custPIN=1234, custBalance=50000):
        self.pin = int(custPIN)
        self.balance = int(custBalance)
    def CekID(self):
        return self.id
    def CekPIN(self):
        return self.pin
    def CekSaldo(self):
        return self.balance