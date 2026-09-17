from pathlib import Path

path = Path("note")
print(path.exists()) #// True cuz it exist
print(path.mkdir()) #// return none cuz it create the new directories , can delete through this command "rmdir()"

# search all the files 
path = Path()
for file in path.glob('*.py'):
    print(file)
