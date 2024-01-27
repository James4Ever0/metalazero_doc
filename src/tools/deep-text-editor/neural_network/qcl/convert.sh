ls -1 | grep -Eo "^.*.pdf\$" | sed "s/.pdf//g" | xargs -iabc mutool convert -o "abc.html" "abc.pdf"
