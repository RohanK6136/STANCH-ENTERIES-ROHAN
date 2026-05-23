from collections import Counter

def most_frequent_word(text: str) -> str:
    if not text or not text.strip():
        return ""  # Return empty string for empty/whitespace input
    

    words = [word.lower() for word in text.split() if word]
    
    if not words:
        return ""
    
    # Count frequency of each word
    count = Counter(words)
    
    # Find maximum frequency
    max_freq = max(count.values())
    
    # Get all words with max frequency
    candidates = [word for word, freq in count.items() if freq == max_freq]
    
    
    return min(candidates)