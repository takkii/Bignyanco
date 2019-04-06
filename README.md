[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)[![GitHub release](https://img.shields.io/github/release/takkii/Bignyanco.svg?style=flat)](GitHub)[![GitHub Status](https://img.shields.io/github/last-commit/takkii/Bignyanco.svg?style=flat)](GitHub)

<div style="text-align: center;">
![蛇とるびー](https://github.com/takkii/Bignyanco/blob/master/images/python_ruby.gif)
</div>

## Bignyanco is neovim plugins. 

※ Bignyanco is the neovim plugins. However, if deoplete moves, it works with the vim plugins. 

*Enviroments PC is Windows, Mac, Linux kernel etc.*

#### Bignyanco converted the dictionary word of [ruby-dictionary3](https://github.com/takkii/ruby-dictionary3) as a neovim plugins.

※ The html completion list has moved to 'takkii/bistro' dein repo here.

・Operating environment

```text
neovim
python3
deoplete.nvim
$XDG_CONFIG_HOME=~/.config/nvim (default)
let g:python3_host_prog='path contain python shell' 

(iTerm or Terminal CUI enviroments, Don't need to add python3_host_prog. To init.vim or .vimrc)

(neovim-qt etc GUI enviroments, Need to add python3_host_prog and python_host_prog. To init.vim or .vimrc)
```

## If dein plugin manager using ? 

```
init.vim

call dein#add('takkii/Bignyanco')

or

dein.toml

[[plugins]]
repo = 'takkii/Bignyanco'
```

*Becase init.vim add.*

```text
deoplete running, 

Bignyanco is listing [neo_dictionary].
```


![ねこだるま](https://github.com/takkii/Bignyanco/blob/master/images/nekodaruma.jpg)![闇炎のねこだるま](https://github.com/takkii/Bignyanco/blob/master/images/nekodaruma2.jpg)![殺意の波動に目覚めたねこだるま](https://github.com/takkii/Bignyanco/blob/master/images/nekodaruma3.jpg)

### Japanese say, Sample moving picture.

*Windows10 + WSL + WSL-terminal*

![動画ねこだるま](https://github.com/takkii/Bignyanco/blob/master/images/neo_nekodaruma.gif)

Author Takayuki Kamiyama.