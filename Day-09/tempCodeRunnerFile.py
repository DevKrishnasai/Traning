



    def heightOfTree(self,root,h=0):
        if root==None:
            return h
        l = self.heightOfTree(root.left,h+1)
        r = self.heightOfTree(root.right,h+1)
        return max(l,r)










