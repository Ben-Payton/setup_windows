import os

def check_make_existing_dir(path_to_dir):
    if not os.path.isdir(path_to_dir):
        os.mkdir(path_to_dir)
        print(f"{path_to_dir} was created.")
    else:
        print(f"{path_to_dir} already exists.")

def get_home_dirs():
    all_them = os.listdir("C:\\Users\\")
    acc = []
    for i in all_them:
        if not i in ['All Users','Default', 'Default User', 'desktop.ini', 'Public']:
            acc.append("C:\\Users\\"+i+"\\")
    return acc

def make_home_dir_folders(home_dir):
    home_dirs = ["01_Projects","02_Areas","03_Resources","04_Archive"]
    for i in home_dirs:
        current_path =f"{home_dir}{i}"
        check_make_existing_dir(current_path)

def main():
    home_dirs = get_home_dirs()
    for i in home_dirs: make_home_dir_folders(i)
main()