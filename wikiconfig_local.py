import sys, os
from wikiconfig import LocalConfig

class Config(LocalConfig):
    sitename = u'Moingo'

    parent_dir = os.path.abspath('..') + '/'

    args = sys.argv[1:]

    if len(args) >= 1:
      data_name = args[0]
    else:
      data_name = 'moingo_data'
    print('serving data: ' + data_name)

    if len(args) >= 2:
      underlay_name = args[1]
    else:
      underlay_name = data_name
    print('serving underlay: ' + underlay_name)

    if len(args) >= 3:
      userbase_name = args[2]
    else:
      userbase_name = data_name
    print('serving userbase: ' + userbase_name)

    # Where your mutable wiki pages are. You want to make regular
    # backups of this directory.

    data_dir = parent_dir + data_name + '/data/'

    # Where read-only system and help page are. You might want to share
    # this directory between several wikis. When you update MoinMoin,
    # you can safely replace the underlay directory with a new one. This
    # directory is part of MoinMoin distribution, you don't have to
    # backup it.

    data_underlay_dir = parent_dir + underlay_name + '/underlay/'

    # The URL prefix we use to access the static stuff (img, css, js).
    # NOT touching this is maybe the best way to handle this setting as moin
    # uses a good internal default (something like '/moin_static171' for moin
    # version 1.7.1).
    # For Twisted and standalone server, the default will automatically work.
    # For others, you should make a matching server config (e.g. an Apache
    # Alias definition pointing to the directory with the static stuff).

    user_dir = parent_dir + userbase_name + '/data/user/'


