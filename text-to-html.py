f = open("text.txt", "r", encoding="utf8")
read_str = f.read()
f.close()
read_str = "<p>\n" + read_str.replace('\r\n', '\n').replace('\n ', '\n&nbsp').replace('<', "&lt;").replace('>', "&gt;").replace('\n', "<br>\n") + "</p>\n"
f = open("html.txt", "w", encoding="utf8")
f.write(read_str)
f.close()