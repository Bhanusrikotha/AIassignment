class State:
    def __init__(self,st):
        self.st=st
    def __eq__(self, other):
        return self.st == other.st
    def __hash__(self):
        return hash(tuple(self.st))
    def goalTest(self):
        if(self.st==["l","l","l","_","_","_","r","r","r"]):
            return True
        else:
            return False
    @staticmethod
    def removeSeen(children,open,closed):
        opennodes=[nodes for nodes,parent in open]
        closednodes=[nodes for nodes,parent in closed]
        children=[c for c in children if c not in opennodes and c not in closednodes]
        return children
    def __str__(self):
        return ''.join(self.st)
    @staticmethod
    def reconstructpath(newpair,closed):
        path=[]
        parentmap={}
        for node,parent in closed:
            parentmap[node]=parent
        node,parent=newpair
        path.append(node)
        while parent is not None:
            path.append(parent) 
            parent=parentmap[parent]
        return path
    @staticmethod
    def bfs(s):
        open=[(s,None)]
        closed=[]
        while open:
            newpair=open.pop(0)
            node,parent=newpair
            if node.goalTest():
                print("goal found")
                path=[]
                path=State.reconstructpath(newpair,closed)
                path.reverse()
                c=1
                for p in path:
                   print(c,"=>",p)
                   c=c+1
                return 
            else:
                closed.append(newpair)
                children=node.movGen()
                newnode=State.removeSeen(children,open,closed)
                newpairs=[(c,node)for c in newnode]
                open=open+newpairs
        return []
    @staticmethod
    def dfs(s):
        open=[(s,None)]
        closed=[]
        while open:
            newpair=open.pop(0)
            node,parent=newpair
            if node.goalTest():
                print("goal found")
                path=[]
                path=State.reconstructpath(newpair,closed)
                path.reverse()
                c=1
                for p in path:
                   print(c,"=>",p)
                   c=c+1
                return 
            else:
                closed.append(newpair)
                children=node.movGen()
                newnode=State.removeSeen(children,open,closed)
                newpairs=[(c,node)for c in newnode]
                open=newpairs+open
        return []
    def movGen(self):
        li=[-2,-1,1,2]
        children=[]
        for i in range(len(self.st)):
            if self.st[i] == '_':
                for move in li:
                    pos = i + move
                    if 0 <= pos < len(self.st):
                        if (self.st[pos] == 'r' and move < 0) or (self.st[pos] == 'l' and move > 0):
                            child = self.st.copy()
                            child[i], child[pos] = child[pos], child[i]
                            children.append(State(child))
        return children
    
s_s=State(["_","r","r","r","_","l","l","l","_"])#intial state as right facing rabbits are indicated with r and left facing rabbits are indicated with l
print("bfs")
State.bfs(s_s) 
print("dfs")
State.dfs(s_s) 

        
