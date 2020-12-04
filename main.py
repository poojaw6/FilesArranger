import os

files = os.listdir()
files.remove('main.py')

print(files)

def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


# Move files in coressponding folders
def moveFiles(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

        

if __name__ == '__main__':
       
    createFolder("Images")
    createFolder("Docs")
    createFolder("Media")
    createFolder("Others")

    imgExt = [".png", ".jpeg", ".jpg"]
    docExt = ['.txt', ".xlsx", ".xls", ".docx", ".doc", ".pdf"]
    mediaExt = [".mp3", ".mp4", ".avi", ".flv"]

    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExt]
    print(images)

    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExt]
    print(docs)

    media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExt]
    print(media)

    others = []

    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExt) and (ext not in docExt) and (ext not in mediaExt) and os.path.isfile(file):
            others.append(file)

    print(others)

    # Call move files
    moveFiles("Images", images)
    moveFiles("Docs", docs)
    moveFiles("Media", media)
    moveFiles("Others", others)
