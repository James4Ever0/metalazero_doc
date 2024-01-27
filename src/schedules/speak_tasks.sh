#task export | python3 speaker.py | espeak
while true
do
#	task ls | tail -n +4 | grep -Eo "[^0-9]+"
	task ls | tail -n +4 | head -n -2 |grep -Eo "[^0-9]+" | shuf | xargs -iabc bash speak_word.sh abc 
done
