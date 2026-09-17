from pathlib import Path

path = Path("note")
print(path.exists()) #// True cuz it exist
print(path.mkdir()) #// return none cuz it create the new directories

