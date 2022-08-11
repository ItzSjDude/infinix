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
    git clone https://github.com/ItzSjDude/infinix.git . 
    git clone -b Beta https://github.com/ItzSjDude/PikaBotPlugins ./Temp
    mkdir ./plugins
    cp ./Temp/plugins/*.py ./plugins
    rm -rf ./Temp
    cd infinix
}

StartUp() {
    _logo
    _CleanUp
    _UpSource
    python3 -m INFINIX
}
