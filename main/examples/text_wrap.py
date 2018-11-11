from textwrap import wrap

text = "my text repeated several times because why not." * 80
wrapped = "\n".join(wrap(text, width=70))

print(wrapped)
