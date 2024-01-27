ifconfig | grep -C 1 arc0 | grep -Eo "inet [0-9]+.[0-9]+.[0-9]+.[0-9]+" | grep -Eo "[0-9]+.[0-9]+.[0-9]+.[0-9]+" | tee tmp_ip.confidential | termux-clipboard-set
port=19243
sed -i "s/^/http:\/\//;s/$/:$port/g" tmp_ip.confidential
cat tmp_ip.confidential
cat tmp_ip.confidential | termux-clipboard-set
rm tmp_ip.confidential
echo address copied!
python3 test_events.py
