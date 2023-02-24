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
  ('\r\n', '\n'),
  ("IMAGE_DIR", "../../image"),
  ("  ", "&nbsp&nbsp")
]
def text_to_html(read_str: str):
    return "<p>\n" + read_str.replace('<', "&lt;").replace('>', "&gt;").replace('\n', "<br>\n") + "</p>\n"

def inline_html(ss: str):
    result = ""
    begin = "HTML_BEGIN\n"
    end = "HTML_END\n"
    while True:
        idx = ss.find(begin)
        if idx == -1:
            result += ss
            break
        result += ss[0: idx]
        ss = ss[idx + len(begin): len(ss)]
        end_idx = ss.find(end)
        end_len = len(end)
        if end_idx == -1:
            end_idx = ss.find(end[0:len(end)-1])
            if end_idx == -1 or end_idx < len(ss) - end_len:
                raise "html begin & end must be coupled."
            end_len -= 1
        result += text_to_html(ss[0: end_idx])
        ss = ss[end_idx + end_len: len(ss)]
    return result
def inline_text(ss: str):
    result = ""
    begin = "TEXT_BEGIN\n"
    end = "TEXT_END\n"
    while True:
        idx = ss.find(begin)
        if idx == -1:
            result += ss
            break
        result += ss[0: idx]
        ss = ss[idx + len(begin): len(ss)]
        end_idx = ss.find(end)
        end_len = len(end)
        if end_idx == -1:
            end_idx = ss.find(end[0:len(end)-1])
            if end_idx == -1 or end_idx < len(ss) - end_len:
                raise "text begin & end must be coupled."
            end_len -= 1
        result += ss[0: end_idx].replace("\n", "<br>\n")
        ss = ss[end_idx + end_len: len(ss)]
    return result

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
        try:
            s = inline_text(inline_html(s))
        except TypeError:
            print("error at " + str(path))
        html = md.markdown(s)
        f = open(new_path, "w", encoding="utf-8")
        f.write(style_header)
        f.write(html)
        f.close()


if __name__ == '__main__':
    for i in root_dirs:
        process_path(i)
