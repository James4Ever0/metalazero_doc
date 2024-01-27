#!/bin/bash
emacs --batch --eval '(progn (package-initialize) (lsp) (lsp-workspace-folders-add ".") (find-file "lsp.sh") (lsp) (completion-at-point) (print lsp-completion--cache))'
