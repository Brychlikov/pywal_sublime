#! /usr/bin/env python
import json
import os


def make_element(name, scope, **kwargs):
    """Helper function for generating color scheme entries"""
    result = {}
    result['name'] = name
    result['scope'] = scope
    result.update(kwargs)
    return result


if __name__ == '__main__':
    wal_path = os.path.join(os.environ["HOME"], '.cache/wal/colors.json')
    with open(wal_path) as file:
        wal_scheme = json.load(file)
    wal_colors = [wal_scheme['colors']['color%d' % i] for i in range(16)]

    result_scheme = {}
    result_scheme['name'] = 'Pywal'

    # global settings
    global_settings = {}
    global_settings['background'] = wal_scheme['special']['background']
    global_settings['foreground'] = wal_scheme['special']['foreground']
    global_settings['caret'] = wal_scheme['special']['foreground']
    global_settings['invisibles'] = wal_colors[1]
    global_settings['lineHighlight'] = wal_colors[2]
    global_settings['selection'] = wal_colors[6]

    # Color scheme elements
    settings = []
    settings.append(make_element('Comment', 'comment', foreground=wal_colors[2]))
    settings.append(make_element('String', 'string', foreground=wal_colors[4]))
    settings.append(make_element('Number', 'constant.numeric', foreground=wal_colors[5]))
    settings.append(make_element('Built-in constant', 'constant.language', foreground=wal_colors[5]))
    settings.append(make_element('User-defined constant', 'constant.character, constant.other',
                                 foreground=wal_colors[5]))
    settings.append(make_element('Variable', 'variable', fontStyle=''))
    settings.append(make_element('Storage', 'storage', foreground=wal_colors[3], fontStyle=''))
    settings.append(make_element('Storage type', 'storage.type', foreground=wal_colors[6], fontStyle='italic'))
    settings.append(make_element('Class name', 'entity.name.class', foreground=wal_colors[1],
                                 fontStyle='italic'))
    settings.append(make_element('Inherited class', 'entity.other.inherited-class', foreground=wal_colors[1],
                                 fontStyle='italic'))
    settings.append(make_element('Function name', 'entity.name.function', foreground=wal_colors[1], fontStyle='italic'))
    settings.append(make_element('Function argument', 'variable.parameter', foreground=wal_colors[6], fontStyle=''))
    settings.append(make_element('Tag name', 'entity.name.tag', foreground=wal_colors[3], fontStyle=''))
    settings.append(make_element('Tag attribute', 'entity.other.attribute-name', foreground=wal_colors[1],
                                 fontStyle=''))
    settings.append(make_element('Library function', 'support.function', foreground=wal_colors[6], fontStyle=''))
    settings.append(make_element('Library constant', 'support.constant', foreground=wal_colors[6], fontStyle=''))
    settings.append(make_element('Library class/type', 'support.class, support.type', foreground=wal_colors[6],
                                 fontStyle='italic'))
    settings.append(make_element('Library variable', 'support.other.variable', fontStyle=''))
    settings.append(make_element('Invalid', 'invalid', fontStyle='',
                                 foreground=wal_scheme['special']['foreground'], background=wal_colors[5]))
    settings.append(make_element('Invalid deprecaded', 'invalid.deprecated', fontStyle='',
                                 foreground=wal_scheme['special']['foreground'], background=wal_colors[4]))

    result_scheme['globals'] = global_settings
    result_scheme['rules'] = settings
    result_scheme['semanticClass'] = 'theme.dark.pywal'

    theme_path = os.path.join(os.environ['HOME'], '.config/sublime-text-3/Packages/User/PyWal.sublime-color-scheme')
    with open(theme_path, 'w') as file:
        json.dump(result_scheme, file, indent=4)







