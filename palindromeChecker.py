print("Palindrome Checker")
print()
word = input("Input a word: ").strip().lower()
print()

def pali(word):
  if len(word) <= 1:
    print(word, "is a palindrome, yay!")
    return True
  if word[0] != word[-1]:
    print(word, "is not a palindrome...")
    return False
  return pali(word[1:-1])