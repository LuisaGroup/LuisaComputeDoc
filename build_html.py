import markdown as md
from pathlib import Path
import os
import shutil
style_header = '''<!DOCTYPE html>
<style>
img {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 5px;
  max-width:100%;
  max-height:100%;
}
</style>
'''
programPath = str(Path.cwd())
root_dirs = ["en-us", "zh-cn"]
replace_str = [
  ("IMAGE_DIR", "../../image"),
  ("  ", "&nbsp&nbsp")
]

def makedir(path: str):
    if not os.path.exists(path):
        os.mkdir(path)


def html_path(md_path: str, new_dir: str):
    new_path = ""
    for i in md_path:
        if i == '\\':
            new_path += '/'
        else:
            new_path += i
    elements = new_path.split('/')
    folder = new_dir + '/'
    if len(elements) <= 1:
        return folder + new_path.replace('.md', '.html')
    for i in range(len(elements) - 1):
        folder += elements[i] + '/'
        makedir(folder)
    folder += elements[len(elements) - 1].replace('.md', '.html')
    return folder


def process_path(root_dir: str):
    if not os.path.exists(root_dir):
        return
    html_rootpath = root_dir + "-html"
    if os.path.exists(html_rootpath):
        shutil.rmtree(html_rootpath)
    makedir(html_rootpath)
    local_path = programPath + '/' + root_dir
    for path in Path(root_dir).rglob('*.md'):
        pt = path.absolute()
        new_path = html_path(str(pt.relative_to(local_path)), html_rootpath)
        f = open(pt, "r", encoding="utf-8")
        s = f.read()
        f.close()
        for rps in replace_str:
          s = s.replace(rps[0], rps[1])
        html = md.markdown(s)
        f = open(new_path, "w", encoding="utf-8")
        f.write(style_header)
        f.write(html)
        f.close()


if __name__ == '__main__':
    for i in root_dirs:
        process_path(i)
