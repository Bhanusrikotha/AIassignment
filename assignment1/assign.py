from itertools import combinations
class State:
    amoght=5
    ameyat=10
    gdmt=20
    gdft=25
    def __init__(self,amogh,ameya,gdm,gdf,um,t):
        self.amogh=amogh
        self.ameya=ameya
        self.gdm=gdm
        self.gdf=gdf
        self.um=um
        self.t=t
    def goalTest(self):
        if(self.amogh==self.ameya==self.gdm==self.gdf=='r' and self.t==60):
            return True
        else:
            return False
    def movGen(self):
        children=[]
        options=["am","ay","gm","gf"]
        if self.um=="l":
            n="r"
            for i, j in combinations(options, 2):
                        if i=="am" and j=="ay" and self.amogh=="l" and self.ameya=="l":
                            t=max(State.amoght,State.ameyat)
                            child_obj=State(n,n,self.gdm,self.gdf,n,self.t+t)
                            if(child_obj.t<=60):
                                children.append(child_obj)
                        elif i=="am" and j=="gm" and self.amogh=="l" and self.gdm=="l":
                            t=max(State.amoght,State.gdmt)
                            child_obj=State(n,self.ameya,n,self.gdf,n,self.t+t)
                            if(child_obj.t<=60):
                                children.append(child_obj)
                        elif i=="am" and j=="gf" and self.amogh=="l" and self.gdf=="l":
                            t=max(State.amoght,State.gdft)
                            child_obj=State(n,self.ameya,self.gdm,n,n,self.t+t)
                            if(child_obj.t<=60):
                                children.append(child_obj)
                        elif i=="ay" and j=="gf" and self.gdf=="l" and self.ameya=="l":
                            t=max(State.ameyat,State.gdft)
                            child_obj=State(self.amogh,n,self.gdm,n,n,self.t+t)
                            if(child_obj.t<=60):
                                children.append(child_obj)
                        elif i=="ay" and j=="gm" and self.gdm=="l" and self.ameya=="l":
                            t=max(State.ameyat,State.gdmt)
                            child_obj=State(self.amogh,n,n,self.gdf,n,self.t+t)
                            if(child_obj.t<=60):
                                children.append(child_obj)
                        elif i=="gm" and j=="gf" and self.gdm=="l" and self.gdf=="l":
                            t=max(State.gdmt,State.gdft)
                            child_obj=State(self.amogh,self.ameya,n,n,n,self.t+t)
                            if(child_obj.t<=60):
                                children.append(child_obj)
        else:
            n="l"
            for i in options:
                if i=="am" and self.amogh=="r":
                    child_obj=State(n,self.ameya,self.gdm,self.gdf,n,self.t+State.amoght)
                    children.append(child_obj)
                elif i=="ay" and self.ameya=="r":
                     child_obj=State(self.amogh,n,self.gdm,self.gdf,n,self.t+State.ameyat)
                     children.append(child_obj)
                elif i=="gm" and self.gdm=="r":
                     child_obj=State(self.amogh,self.ameya,n,self.gdf,n,self.t+State.gdmt)
                     children.append(child_obj)
                elif i=="gf" and self.gdf=="r":
                     child_obj=State(self.amogh,self.ameya,self.gdm,n,n,self.t+State.gdft)
                     children.append(child_obj)
        return children
    @staticmethod
    def removeSeen(children,open,closed):
        opennodes=[nodes for nodes,parent in open]
        closednodes=[nodes for nodes,parent in closed]
        children=[c for c in children if c not in opennodes and c not in closednodes]
        return children
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
    def __str__(self):
        return f"amogh: {self.amogh}, ameya: {self.ameya}, gdm: {self.gdm}, gdf: {self.gdf}, um: {self.um}, time: {self.t}"
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
                for p in path:
                   print(p)
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
                for p in path:
                   print(p)
                return 
            else:
                closed.append(newpair)
                children=node.movGen()
                newnode=State.removeSeen(children,open,closed)
                newpairs=[(c,node)for c in newnode]
                open=newpairs+open
        return []
    def __eq__(self, other):
        return (self.amogh == other.amogh and self.ameya == other.ameya and
            self.gdm == other.gdm and
            self.gdf == other.gdf and
            self.um == other.um)

    def __hash__(self):
        return hash((self.amogh, self.ameya, self.gdm, self.gdf, self.um))
s_s=State("l","l","l","l","l",0)
print("bfs")
State.bfs(s_s) 
print("dfs")
State.dfs(s_s) 
