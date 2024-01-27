mkdir diary
target_diary=$(python3 -c "import datetime; print(datetime.datetime.now().date().isoformat()+'.txt')")
echo target: $target_diary
sleep 0.5
cd diary
vim $target_diary
