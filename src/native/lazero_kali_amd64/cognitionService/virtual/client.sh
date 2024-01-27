emacsclient -s ~/.emacs.d/server/server -e "(add-to-list 'load-path \".\")"
emacsclient -s ~/.emacs.d/server/server -e "(load \"client\")"
emacsclient -s ~/.emacs.d/server/server -e "(defun voidme () (find-file \"lsp.sh\") (lsp) (next-line))"
emacsclient -s ~/.emacs.d/server/server -e "(voidme)"
#emacsclient -s ~/.emacs.d/server/server -e
#"((lambda () ((next-line))))"
#emacsclient -s ~/.emacs.d/server/server -e "((lambda () ((switch-to-buffer \"lsp.sh\") (next-line))))"
#emacsclient -s ~/.emacs.d/server/server -e "(print 'hello)"
