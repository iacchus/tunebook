#!/usr/bin/env python

import os
import glob
# use os.system("") to do it lil boy

def return_html(what=""):
    return """
    <!DOCTYPE html>
    <html lang="en">
      <head>

        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1">

        <title>My Tunebook</title>

        <link rel="stylesheet" href="index_files/style.css">

        <script src="index_files/jquery-latest.js"></script>
        <script src="index_files/abcjs_basic_2.3-min.js"></script>

        <script src="index_files/script.js"></script>

      </head>
      <body>
        <div id="page-container">
          <h1>Mercurii Tunebook</h1>

          <div id="presentation">
            <a href="https://github.com/iacchus/tunebook/">GitHub</a> – <a href="https://iacchus.github.io">Website</a><br/><br/>
          </div>

          <div id="files">
    {0}
          </div> 
        </div>
      </body>
    </html>
""".format(what)

print("Listing ABC files..")
abc_files = glob.glob('abc/*.abc', recursive=False)

tune_files = str()
abc_code_files = str()
#index_filename = "index-rendered.html"

index_abcjs_filename = "index.html"

#png_files.sort()

#print("Writing index file listing..")
#for file in png_files:
    #index_files += "<a href='{0}' data-featherlight='iframe'>{0}</a><br/>\n".format(file)
#    tune_files += "<div class='tune-container'><img src='{0}' /></div>\n".format(file)

abc_files = glob.glob('abc/*.abc', recursive=False)
abc_files.sort()

for abc_file in abc_files:
    #index_files += "<a href='{0}' data-featherlight='iframe'>{0}</a><br/>\n".format(file)
    with open(abc_file, 'r') as MYFILE:
        abc = "".join(list(MYFILE))
    abc_code_files += "<div class='tune-container' id='{0}'><pre class='abctune'>{1}</pre></div>\n".format(abc_file.split('/')[1].split('.')[0], abc)


print("Writing index file '{}'..".format(index_abcjs_filename))
with open(index_abcjs_filename,'w') as fd:
    fd.write(return_html(abc_code_files))
    fd.close()

git_commands = "git add .; git commit -a -m 'autocommit from build.py!'; git push"
print("Running git commands {}..".format(git_commands))
os.system(git_commands)

print("Done..")
