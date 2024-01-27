STR='Ubuntu is a Linux OS'
SUBSTR='Linux'
if [[ "$STR" == *"$SUBSTR"* ]]; then
  echo "String is there."
fi
STR='Ubuntu is a Linux OS'
SUBSTR='UNIX'
if [[ "$STR" == *"$SUBSTR"* ]]; then
  echo "String is there."
else
	echo NOT THE CASE
fi
