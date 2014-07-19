import sublime, sublime_plugin
import unicodedata

# Iota omega nu alpha theta alpha nu
# Ιωναθαν Σωνδκβισθ

# IOTA OMEGA NU ALPHA THETA ALPHA NU
# ΙΩΝΑΘΑΝ ΣΩΝΔΚΒΙΣΘ

# NOTE: Unicode uses the spelling 'lamda'

# TODO | - Load bindings from file
#        - 

# Spec | -
#        - 


class Callback(sublime_plugin.EventListener):
    pass

    def on_query_completions(self, view, prefix, location):
        ''' Docstring... '''
        return [('Alpha', '1'), ('Beta', '2'), ('Gamma', '3'), ('Bling', 'Hello')]


class InsertSpecialSymbol(sublime_plugin.TextCommand):
    
    # Configuration
    DEBUG = True
    
    # Symbol sets
    Greek = { unicodedata.name(L).split()[-1].lower() : L for L in map(chr, range(945, 970)) }
    Math = { 'multiply': '×', 'forall': '∀', 'element': '∈', 'angle': '∠', 'proportional': '∝', 'le': '≤', 'ge': '≥' }
    Misc = { 'check': '✓', 'cross': '❌' }

    replacements = {}

    for d in (Greek, Math, Misc):
        replacements.update(d)

    
    def debug(self, string):
        if InsertSpecialSymbol.DEBUG: print(string)
    
    def run(self, edit):
        ''' Replaces the selected word with an appropriate symbol '''
        view = self.view
        print('Running command')
        for cursor in view.sel():
            wordRegion = view.word(cursor)
            word = view.substr(wordRegion)
            symbol = self.replacements.get(word.lower(), None)
    
            if symbol is not None:
                view.replace(edit, wordRegion, symbol if word[0].islower() else symbol.upper())
            else:
                self.debug('Substitution not available for \'%s\'.' % word)