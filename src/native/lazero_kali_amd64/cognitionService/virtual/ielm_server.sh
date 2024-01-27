#!/bin/bash
emacs --batch --eval "(while t (condition-case err (print (catch 'err (eval (read)))) (error (princ (format \"%s\\n\" (error-message-string err))))))"
