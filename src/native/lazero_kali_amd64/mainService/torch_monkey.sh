#DISPLAY=:99 xhost +
#DISPLAY=:99 python3 monkey_basic.py
address=localhost:5800
passwd=$(cat .secret)
#passwd=randompassword
stime0=100
stime1=20
while true
do
	echo launching monkey.
	timeout $stime0 python3 vnc_monkey.py -p $passwd -a $address
	echo launching bruteforcer.
	timeout $stime1 python3 vnc_bruteforcer.py -p $passwd -a $address
done
#vncdotool -p $passwd -s 127.0.0.1::5800 mouseup 1 
#vncdotool -p $passwd -s 127.0.0.1::5800 -vvvv keydown A
# we launch the shit within the shit.
#vncdotool -p $passwd -s 127.0.0.1::5800 mousemove 500 500  
#vncdotool -p $passwd -s 127.0.0.1::5800 mousedown 1 
