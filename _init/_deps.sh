#!/bin/bash
_logo() {
    echo '
    ┏━━┓╋╋╋╋┏━┓┏┓╋╋╋╋┏┓
    ┗┃┃┛┏━┳┓┃━┫┣┫┏━┳┓┣┫┏┳┓
    ┏┃┃┓┃┃┃┃┃┏┛┃┃┃┃┃┃┃┃┣┃┫
    ┗━━┛┗┻━┛┗┛╋┗┛┗┻━┛┗┛┗┻┛
    '
}

_CleanUp() {
    echo 'Cleanup : Cleaning old source'
    rm -rf ./* && rm -rf *
} 

_UpSource() {
    echo 'Github: Updating Your INFINIX With ItzSjDude/Infinix' 
    git init .     
    git remote add origin https://github.com/ItzSjDude/infinix.git  
    git pull origin main --allow-unrelated-histories
    git clone -b Beta https://github.com/ItzSjDude/PikaBotPlugins ./Temp
    mkdir ./plugins
    cp ./Temp/plugins/*.py ./plugins
    rm -rf ./Temp
}


StartUp() {
    _logo
    _CleanUp
    _UpSource
    python3 -m INFINIX
}
