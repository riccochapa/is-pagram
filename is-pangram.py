# Version One

pangramCheck = "The quick brown fox jumps over the lazy dog"

def is_pangram(sentence):
    c = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentenceLetters = ""
    for char in sentence:
        for letter in alphabet:
            if char == letter and char not in sentenceLetters:
                sentenceLetters += char
    for char in sentenceLetters:
        for letter in alphabet:
            if char == letter:
                c += 1
    if c == 26:
        return True
    else:
        print sentenceLetters, alphabet
        return False

print is_pangram()


# Version Two

pangramCheck = "The quick brown fox jumps over the lazy dog"

def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentenceLetters = ""
    for char in sentence:
       if char in alphabet:
            sentenceLetters += char
    for char in alphabet:
        if char not in sentence:
            print sentenceLetters, alphabet
            return False

    return True

    else:
        print sentenceLetters, alphabet
        return False

print is_pangram()


# Version Three

pangramCheck = "The quick brown fox jumps over the lazy dog"

    def is_pangram(sentence):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabet:
            if char not in sentence:
                return False

        return True

    else:
        print sentenceLetters, alphabet
        return False

print is_pangram()


# Version Four

pangramCheck = "The quick brown fox jumps over the lazy dog"

  def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return not (set(alphabet) - set(sentence))

  else:
      print sentenceLetters, alphabet
      return False

print is_pangram()
