#!/usr/bin/env python
import os
import sys
from github import Github

print("Hello\n")
# path = os.getcwd()
# path= path+"/000Test"
path = "D:/Projects/"
url = "www.github.com/login"
username="iamthecubixnerd5@gmail.com"
password="Souptik5!"

# print("the current working directorhy is: %s" %path)


def create():
    folder_name= str(sys.argv[1])

    # try:
    #     os.makedirs(path+ str(folder_name))
    # except OSError:
    #     print("Creation of directory %s failed." % path)
    # else:
    #     print("Successfully created the directory %s ." % path)

    os.makedirs(path+ str(folder_name)  
    g = Github(username, password)
    user= g.get_user()
    repo = user.create_repo(folder_name)
    print("Succesfully created repository {}".format(folder_name))
    )

if __name__ == "__main__":
    create()
