emacsclient -s foo -e "(list (find-file \"lsp.sh\") (print (current-buffer)))"
#emacsclient -s foo -e "((lambda () (find-file \"lsp.sh\") (print (current-buffer))))"
#emacsclient -s foo -e "(cons (print 'hello) (cons (print 'world) (print 'hello)))"
