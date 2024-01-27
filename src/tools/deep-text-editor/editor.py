import copy 
import traceback
class editor:
    def __init__(self,content="",position=0,operation=[]):
        self.content=content
        self.init_content=content
        self.position=position
        self.clipboard=""
        self.operation=[]
        self.backup()
        if operation != []:
            self.redo_operation(operation)
        self.backup()
    def log_operation(self,op_type,param=None):
        self.operation.append((op_type,param))
    def backup(self):
        self.last_state=(self.content,self.position,self.clipboard)
    def self_check(self):
        if self.position<0:
            self.position=0
        elif self.position>len(self.content):
            self.position=len(self.content)
    def insert(self,content,paste=False):
        self.backup()
        if not paste:
            self.log_operation("insert",content)
        head=self.content[:self.position]
        tail=self.content[self.position:]
        self.content=head+content+tail
        self.position=len(head)+len(content)
        self.self_check()
    def backspace(self,times):
        self.backup()
        self.log_operation("backspace",times)
        delta_p=self.position-times
        if delta_p<0:
            delta_p=0
        head=self.content[:delta_p]
        tail=self.content[self.position:]
        self.content=head+tail
        self.position=delta_p
        self.self_check()
    # maybe you can duplicate something like that?
    def delete(self,times):
        self.backup()
        self.log_operation("delete",times)
        delta_p=self.position+times
        lc=len(self.content)
        if delta_p>lc:
            delta_p=lc
        head=self.content[:self.position]
        tail=self.content[delta_p:]
        self.content=head+tail
        self.self_check()
    def replace(self,content):
        self.backup()
        self.log_operation("replace",content)
        head=self.content[:self.position]
        tail=self.content[self.position+len(content):]
        self.content=head+content+tail
        self.position=len(head)+len(content)
        self.self_check()
    def copy(self,content):
        self.backup()
        self.log_operation("copy",content)
        self.clipboard=content
        self.self_check()
    def paste(self):
        self.backup()
        self.log_operation("paste")
        self.insert(self.clipboard,paste=True)
        self.self_check()
    def forward(self,times):
        self.backup()
        self.log_operation("forward",times)
        self.position+=times
        self.self_check()
    def backward(self,times):
        self.backup()
        self.log_operation("backward",times)
        self.position-=times
        self.self_check()
    def view(self,span=30):
        a=self.position-span
        b=self.position+span
        if a<0:
            a=0
        if b>len(self.content):
            b=len(self.content)
        return self.content[a:b]
    def undo(self):
        self.log_operation("undo")
        content, position, clipboard =self.content,self.position, self.clipboard
        self.content,self.position,self.clipboard=self.last_state
        self.last_state = (content,position,clipboard)
    def dump_operation(self):
        return tuple(self.operation)
    def redo_operation(self,operation):
        #import time
        #print("redoing all things")
        # is that unknown compiler bug?
        last_state = self.last_state
        clipboard = self.clipboard
        cstate, pstate= self.content, self.position
        ops_bk=copy.copy(self.operation)
        #print(operation)
        try:
            for x in range(len(operation)):
                ops, param = operation[x]
                #print("executing:",(ops,param))
                #time.sleep(1)
                if ops == "copy":
                    self.copy(param)
                elif ops == "paste":
                    self.paste()
                elif ops == "delete":
                    self.delete(param)
                elif ops == "backspace":
                    self.backspace(param)
                elif ops == "insert":
                    self.insert(param)
                elif ops == "replace":
                    self.replace(param)
                elif ops == "undo":
                    self.undo()
                elif ops == "forward":
                    self.forward(param)
                elif ops == "backward":
                    self.backward(param)
                else:
                    raise Exception('Invalid operation: %s' % str(ops,param))
                #print("after execution:",self.content,self.position)
        except:
            traceback.print_exc()
            print("failed to execute all operations.")
            print("revoking to previous state.")
            self.content=cstate
            self.position=pstate
            self.clipboard=clipboard
            self.last_state=last_state
            self.operation=ops_bk
