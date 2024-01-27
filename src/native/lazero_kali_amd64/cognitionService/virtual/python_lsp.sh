#echo {} | pyls
# this is extraneous,
python3 -c "import jedi;s=jedi.Script(path='python_complete.py');print(s.complete(2+1,len('a=np.')))"
#line num is not index num.
