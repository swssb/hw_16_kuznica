from flask import Flask
from sqlalchemy import desc
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.app_context().push()
db = SQLAlchemy(app)

class Fruit(db.Model):
    __tablename__ = 'fruits'
    pk = db.Column(db.Integer, primary_key=True, autoincrement=True)
    icon = db.Column(db.String(6))
    name = db.Column(db.String(50))
    category = db.Column(db.String(50))
    kcal = db.Column(db.Integer)


db.create_all()

mock_fruits = []
mock_fruits.append(Fruit(icon="🍏", name="Аpple", category="fruit", kcal=38))
mock_fruits.append(Fruit(icon="🍎", name="RedApple", category="fruit", kcal=40))
mock_fruits.append(Fruit(icon="🍌", name="Banana", category="fruit", kcal=96))
mock_fruits.append(Fruit(icon="🥑", name="Avocado", category="fruit", kcal=160))
mock_fruits.append(Fruit(icon="🍅", name="Tomato", category="veggie", kcal=23))
mock_fruits.append(Fruit(icon="🥦", name="Broccoli", category="veggie", kcal=34))
mock_fruits.append(Fruit(icon="🥕", name="Carrot", category="veggie", kcal=41))
mock_fruits.append(Fruit(icon="🍪", name="Cookie", category="sweets", kcal=417))
mock_fruits.append(Fruit(icon="🍩", name="Donut", category="sweets", kcal=280))
mock_fruits.append(Fruit(icon="🍰", name="Cake", category="sweets", kcal=271))

db.session.add_all(mock_fruits)
db.session.commit()

all = Fruit.query.all()
for one in all:
    print(one.name)
print()
cookie = db.session.query(Fruit).filter(Fruit.name == 'Cookie')
print(cookie.one().icon, cookie.one().name, cookie.one().kcal)

print()

veggie = db.session.query(Fruit).filter(Fruit.category == 'veggie')
veggie = veggie.all()
print("VEGGIE")
for one in veggie:
    print(one.icon, one.name, one.kcal)

print()

sweets = db.session.query(Fruit).filter(Fruit.category == 'sweets')
sweets = sweets.all()
print('SWEETS')
for one in sweets:
    print(one.icon, one.name, one.kcal)

print()

low_calory = db.session.query(Fruit).filter(Fruit.kcal < 200)
low_calory = low_calory.all()
print('low_calory meal(<200)')
for one in low_calory:
    print(one.icon, one.name, one.kcal)


print()

veggie_sort = db.session.query(Fruit).filter(Fruit.category == 'veggie').order_by(Fruit.name)
veggie_sort = veggie_sort.all()
print("VEGGIE SORTED")
for one in veggie_sort:
    print(one.icon, one.name, one.kcal)

print()

sweets = db.session.query(Fruit).filter(Fruit.category == 'sweets').order_by(desc(Fruit.kcal))
sweets = sweets.all()
print('SWEETS sort by calory')
for one in sweets:
    print(one.icon, one.name, one.kcal)

print()
two_products = Fruit.query.limit(2).all()
# sweets = sweets.all()
print('first 2 products')
for one in two_products:
    print(one.icon, one.name, one.kcal)

print()


max_calory = db.session.query(Fruit).order_by(desc(Fruit.kcal))
max_calory = max_calory.first()
min_calory = db.session.query(Fruit).order_by(Fruit.kcal)
min_calory = min_calory.first()

print('max calory', max_calory.name, max_calory.kcal)
print('min calory', min_calory.name, min_calory.kcal)

print()

items_with_a = db.session.query(Fruit).filter(Fruit.name.like("%a%"))
items_with_a = items_with_a.all()

for one in items_with_a:
    print(one.name)
