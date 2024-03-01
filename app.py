from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

@app.route('/', methods=['GET'])
def get_transactions():
    """
    GET method to retrieve and display all transactions
    returns:
    always renders the transactions.html page
    """
    return render_template("transactions.html", transactions = transactions)

@app.route('/add', methods['GET', 'POST'])
def add_transaction():
    """
    GET or POST method to add new transactions
    returns:
    POST request: creates a new transaction, adds it to the list, and redirects to transactions page
    else, GET request: renders the form.html page
    """
    if request.method == 'POST':
        #transaction to add
        transaction = {
        'id' : len(transactions) + 1,
        'date' : request.form['date'],
        'amount' : float(request.form['amount'])
        }
        #add transaction to transactions list
        transactions.append(transaction)
        #redirect to transactions page
        return redirect(url_for("get_transactions"))

    #else- GET request
    return render_template("form.html")

@app.route('edit/<int:transction_id>', methods=['GET', 'POST'])
def edit_transaction(transction_id):
    """
    GET or POST method to view or update transactions
    returns:
    POST request:
    else, GET request:
    """
    if request.method == 'POST':
        #transaction info to update to
        date = request.form['date']
        amount = float(request.form['amount'])
        #look for the transaction id in the transactions list
        for tr in transactions:
            #if the id matches, update the info, and break
            if tr['id'] == transction_id:
                tr['date'] = date
                tr['amount'] = amount
                break
        #redirect to transactions page
        return redirect(url_for("get_transactions"))

    #else- GET request, render the edit.html page if id is known
    for tr in transactions:
        #if the id matches,
        if tr['id'] == transaction_id:
            return render_template("edit.html", transaction = tr)


# Delete operation

# Run the Flask app
    
