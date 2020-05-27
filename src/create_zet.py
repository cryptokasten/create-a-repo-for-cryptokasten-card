#!/usr/bin/env python

import os
import sys
import secret

from jinja2 import Template

tpl = """#+TITLE: {{ title }}
#+OPTIONS: ^:nil
#+PROPERTY: header-args:sh :session *shell {{ slug }} sh* :results silent raw
#+PROPERTY: header-args:python :session *shell {{ slug }} python* :results silent raw

 ** System environment

 ** References

"""

LIB_DIR = "/data/Lab"

def convert_title_to_file_name(title, delimeter="-"):
    res = []
    tmp = ""
    for c in title:
        if c.isalnum():
            tmp += c.lower()
        else:
            if tmp:
                res.append(tmp)
            tmp = ""
    if tmp:
        res.append(tmp)
    return delimeter.join(res)

def create_zet(title):
    slug = convert_title_to_file_name(title)
    dirname = os.path.join(LIB_DIR, slug)
    # create dir
    os.mkdir(dirname)
    # create README.org
    fn = os.path.join(dirname, "README.org")
    t = Template(tpl)
    content = t.render(title=title, slug=slug)
    f = open(fn, "wt")
    f.write(content)
    f.close()

if __name__ == '__main__':
    create_zet(sys.argv[1])
