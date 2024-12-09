from app import my_deskrip
from flask import url_for

def my_list():
    merek = [
        {"id": 1, "name": "Produk 1", "price": "Rp27.600", "image": "/static/img/Assus.png"},
        {"id": 2, "name": "Produk 2", "price": "Rp49.680", "image": "/static/img/HP elite book.png"},
        {"id": 3, "name": "Produk 3", "price": "Rp42.500", "image": "/static/img/Laptop Gaming.png"},
        {"id": 4, "name": "Produk 4", "price": "Rp50.500", "image": "/static/img/produk3.png"},
        {"id": 5, "name": "Produk 5", "price": "Rp42.500", "image": "/static/img/produk1.png"},
        ]
    return merek

def create_list():
    gabung = []
    for m, s in zip(list1, list2):
        gabung.append({**m, **s})
    return gabung

list1 = my_deskrip.create_deskripsi()
list2 = my_list()