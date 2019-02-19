from anytree import Node, RenderTree
cn = Node("CN")
rn2 = Node("rn2", parent=cn)
tdz = Node("tdz", parent=cn)
rn1 = Node("rn1", parent=cn)
b4Start = Node("b4Start", parent=cn)
ah2 = Node("AH2", parent=rn2)
serv2 = Node("serv2", parent=ah2)
serv1 = Node("serv1", parent=ah2)
ah1   = Node("AH1", parent=rn2)
serv2 = Node("serv2", parent=ah1)
serv1 = Node("serv1", parent=ah1)
ah0 = Node("AH0", parent=rn1)
serv2 = Node("serv2", parent=ah0)
serv1 = Node("serv1", parent=ah0)
ah3   = Node("AH3", parent=rn1)
serv2 = Node("serv2", parent=ah3)
serv1 = Node("serv1", parent=ah3)
c = Node("C", parent=b4Start)
b = Node("B", parent=c)
a = Node("A", parent=b)
d = Node("D", parent=b4Start)
e = Node("E", parent=d)
f = Node("F", parent=e)
s3 = Node("S3", parent=c)
s2 = Node("S2", parent=b)
s1 = Node("S1", parent=a)
s4 = Node("S4", parent=d)
s5 = Node("S5", parent=e)
s6 = Node("S6", parent=f)
Start = Node("Start", parent=b4Start)
for pre, fill, node in RenderTree(cn):
    print("%s%s" % (pre, node.name))
