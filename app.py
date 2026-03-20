from flask import Flask, render_template, request, redirect, url_for
from models import Business

app = Flask(__name__)

businesses = []

@app.route('/')
def index():
    return render_template('index.html', businesses=businesses)

@app.route('/add', methods=['GET', 'POST'])
def add_business():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        location = request.form['location']
        address = request.form.get('address', '')
        business = Business(name, category, location, address)
        businesses.append(business)
        return redirect(url_for('index'))
    return render_template('add_business.html')

if __name__ == '__main__':
    app.run(debug=True)