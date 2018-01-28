import os

def get_latest_image(dirpath, valid_extensions=('jpg','jpeg','png')):
    """
    Get the latest image file in the given directory
    """

    # get filepaths of all files and dirs in the given dir
    valid_files = [os.path.join(dirpath, filename) for filename in os.listdir(dirpath)]
    # filter out directories, no-extension, and wrong extension files
    valid_files = [f for f in valid_files if '.' in f and \
        f.rsplit('.',1)[-1] in valid_extensions and os.path.isfile(f)]

    if not valid_files:
        raise ValueError("No valid images in %s" % dirpath)

    print(max(valid_files, key=os.path.getmtime))
    print("hello")
    return max(valid_files, key=os.path.getmtime)
#print(get_latest_image)
get_latest_image("/Users/caitlinschmuck/Desktop/sheinnovatesnew", valid_extensions='jpg')
print("hello1")
