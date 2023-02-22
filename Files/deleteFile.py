import os
import shutil

path = "folder"

try:
    # os.remove(path)
    # os.rmdir(path)        # this one will not delete a directory which is not empty
    shutil.rmtree(path)     # delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path + " was deleted")
