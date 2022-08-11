

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
    rm -rf ./plugins && rm -rf ./* && rm -rf ./.gitignore && rm -rf ./.git
} 

_UpSource() {
    echo 'Github: Updating Your INFINIX With ItzSjDude/Infinix' 
    git clone https://github.com/ItzSjDude/infinix ./ &> /dev/null
    git clone -b Beta https://github.com/ItzSjDude/PikaBotPlugins ./Temp &> /dev/null
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
