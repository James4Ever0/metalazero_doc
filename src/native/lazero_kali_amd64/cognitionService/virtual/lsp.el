;try to import the eglot.el
; or find the way to import? or spy the import stack.
;(use-package eglot)
(require 'package)
(package-initialize)
(require 'lsp-mode)
(require 'company)
(require 'request)

(company-mode)
(lsp)
;(use-package lsp-mode
;  :config
;  (setq lsp-idle-delay 0.5)
;  :hook
;  ((python-mode . lsp)
;   (sh-mode . lsp))
;  )
;(require 'lsp-mode)
;(lsp)
(setq lsp-idle-delay 0)
;(company-complete-common)
(find-file "lsp.sh")
;(lsp-workspace-folders-add "/data/data/com.termux/files/home/metalazero/native/lazero_kali_amd64/cognitionService/virtual")
(lsp-workspace-folders-add ".")
(find-file "lsp.sh");wtf is going on?
;(print "init done?")
(company-complete-common)
(completion-at-point) ;;this is the function
;; minibuffer.el, even accessible for ielm?
(setq cnds (format "%s" company-candidates))
(request "http://localhost:8786/post" :type "POST" :data `(("key" . ,cnds) ("key2" . "value2")) :parser 'json-read :success (cl-function(lambda (&key data &allow-other-keys)(message "I sent: %S" (assoc-default 'form data)))))
;completion-all-sorted-completions
;completion--all-sorted-completions-location
;(apply #'eglot--connect (eglot--guess-contact));no def here.
;(describe-function #'lsp-mode)
;(print-buffer)
;(describe-function #'eglot)
;(eglot 'sh-mode (project-current) 'eglot-lsp-server 'eglot-server-programs nil)
;(find-file "lsp.sh"); not executing.
;(run-with-timer 2 2 #'eglot-completion-at-point)
;(run-with-idle-timer eglot-completion-at-point)
;(package-install 'helm)
;(ielm) in buffer, not stdout.
;(defun find-symbols-having-properties (properties)
;  (let (ret)
;    (mapatoms (lambda (s)
;                (when (cl-loop for prop in properties
;                               thereis (get s prop))
;                    (push s ret))))
;    ret))
;(find-symbols-having-properties)
;(autoload 'use-package)
;(use-package "eglot")
;(package-activate 'eglot)
;(require 'eglot)
;(eglot-ensure)
;(find-file "vscode_ipc.sh")
;(package-install 'async-await)
;(add-to-list 'load-path ".")
;(print load-path)
;(require 'package)
;(require 'eglot)
;(load "eglot")
;(eglot-ensure)
;(sleep-for 20)
;(eglot-completion-at-point)
;(eglot t t t)
;(print (eglot--all-major-modes))
;(managed-major-mode project class contact &optional interactive)
;(setq project-root ".")
;(eglot "." t t t)
;(eglot t t)
;(eglot t t t t t)
;(eglot t t t)
;(add-hook 'sh-mode-hook 'eglot-ensure)
;(sh-mode)
;(sleep for a while...)
;(eglot-completion-at-point)
;(add-hook 'text-mode 'eglot-ensure)
;(add-hook 'sh-mode-hook 'eglot-ensure)
;(add-hook 'foo-mode-hook 'eglot-ensure)
;(print eglot-server-programs)
