def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_number_of_words(text)
    chars_dict = get_each_char_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    
    print(f"---Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
        
    print("---End report ---")

def get_number_of_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
        
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_each_char_count(text):
    my_dict = {}
    string = text.lower()
    for char in string:
        if char.isalnum():  # Only count alphanumeric characters
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
    return my_dict



def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
