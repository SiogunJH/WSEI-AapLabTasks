import re

POS_WORDS = {"good", "great", "excellent", "wonderful", "love", "best", "amazing", "brilliant", "perfect"}
NEG_WORDS = {"bad", "worst", "awful", "terrible", "hate", "boring", "waste", "poor", "horrible"}


def sentiment_score(text: str) -> int:
    """CPU-bound sentiment score helper importable by multiprocessing."""
    all_words = re.findall(r"\w+", text.lower())
    pos_count = sum(1 for word in all_words if word in POS_WORDS)
    neg_count = sum(1 for word in all_words if word in NEG_WORDS)
    return pos_count - neg_count
