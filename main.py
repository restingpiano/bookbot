

def getText(file_path):
    with open(file_path) as f:
        words = f.read()

    return words

file_path = "books/frankenstein.txt"
text = getText(file_path)

def word_count(file_path):
    with open(file_path) as f:
        words = f.read()
        word_list = words.split()

    return len(word_list)

def char_count(text):
        chars = text
        chars = chars.lower()

        char_count = {}

        for i in chars:
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1

        #print(char_count)
        return char_count

def sort_on(dict):
     return dict["num"]

def char_count_report(text):
     count_dict = char_count(text)

     word_list =[]

     for i in count_dict:
          word_part_dict = {}
          #word_part_dict[i] = count_dict[i]
          letter = i 
          value = count_dict[i]

          word_part_dict["key"] = letter
          word_part_dict["num"] = value

          word_list.append(word_part_dict)

     word_list.sort(key=sort_on, reverse=True)

     print("--- Begin report of books/frankenstein.txt ---")
     print(str(word_count(file_path))+" words found in the document")
     print("")

     for i in range(0, len(word_list)):
          if word_list[i]["key"].isalpha():
            print("The '"+word_list[i]["key"]+"' character was found "+str(word_list[i]["num"])+" times")
 
     print("-- End report --")

#word_count(file_path)
#char_count(text)
char_count_report(text)