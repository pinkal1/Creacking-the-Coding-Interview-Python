# Determine whether or not a given string contains no duplicate characters.

def is_Unique(string):
  characters = {}
  for char in string:
    if char in characters:
      return False
    characters[char] = True
  return True

if __name__ == "__main__":
    print is_Unique(raw_input('Please enter string:'))



