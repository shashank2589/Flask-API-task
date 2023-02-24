from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def welcome():
        return render_template("index1.html")

@app.route("/items", methods = ["POST"])
def items():
    if(request.method == "POST"):
        items = request.form["items"]
        qty = float(request.form["qty"])
        rate = float(request.form["rate"])
        item_cost = qty*rate
        if item_cost <= 1000:
            discount = item_cost * 0.1
            final_cost = item_cost-discount
            return f"<h2>The item cost is Rs. {item_cost}, you got 10% off i.e Rs. {discount} and the final cost is Rs. {final_cost}<h2>"
        elif 1000 < item_cost <= 2000:
            discount = item_cost * 0.2
            final_cost = item_cost-discount
            return f"<h2>The item cost is Rs. {item_cost}, you got 20% off i.e Rs. {discount} and the final cost is Rs. {final_cost}<h2>"
        else:
            discount = item_cost * 0.3
            final_cost = item_cost-discount
            return f"<h2>The item cost is Rs. {item_cost}, you got 30% off i.e Rs. {discount} and the final cost is  Rs. {final_cost}<h2>"
       

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)