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

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    """
    GET or POST method to view and add new transactions
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

    #else- GET request, render the form.html page
    return render_template("form.html")

@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
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
            if tr['id'] == transaction_id:
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

@app.route('/delete/<int:transaction_id>', methods=['GET'])
def delete_transaction(transaction_id):
    #look for the transaction id in the transactions list
    for tr in transactions:
        #if the id matches, delete the transaction, and break
        if tr['id'] == transaction_id:
            transactions.remove(tr)
            break
    #redirect to the transactions page
    return redirect(url_for("get_transactions"))

@app.errorhandler(404)
def api_not_found(error):
    """
    Error handler for 404 errors, return error message
    Returns:
    404: always, error message for API not found
    """
    return {"message" : "Error- API not found!"}, 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Error handler for 500 errors, return error message
    Returns:
    500: always, error message for internal server error
    """
    return {"message" : "Error- Internval server error!"}, 500

if __name__ == "__main__":
    app.run(debug = True)
