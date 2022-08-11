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
    rm -rf .* 
} 

_UpSource() {
    echo 'Github: Updating Your INFINIX With ItzSjDude/Infinix'      
    git clone -b main https://github.com/ItzSjDude/infinix.git ./tmp
    cp ./tmp/* ./ && rm -rf ./tmp/*
    git clone -b Beta https://github.com/ItzSjDude/PikaBotPlugins ./tmp
    mkdir ./plugins
    cp ./tmp/plugins/*.py ./plugins
    rm -rf ./tmp
}


StartUp() {
    _logo
    _CleanUp
    _UpSource
    python3 -m INFINIX
}
