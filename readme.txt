Building an application for desktop mainly. Figured i'd package it for android as well. This is a template i am putting together to make future projects like this easier. Havent uploaded anything from the actuall application i am working on.

the apk is packaged in the root dir. the pyinstaller application is packagted in the winfreeze folder

  THE ZIP FOLDER HAS THE FILE STRUCTURE FOR THE APPLICATION. SEPERATE .SPEC FILE 

1)uses bootflat as the css framework. can use bootstrap too
2)sqlalchemy as the database
3)wtforms for forms
4)buildozer for the apk webview
5)pyinstaller for the exe webview


--------------------------------------------------

#pyinstaller some basic useful commands --onefile creates 1 file executable. #was having issues getting the sqlite file updated though.
#writes static and templates into the .spec folder -n changes the name --hidden to whitelist libraries --icon to change icon

pyinstaller -w --add-data "templates:templates" --add-data "static:static" -n 'BookMahks' --hidden-import=sqlite3 --hidden-import=sqlalchemy --icon ".web.ico" --clean main.py

#basic usage for creating application with buildozer loglevel=2 for more output

buildozer android clean
buildozer android debug
---------------------------------------------------
#work in process still need some comments in actuall code
#added a jinja extends style html page.

