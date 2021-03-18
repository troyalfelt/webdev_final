from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

contents = []

class Product:
    def __init__(self, name, price, quantity, image):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.image = image

skateboard = Product("Skateboard", 142.09, 0, "../static/images/skateboard.jpg")
bike = Product("Bike", 320.11, 0, "../static/images/bike.jpg")
skates = Product("Skates", 70.02, 0, "../static/images/skates.jpg")
unicycle = Product("Unicycle", 75.00, 0, "../static/images/unicycle.jpg")
tike = Product("TikeTruck", 102.73, 0, "../static/images/tike.jpg")
segue = Product("Segue", 799.99, 0, "../static/images/segue.jpg")
tank = Product("Tank", 85000000, 0, "../static/images/tank.jpg")
scooter = Product("Scooter", 32.06, 0, "../static/images/scooter.jpg")

products = [skateboard, bike, skates, unicycle, tike, segue, tank, scooter]

@app.route('/')
def index():


    return render_template('index.html', skb_price = skateboard.price,
    skb_q = skateboard.quantity, bike_price = bike.price, bike_q = bike.quantity,
    skates_price = skates.price, skates_q = skates.quantity, uni_price = unicycle.price,
    uni_q = unicycle.quantity, tike_price = tike.price, tike_q = tike.quantity,
    segue_price = segue.price, segue_q = segue.quantity, tank_price = tank.price,
    tank_q = tank.quantity, scooter_price = scooter.price, scooter_q = scooter.quantity)


@app.route('/add/<item>')
def put(item):
    for i in products:
        if item == i.name:
            if i not in contents:
                contents.append(i)
            i.quantity += 1
    return redirect(url_for('index'))

@app.route('/checkout')
def check():
    total = 0
    for i in contents:
        total += i.price * i.quantity
    return render_template('checkout.html', contents = contents, total = total)

@app.route('/remove/<item>')
def take(item):
    for i in products:
        if item == i.name:
            contents.remove(i)
            i.quantity = 0
    return redirect(url_for('check'))

@app.route('/finish/<amount>')
def fin(amount):
    total = 0
    for i in contents:
        total += i.price * i.quantity
    return render_template('checkout_complete.html', contents = contents, total = total)


if __name__ == "__main__":
    app.run(debug=True)
