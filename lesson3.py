"""Lesson 3: corrected function exercises."""
def divide(a: float, b: float) -> float:
    if b == 0: raise ZeroDivisionError("Divisor must not be zero")
    return a / b

def user_summary(*, name, surname, year, city, email, telephone) -> str:
    return " ".join(map(str, (name, surname, year, city, email, telephone)))

def largest_two_sum(a: float, b: float, c: float) -> float:
    return sum(sorted((a,b,c))[1:])

def negative_power(x: float, y: int) -> float:
    if x <= 0 or y >= 0: raise ValueError("Expected x > 0 and y < 0")
    result = 1.0
    for _ in range(-y): result *= x
    return 1.0 / result

def running_sum(lines) -> int:
    total = 0
    for line in lines:
        for token in line.split():
            if token.lower() == "q": return total
            total += int(token)
    return total

def capitalize_word(word: str) -> str:
    return word[:1].upper() + word[1:]

def capitalize_words(text: str) -> str:
    return " ".join(capitalize_word(word) for word in text.split())
