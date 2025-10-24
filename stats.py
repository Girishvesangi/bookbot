def get_book_text(filepath):
    with open(filepath) as f:
         return f.read()



def count_words(text):
    words=text.split()
    return len(words)

def count_chars(text):
    dict_chars={}
    
    for i in text:
        i=i.lower()
        dict_chars[i]=dict_chars.get(i,0)+1
    return dict_chars

def sort_dict(dict):
    l=[]
    for i in dict.keys():
        l.append({"char": i,"num": dict[i]})
    l.sort(reverse=True, key=sort_on)
    return l


def sort_on(items):
    return items["num"]
