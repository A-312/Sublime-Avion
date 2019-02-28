import sublime
import sublime_plugin

import os
import re
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    attr = {}
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            self.attr[attr[0]] = attr[1]


class AvionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        line = self.view.substr(self.view.line(self.view.sel()[0]))
        regex = r'^(\s*)(?:(?:\#|\/\/)\s?)?(<!--|\/\*)(.*)(-->|\/\*)$'
        match = re.match(regex, line)

        if match is not None:
            line = re.sub(regex, r'<img \g<3>>', line)

            parser = MyHTMLParser()
            parser.feed(line)

            if not ('path' in parser.attr and 'template' in parser.attr):
                return sublime.status_message('Need 2 arguments path and template.')

            indent = match.group(1)

            template = parser.attr['template']

            prepath = os.path.dirname(self.view.file_name()) + '/'
            prepath = os.path.abspath(prepath + (parser.attr['pre'] or ''))

            path = prepath + '/' + parser.attr['path']
            path = os.path.abspath(path)

            position = self.view.line(self.view.sel()[0]).end()

            output = ''

            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    src = os.path.relpath(os.path.join(root, name), prepath)
                    src = src.replace('\\', '/')
                    src = ('', '/')[parser.attr['path'][0] == '/'] + src
                    output += printTemplate(indent, src, template)

            self.view.insert(edit, position, '\n' + output)
            sublime.status_message('ok')
        else:
            sublime.status_message('Comment not match.')


def printTemplate(indent, src, template):
    output = indent + template.format(src) + '\n'
    return output
