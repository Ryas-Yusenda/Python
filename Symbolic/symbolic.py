# mklink X:\Github\Scaping\google-maps-scrapping X:\JavaScript\google-maps-scrapping /j


import os

print(os.getcwd())
while True:
    folder_path = input("Enter Folder Path: ").replace('"', "")

    folder_path_last = folder_path.split("\\")[-1]

    if os.path.exists(folder_path_last):
        print("Folder Path Exists")
    else:
        # make symbolic link
        to = os.path.join(os.getcwd(), folder_path_last)
        from_ = folder_path

        syntax = 'mklink /J "{}" "{}"'.format(to, from_)
        os.system(syntax)
