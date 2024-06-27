from flask import Flask, render_template
import os

app = Flask(__name__)


files = [
    {
        'name': 'Chart for 8h without sentiment with last 20 percent',
        'image': '8h_no_sentiment_last_20_percent.png'
    },
    {
        'name': 'Chart for 8h without sentiment',
        'image': '8h_no_sentiment.png'
    },
    {
        'name': 'Chart for 8h with sentiment with last 20 percent',
                'image': '8h_sentiment_test.png'
    },
    {
        'name': 'Chart for 8h with sentiment',
                'image': '8h_sentiment.png'
    },
    {
        'name': 'Chart for 12h without sentiment with last 20 percent',
                'image': '12h_no_sentiment_last_20_percent.png'
    },
    {
        'name': 'Chart for 12h without sentiment',
                'image': '12h_no_sentiment.png'
    },
    {
        'name': 'Chart for 12h with sentiment with last 20 percent',
                'image': '12h_sentiment_last20.png'
    },
    {
        'name': 'Chart for 12h with sentiment',
                'image': '12h_sentiment.png'
    }
]


@app.route('/')
def index():
    return render_template('index.html', files=files)


if __name__ == '__main__':
    app.run(debug=True)
