from emacs import Emacs
emacs = Emacs.batch(['-q'])
src = '(princ (format "One plus two is %d" (+ 1 2)))'
print(emacs.eval(src))
#print(emacs.eval("(lsp)"))
#subprocess.CalledProcessError: Command '['emacs', '--batch', '-q', '--eval', '(lsp)'
#error.
#it is repeated?
print(emacs.eval("(print 'hello)"))
