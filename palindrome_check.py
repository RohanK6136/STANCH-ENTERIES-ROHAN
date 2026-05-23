def is_palindrome(s: str) -> bool:
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]



if __name__ == "__main__":
    print("Enter strings to check (type 'exit' to quit):")
    while True:
        text = input("> ").strip()
        if text.lower() == 'exit':
            break
        print(is_palindrome(text))