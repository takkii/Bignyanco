import re
import os.path
import sys
from .base import Base

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'Bignyanco'
        self.mark = '[neko_dictionary]'
        self.input_pattern = (r'^ruby\.')

    def get_complete_position(self, context):
        m = re.search(r'[^. *\t]\w*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        fi = open(os.path.expanduser('~/.config/nvim/repos/github.com/takkii/Bignyanco/complete/ruby_complete'),'r',encoding='utf-8')
        for line in fi:
        return (line, end=" ")
        fi.close()