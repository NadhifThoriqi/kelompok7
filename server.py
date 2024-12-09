# untuk memanggin extensions
from flask import Flask, render_template, request
from app import my_class #untuk products

app = Flask(__name__)

products = my_class.create_list()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search/')
def search():
    query = request.args.get('query')
    return f'Anda mencari: {query}?'

@app.route('/deskripsi/laptop/')
def laptop():
    return render_template('deskripsi.html')

@app.route('/product/<int:product_id>/')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product.html', product=product)

@app.route('/checkout/<int:product_id>/')
def checkout(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('checkout.html', product=product)

@app.route('/process_checkout/', methods=['POST'])
def process_checkout():
    name = request.form['name']
    address = request.form['address']
    product = request.form['product']
    price = request.form['price']
    return f"Terima kasih {name}, pembelian {product} seharga {price} telah diterima dan akan dikirim ke {address}."

# untuk menjalankan server lokal
if __name__ == '__main__':
    app.run(debug=True)