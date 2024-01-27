(run-with-timer 3 3 #'sm-poll-message-changes)
(add-hook 'post-command-hook #'sm-poll-message-changes)

(defvar sm--pmc-marker nil)
(defvar sm--pmc-marker-pos nil)
(defvar sm--pmc-tick nil)

(setq content_notice "buffer has changed")
(with-current-buffer (get-buffer "*Messages*")
  (setq sm--pmc-marker (point-max-marker))
  (setq sm--pmc-marker-pos (point-max))
  (setq sm--pmc-tick (buffer-chars-modified-tick)))

(defun sm-poll-message-changes ()
  (with-current-buffer (marker-buffer sm--pmc-marker)
    (unless (eq sm--pmc-tick (buffer-chars-modified-tick))
      ;; A change happened.
      (let ((deleted-chars-at-bob
             (- sm--pmc-marker-pos sm--pmc-marker))
            (inserted-chars-at-eob
             (- (point-max) sm--pmc-marker)))
	(setq previous-marker sm--pmc-marker-pos)
        (setq sm--pmc-marker-pos (point-max))
        (setq sm--pmc-tick (buffer-chars-modified-tick))
        (move-marker sm--pmc-marker (point-max))
	(print (format "delta: %s" (buffer-substring previous-marker (point-max))))
	;(print (format "delta: %d-%d" previous-marker (point-max)))
	; do shit here.
	))))
