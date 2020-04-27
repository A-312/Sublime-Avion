# Sublime Avion

It's a Sublime Text 3 plugin with several commands / features.

# TODO

 - Add Sublime Avion in Package Control.
 - Add shortcut.
 - Make a documentation (gulp & github.io page) or github Wiki.

# Commands

## Make a file list

This command will print a file list in your folder. 

``` html
<!-- pre="{pwd}" path='{path}' template='{template}"></script>' -->
```

You can comment this line with : `# ` or `//`.

 - {pwd} : Optional parameter, by default is the file folder (-> relative path from the file folder).
   This parameter is usefull for HTML project.
 - {template} : String template for each file `{0}`.
 - {path} : File output. Recommanded : Relative url from the file folder or `{pwd}` path.

### TODO :

 - Replace old output (don't make duplicate).
 - Add more attribute (boolean) : dir, dironly, recursive, file.
 - Add regex filter include and exclude.

### Example :

#### Example 1 :

www/index.html :

``` html
<head>
    <!-- pre="../asset/" path='/javascript/chat' template='<script type="text/javascript" src="{0}"></script>'  -->
```

Output :

``` html
<head>
    <!-- pre="../asset/" path='/javascript/chat' template='<script type="text/javascript" src="{0}"></script>'  -->
    <script type="text/javascript" src="/javascript/chat/i2n/translation/en.js"></script>
    <script type="text/javascript" src="/javascript/chat/i2n/i2n.js"></script>
```

Folder :

```
asset/javascript/chat/i2n/translation/en.js
asset/javascript/chat/i2n/i2n.js
www/index.html
```

#### Example 2 :

main.py

``` py
def run():
    # <!-- path='changelog/' template='file = "{0}"'  -->
```

Output :

``` py
def run():
    # <!-- path='changelog/' template='file = "{0}"'  -->
    file = 'version1.txt'
    file = 'version2.txt'
    file = 'version3.txt'
```

Folder :

```
main.py
changelog/version1.txt
changelog/version2.txt
changelog/version3.txt
```
