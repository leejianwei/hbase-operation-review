import os
from zipfile import ZipFile

def archive_files(output_dir):
    compressed_files = output_dir + ".zip"
    parent_folder = os.path.dirname(output_dir)
    with ZipFile(compressed_files, 'w') as zipObj:
        for folderName, subfolders, filenames in os.walk(output_dir):
            for filename in subfolders:
                absolute_path = os.path.join(folderName, filename)
                relative_path = absolute_path.replace(parent_folder + '\\','')
                print("Adding '%s' to archive." % absolute_path)
                zipObj.write(absolute_path, relative_path)
            for filename in filenames:
                absolute_path = os.path.join(folderName, filename)
                relative_path = absolute_path.replace(parent_folder + '\\','')
                print("Adding '%s' to archive." % absolute_path)
                zipObj.write(absolute_path, relative_path)

archive_files("./output")