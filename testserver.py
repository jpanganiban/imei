from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/index.php', methods=['GET', 'POST'])
def test_api():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        print(request.form)
        return None


if __name__ == '__main__':
    app.run(debug=True)
