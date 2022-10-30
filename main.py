import os
import shutil
from datetime import datetime

# get public desktop path
desktop_public_path = os.path.join(os.path.join(os.environ['public']), 'Desktop')

# get public desktop files
files_public = os.listdir(desktop_public_path)

# get or create backup public desktop path
backup_public_path = os.path.join(desktop_public_path, f"backup_public_desktop#")
if not os.path.exists(backup_public_path):
    os.makedirs(backup_public_path)

# move files
for file in files_public:
    if "#" in file:
        continue
    file_path = os.path.join(desktop_public_path, file)
    file_backup_path = os.path.join(backup_public_path, file)
    shutil.move(file_path, file_backup_path)

# get user desktop
desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

files = os.listdir(desktop_path)

now = datetime.now()
backup_path = os.path.join(desktop_path, f"backup_desktop#/{now.strftime('%Y%m%d-%H%M%S')}")
if not os.path.exists(backup_path):
    os.makedirs(backup_path)

for file in files:
    if "#" in file:
        continue
    file_path = os.path.join(desktop_path, file)
    file_backup_path = os.path.join(backup_path, file)
    shutil.move(file_path, file_backup_path)
