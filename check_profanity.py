import urllib

def read_text():
    quotes = open ('G:\MK1\Documents\Python Practice\profanity-check.txt')
    contents_of_life = quotes.read()
    print(contents_of_life)
    quotes.close()
    check_profanity(contents_of_life)

def check_profanity(text_to_check):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=shot')
    output = connection.read()
    print(output)
    connection.close()
    if output is True :
        print('Profanity ALert')
    else :
        print('Document looks fine')

read_text()