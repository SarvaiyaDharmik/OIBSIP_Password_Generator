from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    password = ""

    if request.method == 'POST':

        length = int(request.form['length'])

        use_upper = request.form.get('uppercase')
        use_lower = request.form.get('lowercase')
        use_numbers = request.form.get('numbers')
        use_symbols = request.form.get('symbols')

        characters = ""

        if use_upper:
            characters += string.ascii_uppercase

        if use_lower:
            characters += string.ascii_lowercase

        if use_numbers:
            characters += string.digits

        if use_symbols:
            characters += string.punctuation

        if length < 8:
            return render_template('index.html',
                                   error="Password length must be at least 8")

        if characters == "":
            return render_template('index.html',
                                   error="Select at least one character type")

        password = ''.join(random.choice(characters) for i in range(length))

    return render_template('index.html', password=password)

if __name__ == '__main__':
 app.run(debug=True, port=5001)