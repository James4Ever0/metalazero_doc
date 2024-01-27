# only if there is tasks.json can we import anything
if [[ -f tasks.json ]]; then
	task import < tasks.json
else
	echo there is no tasks.json
	exit 1
fi
