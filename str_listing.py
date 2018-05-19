import re
import os.path

fi = open(os.path.expanduser('~/.config/nvim/repos/github.com/takkii/Bignyanco/complete/ruby_complete'),'r')
line = fi.readline()
fi.close()

print line.sort(key=to_lower)
