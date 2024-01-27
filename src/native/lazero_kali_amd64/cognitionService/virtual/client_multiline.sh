emacsclient -s foo -e "\`(,(print (current-buffer)) ,(find-file \"autopush.sh\") ,(print (current-buffer)))"
# not the same in fish. backtick no need to escape.
