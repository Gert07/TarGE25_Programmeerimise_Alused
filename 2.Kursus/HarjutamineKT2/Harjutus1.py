def print_out_list():
    #list
    salat_ingredients = ["potato", "cucumber", "mayonnaise", "tomato"]
    #printing out list values under each other
    for ingredients in salat_ingredients:
        print(ingredients)

def checking_for_vowels():
    #list
    words = ["sky", "apple", "rhythm", "fly", "orange"]
    #taking each word from list
    for word in words:
        #taking each letter from word
        for letter in word:
            #checking if word contains letters aeiou
            if letter.lower() in "aeiou":
                print(f"{word} contains the vowel {letter}")
                break
        else:
            print(f"{word} has no vowels")

def enumerate_lists():
    #lists
    words = ["sky", "apple", "rhythm", "fly", "orange"]
    #putting index for a word in the list (if you put number after enumerate list, it starts counting from that number)
    for index, word in enumerate(words, 1):
        print(f"Index {index} and language {word}")

def zip_lists():
    words = ["sky", "apple", "rhythm", "fly", "orange"]
    ids = [1, 2, 3, 4, 5]
    #adding 2 lists together
    for word, id in zip(words, ids):
        print(f"Word is {word}")
        print(f"Id is {id}")

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


if __name__ == "__main__":
