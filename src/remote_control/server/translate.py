abc = [chr(ord("a")+x) for x in range(26)]
ABC = [x.upper() for x in abc]
#print(abc)
#print(ABC)
keyABC = ["Key"+x for x in ABC]
#print(keyABC)
modifier = ["Alt","Ctrl","Shift","Meta","MetaLeft","MetaRight","ShiftLeft","ShiftRight","AltLeft","AltRight","CtrlLeft","CtrlRight"]
symbols="~`!@#$%^&*()-_+={}[]|\\:;\"'<,>.?/"
digits= "0123456789"
extras= ["Tab","Enter","Escape","ArrowUp","ArrowDown","ArrowLeft","ArrowRight","PageUp","PageDown","Home","End","Space","Backspace","Delete"]

key_translate={}
code_translate={}
key_modifier=[x for x in modifier if "Left" not in x and "Right" not in x]
code_modifier = [x for x in modifier if x not in key_modifier]

key_abc = {x:x for x in abc}
key_ABC = {x:x.lower() for x in ABC}
key_symbols = {x:x for x in symbols}
key_digits = {x:x for x in digits}
key_extras = {x:x.lower().replace("arrow","") for x in extras}
key_extras.pop("Space")
key_extras.update({" ":"space"})
# if modifier then translate using code. may still have some shits.
# if not using key translate table.
modifier_translate = {x:x.lower() for x in modifier}

for x in [key_abc, key_ABC, key_symbols, key_digits, key_extras]:
    key_translate.update(x)

print("key_modifier:",key_modifier)
print("main translate table:\n",key_translate)
print("modifier trabslate table (code):\n", modifier_translate)
