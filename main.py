def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lower_text= text.lower()
    num_words = get_num_words(text)
    letter_dic={}
    lower_text= text.lower()
    get_letter_count(lower_text,letter_dic)
    list_of_dics = dic_to_list(letter_dic)
    sorted_list = sort_dicts_list(list_of_dics)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    printed_list=print_in_a_list(sorted_list)
    print("--- End report ---")
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_letter_count(lower_text,letter_dic):
    for i in lower_text:
        if i.isalpha():
            if i in letter_dic:
                letter_dic[i] += 1
            else:
                letter_dic[i] = 1
    
def dic_to_list(letter_dic):
    return [{key: value} for key, value in letter_dic.items()]

def get_value(list_of_dics):
    return list(list_of_dics.values())[0]

def sort_dicts_list(dicts_list):
    dicts_list.sort(reverse=True, key=get_value)
    return dicts_list

def print_in_a_list(sorted_list):
    for dic in sorted_list:
        for key, value in dic.items():
            print(f"The '{key}' character was found {value} times")



main()


