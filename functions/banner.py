def banner_text(text, screen_width=80):
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width"
                         .format(text, screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


width = 55

banner_text("*", width)
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing")
banner_text("*", width)