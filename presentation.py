#! /usr/bin/python3
"""Presentation software by Paul Ross (c) 2017
Usage:
python3 presentation.py
<cr>  - Next slide.
b<cr> - Previous slide.
q<cr> - Quit
r<cr> - Refresh display (useful after resizing the command line). 
"""
import shutil

PRES = [
    [
        'Tracing in Production',
        '',
        'by Paul Ross',
    ],
    [
        'Python 3.6 has dtrace support!',
    ],
    [
        'Building Python 3.6 with dtrace support',
        '---------------------------------------',
        '',
        'cd ~/tmp                                                                         ',
        'curl -o Python-3.6.1.tgz https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz',
        'tar -xzf Python-3.6.1.tgz                                                        ',
        'cd Python-3.6.1                                                                  ',
        './configure --with-dtrace                                                        ',
        'make                                                                             ',
        'python.exe -m venv ~/venvs/dtrace                                                ',
        '. ~/venvs/dtrace/bin/activate                                                    ',
    ],
    [
        'Live demo!',
    ],
    [
        'What about Linux?',
        '',
        'stap - system tap.',
        'The good news: eBPF - Linux 4.x kernels',
    ],
    [
        'Thanks!',
        '',
        '',
        '(if we got this far then the demo probably wasn\'t a complete disaster)',
        '',
        '',
        'https://github.com/paulross/dtrace_demo',
    ],
]

def cls(r):
    for i in range(r):
        print()

def main():
    slide = 0
    while True:
        c, r = shutil.get_terminal_size()
        rows = len(PRES[slide])
        for i in range((r - rows) // 2):
            print()
        for line in PRES[slide]:
            print(line.center(c))
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
            c, r = shutil.get_terminal_size()
            cls(r)
            pass
        else:
            slide += 1
            if slide >= len(PRES):
                cls(r)
                break
    return 0


if __name__ == '__main__':
    exit(main())

