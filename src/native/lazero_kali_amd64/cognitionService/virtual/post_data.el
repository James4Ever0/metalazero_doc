(require 'package)
(package-initialize)
(require 'request)
(request "http://localhost:8786/post" 
	 :type "POST" 
	 :data '(("key" . "value") ("key2" . "value2")) 
	 :parser 'json-read 
	 :success (cl-function(lambda (&key data &allow-other-keys)
	(message "I sent: %S" (assoc-default 'form data)))))
(require 'company)
(find-file "lsp.sh")
(company-mode)
(company-complete-common)
(setq cnds (format "%s" company-candidates))
(request "http://localhost:8786/post" :type "POST" :data `(("key" . ,cnds) ("key2" . "value2")) :parser 'json-read :success (cl-function(lambda (&key data &allow-other-keys)(message "I sent: %S" (assoc-default 'form data)))))
;(print cnds)
;(print (format "%s" company-candidates))
