def python_food():
    width = 80
    text = 'spam and eggs'
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(text):
    left_margin = (80 - len(str(text))) // 2
    print(" " * left_margin, text)


# call the function
center_text("spam and eggs")
center_text('spam, spam and eggs')
center_text(121)
center_text("spam, spam, spam and eggs")
