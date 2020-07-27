
'''
def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on jp"
    time.sleep(4)
    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("Book")

search.close()
search.send("jp")
# input("press any key")
# search.send("harry and")
# input("press any key")
# search.send("thi si")
# input("press any key")
# search.send("joker")
'''
def searcher():
    list1=[]
    for i in range(1,6):
        filename = f"Letter{i}.txt"
        with open(filename,'r') as f:
            list1.append(f.read())
            f.close()

    print(list1)

    while True:
        text = (yield)
        if text in list1:
            print("text found")
        else:
            print("Text not found")

search = searcher()
next(search)
search.send("Yogesh")
search.close()
