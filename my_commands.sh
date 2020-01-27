#i/bin/bash

#prints the input
# echo "String";
# python create.py;
function create(){
    cd
    python create.py $1
    echo $1
    cd D:/Projects/$1
    ls
    # python create.py $1
    # git init
    # git remote add origin git@github.com:souptik5/$1.git
    # touch README.md
    # git add .
    # git commit -m "Initial commit"
    # git push -u origin master
    # code .
}
# create TEST;