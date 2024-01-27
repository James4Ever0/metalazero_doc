(require 'package)
(package-initialize)
;(require 'async-await)
(setq lexical-binding t)
(setq kill-emacs t)
(defun wait-async (n)
  (promise-new (lambda (resolve _reject)
                 (run-at-time n
                              nil
                              (lambda ()
                                (funcall resolve n))))))

(async-defun example2 ()
  (print (await (wait-async 0.5)))
  (message "---")

  (print (await (wait-async 1.0)))
  (message "---")

  (print (await (wait-async 1.5)))
  (message "---")

  (message "await done"))
(example2)
;(await (example2))
;(print 'preinit)
;(message "what is going on?")
(run-with-timer 2 2 #'print "hello")
;(print 'hello)(print 'hello)
