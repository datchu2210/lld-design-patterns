"""
=========================
FACTORY METHOD PATTERN
=========================

Definition:
-----------
Factory Method Pattern defines an interface for creating an object,
but lets subclasses decide which class to instantiate.

The Factory Method lets a class defer instantiation to subclasses.

Why it is used:
---------------
1. Removes tight coupling between client code and concrete classes
2. Follows Open/Closed Principle (OCP)
3. Enables polymorphism
4. Avoids large if/else or switch-case blocks

When to use:
------------
- When object creation logic varies based on context
- When new object types may be added in the future
- When client should not know concrete class names

This example is written for LLD (Low Level Design) practice.
"""

from abc import ABC, abstractmethod


# =========================================================
# 1. PRODUCT INTERFACE
# =========================================================
class Vehicle(ABC):
    """
    Product Interface

    All concrete products must implement this interface.
    """

    @abstractmethod
    def drive(self) -> str:
        pass


# =========================================================
# 2. CONCRETE PRODUCTS
# =========================================================
class Car(Vehicle):
    """
    Concrete Product - Car
    """

    def drive(self) -> str:
        return "Driving a car"


class Bike(Vehicle):
    """
    Concrete Product - Bike
    """

    def drive(self) -> str:
        return "Riding a bike"


# =========================================================
# 3. FACTORY (CREATOR) INTERFACE
# =========================================================
class VehicleFactory(ABC):
    """
    Creator (Factory) Abstract Class

    Declares the factory method which returns a Product.
    """

    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        """
        Factory Method

        Subclasses decide which concrete product to create.
        """
        pass


# =========================================================
# 4. CONCRETE FACTORIES
# =========================================================
class CarFactory(VehicleFactory):
    """
    Concrete Factory - Creates Car objects
    """

    def create_vehicle(self) -> Vehicle:
        return Car()


class BikeFactory(VehicleFactory):
    """
    Concrete Factory - Creates Bike objects
    """

    def create_vehicle(self) -> Vehicle:
        return Bike()


# =========================================================
# 5. CLIENT CODE
# =========================================================
def client_code(factory: VehicleFactory) -> None:
    """
    Client works with factories and products through abstractions.
    It never directly instantiates concrete classes.
    """
    vehicle = factory.create_vehicle()
    print(vehicle.drive())


# =========================================================
# 6. APPLICATION ENTRY POINT
# =========================================================
if __name__ == "__main__":
    """
    Execution Flow:
    ----------------
    1. Client chooses a factory
    2. Factory creates the appropriate object
    3. Client uses the object via interface
    """

    print("Factory Method Pattern Demo\n")

    car_factory = CarFactory()
    client_code(car_factory)

    bike_factory = BikeFactory()
    client_code(bike_factory)



# 🧪 Factory Method Pattern – Coding Test
# Problem Statement

# Design a Document Export System using the Factory Method Pattern.

# Requirements

# Create an abstract class Document

# Method: export() -> str

# Create concrete document types:

# PDFDocument

# WordDocument

# ExcelDocument

# Create an abstract factory class DocumentFactory

# Factory method: create_document() -> Document

# Create concrete factories:

# PDFDocumentFactory

# WordDocumentFactory

# ExcelDocumentFactory

# The client code:

# Should work only with DocumentFactory and Document

# Must NOT directly instantiate any concrete document classes

# No if-else or switch logic allowed in client code.



from abc import ABC, abstractmethod

# =========================================================
# 1. PRODUCT INTERFACE
# =========================================================
class Document(ABC):
    """
    Abstract Product
    """

    @abstractmethod
    def export(self) -> str:
        pass


# =========================================================
# 2. CONCRETE PRODUCTS
# =========================================================
class PDFDocument(Document):
    def export(self) -> str:
        return "Exporting PDF document"


class WordDocument(Document):
    def export(self) -> str:
        return "Exporting Word document"


class ExcelDocument(Document):
    def export(self) -> str:
        return "Exporting Excel document"


# =========================================================
# 3. FACTORY (CREATOR) INTERFACE
# =========================================================
class DocumentFactory(ABC):
    """
    Abstract Factory (Creator)
    """

    @abstractmethod
    def create_document(self) -> Document:
        pass


# =========================================================
# 4. CONCRETE FACTORIES
# =========================================================
class PDFDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return PDFDocument()


class WordDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return WordDocument()


class ExcelDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return ExcelDocument()


# =========================================================
# 5. CLIENT CODE
# =========================================================
def client_code(factory: DocumentFactory) -> None:
    document = factory.create_document()
    print(document.export())


# =========================================================
# 6. APPLICATION ENTRY POINT
# =========================================================
if __name__ == "__main__":
    pdf_factory = PDFDocumentFactory()
    client_code(pdf_factory)

    word_factory = WordDocumentFactory()
    client_code(word_factory)

    excel_factory = ExcelDocumentFactory()
    client_code(excel_factory)
