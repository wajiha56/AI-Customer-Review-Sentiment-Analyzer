# Import TextBlob library
from textblob import TextBlob

print("--- Initializing AI NLP Engine ---\n")

# Customer Reviews
reviews = [
    "This product is absolutely amazing! I love it.",
    "Terrible experience, the item arrived broken and customer support was rude.",
    "It's okay, not the best but it gets the job done."
]

# AI analyzing each review
for review in reviews:
    
    # Create TextBlob object
    analysis = TextBlob(review)

    # Check sentiment polarity
    if analysis.sentiment.polarity > 0.1:
        mood = "Positive 😊"

    elif analysis.sentiment.polarity < -0.1:
        mood = "Negative 😡"

    else:
        mood = "Neutral 😐"

    # Print result
    print(f"Customer Said: '{review}'")
    print(f"AI Verdict: {mood}\n")

print("Text analysis complete.")