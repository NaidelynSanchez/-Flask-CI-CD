from flask import Flask, render_template
import unittest
import io

app = Flask(__name__)

@app.route('/')
def home():
    return "OK, EXITOSO"


@app.route('/run-tests')
def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_*.py')

    stream = io.StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)

    output = stream.getvalue()

    if result.wasSuccessful():
        return "OK"
    else:
        return "ERROR\n\n" + output


if __name__ == '__main__':
    app.run(debug=True)