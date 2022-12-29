import markdown as md
from pathlib import Path
import os
style_header = '''<!DOCTYPE html>
<style>
#carbonads {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu,
  Cantarell, "Helvetica Neue", Helvetica, Arial, sans-serif;
}

#carbonads {
  display: flex;
  max-width: 330px;
  background-color: hsl(0, 0%, 98%);
  box-shadow: 0 1px 4px 1px hsla(0, 0%, 0%, .1);
}

#carbonads a {
  color: inherit;
  text-decoration: none;
}

#carbonads a:hover {
  color: inherit;
}

#carbonads span {
  position: relative;
  display: block;
  overflow: hidden;
}

#carbonads .carbon-wrap {
  display: flex;
}

.carbon-img {
  display: block;
  margin: 0;
  line-height: 1;
}

.carbon-img img {
  display: block;
}

.carbon-text {
  font-size: 13px;
  padding: 10px;
  line-height: 1.5;
  text-align: left;
}

.carbon-poweredby {
  display: block;
  padding: 8px 10px;
  background: repeating-linear-gradient(-45deg, transparent, transparent 5px, hsla(0, 0%, 0%, .025) 5px, hsla(0, 0%, 0%, .025) 10px) hsla(203, 11%, 95%, .4);
  text-align: center;
  text-transform: uppercase;
  letter-spacing: .5px;
  font-weight: 600;
  font-size: 9px;
  line-height: 1;
}
img {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 5px;
  width: 1500px;
}
</style>
'''
programPath = str(Path.cwd())
root_dirs = ["en-us", "zh-cn"]


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
    makedir(html_rootpath)
    local_path = programPath + '/' + root_dir
    for path in Path(root_dir).rglob('*.md'):
        pt = path.absolute()
        new_path = html_path(str(pt.relative_to(local_path)), html_rootpath)
        f = open(pt, "r", encoding="utf-8")
        s = f.read()
        f.close()
        html = md.markdown(s)
        f = open(new_path, "w", encoding="utf-8")
        f.write(style_header)
        f.write(html)
        f.close()


if __name__ == '__main__':
    for i in root_dirs:
        process_path(i)
