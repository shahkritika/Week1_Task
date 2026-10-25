"""Reverse a sentence, make it uppercase, and count its vowels."""
import sys


def main():
    if len(sys.argv) > 1:
        sentence = " ".join(sys.argv[1:])
    else:
        try:
            sentence = input("Enter a sentence: ").strip()
        except EOFError:
            sentence = ""

    if not sentence:
        sentence = "Python Full-Stack Internship Day One"
        print(f"No sentence entered, so we'll use: {sentence}")

    vowel_count = sum(1 for letter in sentence.lower() if letter in "aeiou")

    print(f"\nYour sentence: {sentence}")
    print(f"Backwards: {sentence[::-1]}")
    print(f"In uppercase: {sentence.upper()}")
    print(f"Number of vowels: {vowel_count}")

if __name__ == "__main__":
    main()
