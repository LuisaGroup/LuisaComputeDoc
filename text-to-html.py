f = open("text.txt", "r")
read_str = f.read()
f.close()
read_str = "<p>\n" + read_str.replace('\r', '').replace('\n ', '\n&nbsp').replace('<', "&lt;").replace('>', "&gt;").replace('\n', "<br>\n") + "</p>\n"
f = open("html.txt", "w")
f.write(read_str)
f.close()