
def split_string(size: int, text: str) -> list:
    words = []
    txt = text.split(" ")
    for x in txt:
        if len(x) > size:
            words.append(x)
    return words


sample_text = "The brown fox jumps over the lazy dog"
n = 3

print(split_string(n, sample_text))

