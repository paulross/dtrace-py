#! /usr/bin/python3
"""Presentation software by Paul Ross (c) 2017
Usage:
python3 presentation.py
<cr>  - Next slide.
b<cr> - Previous slide.
q<cr> - Quit
r<cr> - Refresh display (useful after resizing the command line). 
"""
import collections
import shutil

HELP_TEXT = """<cr>  - Next slide.
b<cr> - Previous slide.
q<cr> - Quit
r<cr> - Refresh display (useful after resizing the command line). 
?<cr> - This help text.
"""

# -1 left aligned, 0 centred, 1 right aligned
TextAlign = collections.namedtuple('TextAlign', 'text, align')

PRES = (
    TextAlign((
        'Dynamic Tracing With Python',
        '',
        'by Paul Ross',
        '',
        'All of this is on GitHub!', 
    ), 0),
    TextAlign((
        'Python 3.6/3.7 has dtrace support!',
    ), 0),
    TextAlign((
        'Building Python 3.7 with dtrace support',
        '---------------------------------------',
        '',
        'cd ~/tmp',
        'curl -o Python-3.7.0.tgz \\',
        '    https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz',
        'tar -xzf Python-3.7.0.tgz',
        'cd Python-3.7.0',
        './configure --with-dtrace',
        'make',
        'python.exe -m venv ~/venvs/dtrace',
        '. ~/venvs/dtrace/bin/activate',
    ), -1),
    TextAlign((
        'Live demo!',
    ), 0),
    TextAlign((
        'Thanks!',
        '',
        '',
        '(if we got this far then the demo',
        'probably wasn\'t a complete disaster!)',
        '',
        '',
        'https://github.com/paulross/dtrace-py',
    ), 0),
)

def cls(r):
    for i in range(r):
        print()

def main():
    slide = 0
    while True:
        c, r = shutil.get_terminal_size()
        text, align = PRES[slide]
        rows = len(text)
        for i in range((r - rows) // 2):
            print()
        for line in text:
            if align == -1:
                print(line)
            elif align == 0:
                print(line.center(c))
            elif align == 1:
                print(' ' * (r - rows) + line)
            else:
                assert 0
        for i in range((r - rows) // 2):
            print()
        user = input('')
        if user == 'q':
            cls(r)
            break
        elif user == 'b':
            if slide > 0:
                slide -= 1
        elif user == 'r':
            cls(r)
        elif user == '?':
            cls(r)
            print(HELP_TEXT)
            user = input('<cr> to continue...')
            cls(r)
        else:
            slide += 1
            if slide >= len(PRES):
                cls(r)
                break
    return 0


if __name__ == '__main__':
    exit(main())

