class Category:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class Product:
    def __init__(self, name, description, date_fabrication, is_active, category):
        self.name = name
        self.description = description
        self.date_fabrication = date_fabrication
        self.is_active = is_active
        self.category = category

class OrderItem:
    def __init__(self, quantity, unitary_price, order, product):
        self.quantity = quantity
        self.unitary_price = unitary_price
        self.order = order
        self.product = product

class Order:
    def __init__(self, total_price, status, client):
        self.total_price = total_price
        self.status = status
        self.client = client

class Client:
    def __init__(self, first_name, last_name, address, cell_phone, email, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.cell_phone = cell_phone
        self.email = email
        self.gender = gender

class ClientSocialNetwork:
    def __init__(self, client, socialnetwork):
        self.client = client
        self.socialnetwork = socialnetwork

class SocialNetwork:
    def __init__(self, name, description):
        self.name = name
        self.description = description
