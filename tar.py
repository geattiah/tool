import os
import argparse
import tarfile

output = "/home/gift/Documents/Landsat/2001_data/extracted"


def main(runDir):
    # list all subdirectories:
    allSubContents = os.listdir(runDir)

    year = str(os.path.basename(os.path.normpath(runDir)))
    storage = os.path.join(output,year)
    if not os.path.exists(storage):
        os.mkdir(storage)

    for files in allSubContents: 
        name = os.path.splitext(files)[0]
        base = os.path.splitext(name)[0]
        #print(base)
        location = os.path.join(storage,base)
        if not os.path.exists(location):
            os.mkdir(location)
        filename = os.path.join(runDir,files)   
        tar = tarfile.open(filename)
        tar.extractall(path=location)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
        For creating temperature from Landsat 8
    """)
    parser.add_argument('rundir',
                        type=str,
                        help="The path to the run directory with the landsat files")
    args = parser.parse_args()
    main(os.path.abspath(args.rundir)) 