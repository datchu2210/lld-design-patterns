"""
Abstract Factory Pattern - Notification System
----------------------------------------------

This module demonstrates the Abstract Factory Pattern using
a Notification system.

Each notification type creates a FAMILY of related objects:
- MessageSender
- MessageFormatter

Supported families:
- Email
- SMS

Pattern Type: Creational
"""

from abc import ABC, abstractmethod


# ============================================================
# 1. ABSTRACT PRODUCTS
# ============================================================

class MessageSender(ABC):
    @abstractmethod
    def send_message(self, message: str):
        pass


class MessageFormatter(ABC):
    @abstractmethod
    def format_message(self, message: str) -> str:
        pass


# ============================================================
# 2. CONCRETE PRODUCTS - EMAIL FAMILY
# ============================================================

class EmailMessageSender(MessageSender):
    def send_message(self, message: str):
        print(f"EMAIL SENT: {message}")


class EmailMessageFormatter(MessageFormatter):
    def format_message(self, message: str) -> str:
        return f"[EMAIL FORMAT] {message}"


# ============================================================
# 3. CONCRETE PRODUCTS - SMS FAMILY
# ============================================================

class SMSMessageSender(MessageSender):
    def send_message(self, message: str):
        print(f"SMS SENT: {message}")


class SMSMessageFormatter(MessageFormatter):
    def format_message(self, message: str) -> str:
        return f"[SMS FORMAT] {message}"


# ============================================================
# 4. ABSTRACT FACTORY
# ============================================================

class NotificationFactory(ABC):

    @abstractmethod
    def create_sender(self) -> MessageSender:
        pass

    @abstractmethod
    def create_formatter(self) -> MessageFormatter:
        pass


# ============================================================
# 5. CONCRETE FACTORIES
# ============================================================

class EmailNotificationFactory(NotificationFactory):

    def create_sender(self) -> MessageSender:
        return EmailMessageSender()

    def create_formatter(self) -> MessageFormatter:
        return EmailMessageFormatter()


class SMSNotificationFactory(NotificationFactory):

    def create_sender(self) -> MessageSender:
        return SMSMessageSender()

    def create_formatter(self) -> MessageFormatter:
        return SMSMessageFormatter()


# ============================================================
# 6. CLIENT
# ============================================================

class NotificationApp:
    def __init__(self, factory: NotificationFactory):
        self.sender = factory.create_sender()
        self.formatter = factory.create_formatter()

    def notify(self, message: str):
        print(self.formatter)
        formatted_message = self.formatter.format_message(message)
        self.sender.send_message(formatted_message)


# ============================================================
# 7. FACTORY SELECTOR (RUNTIME DECISION)
# ============================================================

def get_factory(factory_type: str) -> NotificationFactory:
    if factory_type == "email":
        return EmailNotificationFactory()
    elif factory_type == "sms":
        return SMSNotificationFactory()
    else:
        raise ValueError("Unsupported notification type")


# ============================================================
# 8. MAIN (USAGE)
# ============================================================

if __name__ == "__main__":
    factory = get_factory("email")
    app = NotificationApp(factory)
    app.notify("Your order is shipped")

    factory = get_factory("sms")
    app = NotificationApp(factory)
    app.notify("Your OTP is 123456")


# 🧩 Factory Pattern – Practice Question
# 📌 Problem Statement

# You are building a Payment Processing System.

# The system supports multiple payment methods, but only one object is created at a time.

# Factory Requirement

# Create a PaymentFactory that:

# Returns the correct Payment object

# Hides object creation logic from the client

# Uses Factory Pattern (NOT Abstract Factory)

# 🧠 Your Task

# Design:

# 1️⃣ Product Interface

# Payment

# 2️⃣ Concrete Products

# CreditCardPayment

# UPIPayment

# NetBankingPayment

# 3️⃣ Factory

# PaymentFactory

# create_payment(payment_type: str)

# 4️⃣ Client

# Uses only the factory

# Does not instantiate concrete classes

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
