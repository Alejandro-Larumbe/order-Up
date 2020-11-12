from dotenv import load_dotenv
load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType, Table, Order, OrderDetail


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")
    tables = []
    for i in range(1,11):
        tables.append(Table(number=i, capacity=10))

    order = Order(employee_id = 1, table_id = 1, finished=True)
    # order2 = Order(employee_id = 1, table_id = 2, finished=True)

    order_details = OrderDetail(order_id = 1, menu_item_id = 1)
    # order_details1 = OrderDetail(order_id = 1, menu_item_id = 1)
    # order_details2 = OrderDetail(order_id = 2, menu_item_id = 1)


    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)
    # db.session.add_all(tables)
    # db.session.add_all([employee, beverages, entrees, sides, dinner, fries, drp, jambalaya])
    # db.session.add_all(tables)
    db.session.add_all([order, order_details])
    db.session.commit()
