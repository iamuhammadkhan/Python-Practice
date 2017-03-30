import os

def rename_files():

    file_list = os.listdir(r'C:\Users\MK.HajjUmraDirect\Downloads\prank')
    saved_path = os.getcwd()
    print('Current working directory +', saved_path)
    os.chdir(r'C:\Users\MK.HajjUmraDirect\Downloads\prank')
    for file_name in file_list:
        os.rename(file_name, file_name.translate('0123456789'))
    os.chdir(saved_path)
rename_files()
