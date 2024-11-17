from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return '''
        <h1>Welcome to the Simple Flask Web App</h1>
        <p><a href="/submit">Go to Submit Page</a></p>
    '''

# Submit route
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        print("It is POST")
        # Get data from the form
        name = request.form.get('name')
        return f'''
            <h1>Thank you, {name}!</h1>
            <p><a href="/">Back to Home</a></p>
        '''
    return '''
        <h1>Submit Your Name</h1>
        <form method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <button type="submit">Submit</button>
        </form>
        <p><a href="/">Back to Home</a></p>
    '''

# Run the app
if __name__ == '__main__':
    app.run(port=3030)
