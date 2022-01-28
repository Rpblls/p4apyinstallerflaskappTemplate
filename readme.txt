the apk is packaged in the root dir. the pyinstaller application is packagted in the winfreeze folder


#pyinstaller some basic useful commands --onefile creates 1 file executable. #was having issues getting the sqlite file updated though.
#writes static and templates into the .spec folder

pyinstaller -w --add-data "templates:templates" --add-data "static:static" -n 'BookMahks' --hidden-import=sqlite3 --hidden-import=sqlalchemy --icon ".web.ico" --clean main.py

#basic usage for creating application with buildozer loglevel=2 for more output

buildozer android clean
buildozer android debug

#work in process still need some comments in actuall code
#added a jinja style html page. hide the button unused button on each page
