file = open('essay.txt', 'r')
content = file.read()
characters = len(content)
print(f"{characters}\n {content.title()}")
