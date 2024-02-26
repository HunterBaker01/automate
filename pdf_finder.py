import os, shutil

for folderName, subfolders, filenames in os.walk('test'):
    for subfolder in subfolders:
        for filename in filenames:
            if filename.endswith('.pdf') or filename.endswith('.jpg'):
                abs = os.path.abspath(folderName + subfolder + filename)
                # shutil.copy(abs, '/Users/hunterbaker/python/automate/find_pdf/test_copy')
                print(abs)