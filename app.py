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


# Update operation

# Delete operation

# Run the Flask app
    
