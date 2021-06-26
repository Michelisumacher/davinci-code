import requests, json, random, time, socket, platform

timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")
nameid = "VicRoesems"
repoid = "Jar-Runtime"
yamlid = "generate-code"
f = open("./README.md", "w")
f.write(f'''

<a href="https://github.com/{nameid}"><h3 align="center"><b>{nameid}</b></h3></a>

<h3 align="center">Have a nice day!</h3>

<p align="center">

  
<p align="left"> <img src="https://komarev.com/ghpvc/?username=scallions&label=Profile%20views&color=0e75b6&style=flat" alt="scallions" /> </p>

#### This Page Create at:

```bash

{timestr}

```

#### Create By Machine:

```bash

Host Name : {socket.gethostname()}

platform  : {platform.platform()}

Ip Local  : {socket.gethostbyname(socket.gethostname())}

```

[![build_firmware](https://github.com/{nameid}/{nameid}/actions/workflows/generate_readme.yml/badge.svg)](https://github.com/{nameid}/{nameid}/actions/workflows/generate_readme.yml) [![{yamlid}](https://github.com/{nameid}/{repoid}/actions/workflows/{yamlid}.yml/badge.svg)](https://github.com/{nameid}/{repoid}/actions/workflows/{yamlid}.yml)

#### Download This code Here:

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/{nameid}/{repoid}?style=for-the-badge&label=Download)](https://github.com/{nameid}/{repoid}/releases) 

</p> 

#### About Me :

```bash

<h3 align="left">🧑🏻‍💻 Languages and Tools:</h3>
<p align="left"> <a href="https://www.w3schools.com/cpp/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="cplusplus" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://pytorch.org/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a></p>


```

''')
f.close()
