import sys
import os
import time
import shutil

#from directory
go_pro_directory = '/Volumes/gopro_512/DCIM/100GOPRO'

#to directory
backup_directory_base = '/Volumes/T7'

def main(episode):
    for filename in os.listdir(go_pro_directory):
        f = os.path.join(go_pro_directory, filename)

        if not os.path.isfile(f):
            continue

        if not f.endswith(".MP4"):
            continue

        modified_date_epoch = os.path.getmtime(f)
        modified_date = time.strftime('%Y-%m-%d', time.localtime(modified_date_epoch))
        backup_directory_with_episode = backup_directory_base + "/" + episode
        full_backup_directory = backup_directory_with_episode + "/" + modified_date

        if not os.path.isdir(backup_directory_with_episode):
            os.mkdir(backup_directory_with_episode)

        if not os.path.isdir(full_backup_directory):
            os.mkdir(full_backup_directory)

        target_backup_path = full_backup_directory + "/" + filename

        if os.path.isfile(target_backup_path):
            continue

        print ("copying: " + filename)
        shutil.copy2(f, target_backup_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("error: please specify an episode")
        print("example: 'python3 backup_photos.py episode_13'")
        exit(1)
    main(sys.argv[1])