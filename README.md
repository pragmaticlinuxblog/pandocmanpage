# PandocManPage
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Example files for creating a MAN page, written in Markdown, for your own program of script. With the help of [Pandoc](https://pandoc.org/), you can convert it to a properly *groff* formatted MAN page.

In the `source/` directory you can find a Python script called `hello.py`. It is a simple *Hello world* type program. The program accepts two command line parameters:

* `-h` to display its help message.
* `-n` to specify a name of the person to greet.

For example, you can run it as: `./hello.py -n Joe` and it will output `Hello, Joe!`

In the `docs/` directory you can find `hello.1.md`. It is the MAN page written in Markdown. You can use Pandoc to convert it into a *groff* formatted MAN page: `pandoc hello.1.md -s -t man -o hello.1`.

Pandoc then creates the `hello.1` file. To find out what the actual MAN page looks like, you can run: `man -l hello.1`.