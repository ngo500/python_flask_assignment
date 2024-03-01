from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

@app.route('/', , methods=['GET'])
def get_transactions():
    """
    GET method to retrieve and display all transactions
    returns:
    always renders the transactions.html page
    """
    return render_template("transactions.html", transactions = transactions)

# Create operation

# Update operation

# Delete operation

# Run the Flask app
    
