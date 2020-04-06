# -*- coding: utf-8 -*-
import chardet


def log(txt, content):
    ch = chardet.detect(content.encode('utf-8'))
    # content = content.decode(ch).encode("utf-8")
    fd = open(txt, 'a+')
    fd.write(content)
    fd.close()


if __name__ == "__main__":
    log("log.txt", "This is the test333\n")
