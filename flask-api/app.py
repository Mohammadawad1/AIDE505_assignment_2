from flask import Flask,request,jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()


@app.route("/predict",methods=["POST"])
def predict():
    try:
        data = request.get_json()
        text = data.get('text', '')
        prediction = analyzer.polarity_scores(text)
        sentiment_label = get_sentiment_label(prediction['compound'])
        return jsonify({
        'sentiment': sentiment_label
    })
    except Exception as e:
        return jsonify({
            "error":str(e)
        }),400


def get_sentiment_label(compound_score, pos_thresh=0.05, neg_thresh=-0.05):
    if compound_score >= pos_thresh:
        return "positive"
    elif compound_score <= neg_thresh:
        return "negative"
    else:
        return "neutral"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
