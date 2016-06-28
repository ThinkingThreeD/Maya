import maya.cmds as cmds
    
def mirrorSel(r=True,p=True):
    ''' Mirror la selection d'un objet sur l'autre'''
    if len(cmds.ls(sl=True))==2:
        rotate = cmds.xform(cmds.ls(sl=True)[1], q=True, ro=True, ws=True)
        translate = cmds.xform(cmds.ls(sl=True)[1], q=True, t=True, ws=True)
        if p:
            p=(-translate[0],translate[1],translate[2])
            cmds.xform(cmds.ls(sl=True)[0],t=p, ws=True)
        if r:
            r = (rotate[0],-rotate[1],-rotate[2])
            cmds.xform(cmds.ls(sl=True)[0],ro=r, ws=True)

          
if __name__ == '__main__':             
  mirrorSel(r=True, p=False)
