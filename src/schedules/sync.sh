bash pull.sh
if [ $! -eq 0 ]; then
	# now you can safely do your shit.
	touch .latest
	python3 merge_file.py
else
	rm .latest
fi
