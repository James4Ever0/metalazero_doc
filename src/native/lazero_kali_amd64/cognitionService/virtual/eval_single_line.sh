#!/bin/bash
#headless? repl?
emacs --eval "(list (find-file \"lsp.sh\") (lsp) (lsp-workspace-folders-add \".\") (setq lsp-idle-delay 0) (setq completion-at-point-functions (list #'lsp-completion-at-point)) (run-with-timer 10 nil (lambda () (list (completion-at-point) (print lsp-completion--cache)))))"
# hook *Messages*
# post/pre-command-hook polling with-current-buffer
