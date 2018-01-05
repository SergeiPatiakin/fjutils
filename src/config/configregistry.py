from fj.nameresolver import NameResolver
from config.git import GitConfig
from config.subl3 import Subl3Config
from config.bash import BashConfig
from config.vim import VimConfig

config_classes = NameResolver({
    GitConfig: ['git'],
    Subl3Config: ['subl', 'subl3'],
    BashConfig: ['bash'],
    VimConfig: ['vim', 'vi'],
})
