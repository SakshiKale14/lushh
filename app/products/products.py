from flask import Flask , Blueprint , render_template, jsonify, request, abort ,redirect, url_for
from app.models import db,prod_jwellery,product_clothes
products_bp = Blueprint("products_bp", __name__, template_folder="templates/products")

row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}

@products_bp.route("/jewellery")
def jewellery():
	
	
	
	# product = Product(product)
	products = prod_jwellery.query.all()
	product_items=[]
	for r in products:
	
		product_items.append(row2dict(r))
	
	
	

	
	
	
	return render_template("list.html", 
		 products= product_items,
		 title='Jewellery' , 
		 length=len(product_items))


@products_bp.route("/clothing")
def clothing():
	# product = Product(product)
	products = product_clothes.query.all()
	product_items=[]
	for r in products:
	
		product_items.append(row2dict(r))
	
	
	

	
	
	
	return render_template("list.html", 
		 products= product_items,
		 title='Clothing' , 
		 length=len(product_items))
	
@products_bp.route("/jewellery/<product_id>")
def view_product( product_id):
	
	productRow = prod_jwellery.query.filter_by(prod_id=product_id).one()

	product_item = row2dict(productRow) 
	

	return render_template("view.html", product_item=product_item,title='Jewellery')

@products_bp.route("/clothing/<product_id>")
def viewclothing_product( product_id):
	
	productRow = product_clothes.query.filter_by(prod_id=product_id).one()

	product_item = row2dict(productRow) 
	

	return render_template("view.html", product_item=product_item,title='Clothing')
			

@products_bp.route("/view")
def view():
	return 'hi'
	# id = int(request.args.get("id"))
	# product = Product()
	# product_items = product.show_all_items()
	# product_items = [dict(p) for p in product_items if p['id'] == id]
	# print(product_items)
	# return render_template("view.html", 
	# 		results={"item":product_items},
	# 		title="Product View"
	# 		)

