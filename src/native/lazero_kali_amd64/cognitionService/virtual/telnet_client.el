(setq echo-server-port 10000)
(setq client-process (open-network-stream "echo-client"
                          "*echo-client*" "localhost" echo-server-port))
; process-filter
; set-process-filter

;(setq tmp_buf "TempBuffer")
; not just that.
(defun my-filter-function (program text) (with-temp-file "tempbuffer.log" (insert text) (run-with-timer 1 nil #'kill-emacs)))
(set-process-filter client-process #'my-filter-function)
;(kill-buffer tmp_buf)
;(get-buffer-create tmp_buf)
(process-send-string client-process "hello world\n")
;(print (process-filter client-process))
