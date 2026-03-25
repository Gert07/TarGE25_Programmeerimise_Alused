def string_exercise():
    """1. Ülesanne, loo muutuja first_name ja last_name"""
    first_name = "James"
    last_name = "Bond"
    """2. Ülesanne, loo muutuja full_name"""
    full_name = first_name + " " + last_name
    print(full_name)
    self_description_sentence = f"My name is {last_name}, {first_name} {last_name}."
    print(self_description_sentence)
    """3. Ülesanne, loo muutuja cake"""
    cake = "vahukoormarjadtäidispõhi"
    print(cake.replace("vahukoor", "vahukoor\n")
          .replace("marjad", "marjad\n")
          .replace("täidis", "täidis\n"))
    """4. Ülesanne, sõnede tükeldamine"""
    original_string = "Programming is fun!"
    backwards = original_string[::-1]
    every_other = original_string[::2]
    first_word_reversed = original_string[:11][::-1]
    print(first_word_reversed)
    print(backwards)
    print(every_other)

cake = "vahukoormarjatäidispõhi"
print(cake.replace("vahukoor", "vahukoor\n")
      .replace("marjad", "marjad\n")
      .replace("täidis", "täidis\n")
      .replace("põhi", "põhi\n"))

if __name__ == '__main__':
    string_exercise()