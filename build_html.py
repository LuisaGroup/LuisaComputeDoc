import markdown as md
from pathlib import Path
import os
programPath = Path.cwd()
root_dir = "html"


def makedir(path: str):
    if not os.path.exists(path):
        os.mkdir(path)


def html_path(md_path: str):
    new_path = ""
    for i in md_path:
        if i == '\\':
            new_path += '/'
        else:
            new_path += i
    elements = new_path.split('/')
    folder = root_dir + '/'
    if len(elements) <= 1:
        return folder + new_path.replace('.md', '.html')
    for i in range(len(elements) - 1):
        folder += elements[i] + '/'
        makedir(folder)
    folder += elements[len(elements) - 1].replace('.md', '.html')
    return folder


if __name__ == '__main__':
    makedir(root_dir)
    for path in Path('.').rglob('*.md'):
        pt = path.absolute()
        new_path = html_path(str(pt.relative_to(programPath)))
        f = open(pt, "r", encoding="utf-8")
        s = f.read()
        f.close()
        html = md.markdown(s)
        f = open(new_path, "w", encoding="utf-8")
        f.write(html)
        f.close()
