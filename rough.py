from abc import ABC,abstractmethod
# abstractProduct

class Payment(ABC):
    @abstractmethod
    def process_payment(self,amount: float):
        pass

#CONCRETE PRODUCTS
class creditCardPayment(Payment):
    def process_payment(self,amount: float):
        return "Payment Done through CreditCard"+str(amount)
    
class UPIPayment(Payment):
    def process_payment(self,amount: float):
        return "Payment Done through UPI:"+str(amount)
    
class NetBankingPayment(Payment):
    def process_payment(self,amount: float):
        return "Payment Done through NETBanking"+str(amount)

# abstract Factory
class PaymentFactory(ABC):
    @abstractmethod
    def create_payment(self,payment_type: str):
        pass

#concrete Factories
class creditCardPaymentFactory(PaymentFactory):
    def create_payment(self):
        return creditCardPayment()

class UPIPaymentFactory(PaymentFactory):
    def create_payment(self):
        return UPIPayment()
    
class NetBankingPaymentFactory(PaymentFactory):
    def create_payment(self):
        return NetBankingPayment()
    

def get_factory(factory_type: str):
    if factory_type == "Card":
        return creditCardPaymentFactory()
    elif factory_type == "UPI":
        return UPIPaymentFactory()
    elif factory_type == "Net":
        return NetBankingPaymentFactory()
    
factory = get_factory('Card')
print(factory.create_payment().process_payment(1500))
