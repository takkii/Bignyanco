import re
import os.path
from .base import Base

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'Nekodaruma2'
        self.filetypes = ['ruby']
        self.mark = '[neo_dictionary]'
        self.rank = 450
        
    def get_complete_position(self, context):
        m = re.search(r'[^. *\t]\w*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        fi = open(os.path.expanduser('~/.config/nvim/repos/github.com/takkii/Bignyanco/complete/ruby_complete'),'r')
        line = fi.readline()
        fi.close()
        return line