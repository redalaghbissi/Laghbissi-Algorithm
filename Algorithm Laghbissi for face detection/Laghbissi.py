import numpy as np
from PIL import Image

############################  Class Du Visage ##################################

def detectvisage(nomfichier):
    class Visage:
        def __init__(self,x1,x2,y1,y2):
            self.x1=x1
            self.y1=y1
            self.x2=x2
            self.y2=y2        

        def dimmentionVisage(self):
            if( (self.x2-self.x1)/4 < (self.y2-self.y1) < (self.x2-self.x1)):
                return True
            else:
                return False

        def detectionDuBouche(self):
            cmp=0
            cmppoureviteunpixel=0
            xfirst=0
            xlast=0
            yfirst=0
            ylast=0
            for x in range(self.x1,self.x2,1):
                for y in range(self.y1,self.y2,1):
                    s=img[x,y]
                    r=s[0]
                    g=s[1]
                    b=s[2]
                    #230 > r > 120 and 50 > g > 0 and 160 > b > 0
                    if (230 > r > 180 and 100 > g > 50 and 120 > b > 70):
                        #imgtmp[x,y]=np.array([0,0,0])
                        cmp=cmp+1
                        if(xfirst == 0):
                            xfirst=x
                        if(yfirst == 0):
                            yfirst=y
                        
                        cmppoureviteunpixel=cmppoureviteunpixel+1
                        if(cmppoureviteunpixel>100):    
                            xlast=x
                            ylast=y
                            cmppoureviteunpixel=0

            if(cmp > 7):
            
                for x in range(int(xfirst+((xlast-xfirst)/2)-20),int(xfirst+((xlast-xfirst)/2)+21),1):
                    imgtmp[x,int(yfirst+((ylast-yfirst)/2))]=np.array([255,255,255])
                for y in range(int(yfirst+((ylast-yfirst)/2)-20),int(yfirst+((ylast-yfirst)/2)+21),1):
                    imgtmp[int(xfirst+((xlast-xfirst)/2)),y]=np.array([255,255,255])

                return True
            else:
                return False
        
        def detectionYeuxD(self):
            cmp=0
            cmppoureviteunpixel=0
            xfirst=0
            xlast=0
            yfirst=0
            ylast=0
            for x in range(self.x1,self.x2,1):
                for y in range(self.y1,int(self.y1+(self.y2-self.y1)/2),1):
                    s=img[x,y]
                    r=s[0]
                    g=s[1]
                    b=s[2]
                    if (175 > r > 140 and 160 > g > 120 and 160 > b > 120):
                        #imgtmp[x,y]=np.array([0,0,0])
                        cmp=cmp+1
                        if(xfirst == 0):
                            xfirst=x
                        if(yfirst == 0):
                            yfirst=y
                        cmppoureviteunpixel=cmppoureviteunpixel+1
                        if(cmppoureviteunpixel>5):    
                            xlast=x
                            ylast=y
                            cmppoureviteunpixel=0
            if(cmp > 7):
            
                for x in range(int(xfirst+((xlast-xfirst)/2)-20),int(xfirst+((xlast-xfirst)/2)+21),1):
                    imgtmp[x,int(yfirst+((ylast-yfirst)/2))]=np.array([255,255,255])
                for y in range(int(yfirst+((ylast-yfirst)/2)-20),int(yfirst+((ylast-yfirst)/2)+21),1):
                    imgtmp[int(xfirst+((xlast-xfirst)/2)),y]=np.array([255,255,255])

                return True
            else:
                return False      

        def detectionYeuxG(self):
            cmp=0
            cmppoureviteunpixel=0
            xfirst=0
            xlast=0
            yfirst=0
            ylast=0
        
            for x in range(self.x1,self.x2,1):
                for y in range(int(self.y1+(self.y2-self.y1)/2),self.y2,1):
                    s=img[x,y]
                    r=s[0]
                    g=s[1]
                    b=s[2]
                    #175 > r > 120 and 160 > g > 120 and 160 > b > 120
                    if (175 > r > 120 and 160 > g > 120 and 160 > b > 120):
                        #imgtmp[x,y]=np.array([0,0,0])
                        cmp=cmp+1
                        if(xfirst == 0):
                            xfirst=x
                        if(yfirst == 0):
                            yfirst=y
                        cmppoureviteunpixel=cmppoureviteunpixel+1
                        if(cmppoureviteunpixel>5):    
                            xlast=x
                            ylast=y
                            cmppoureviteunpixel=0  
            if(cmp > 7):
            
                for x in range(int(xfirst+((xlast-xfirst)/2)-20),int(xfirst+((xlast-xfirst)/2)+21),1):
                    imgtmp[x,int(yfirst+((ylast-yfirst)/2))]=np.array([255,255,255])
                for y in range(int(yfirst+((ylast-yfirst)/2)-20),int(yfirst+((ylast-yfirst)/2)+21),1):
                    imgtmp[int(xfirst+((xlast-xfirst)/2)),y]=np.array([255,255,255])

                return True
            else:
                return False

######################################## Debut Du Function  ###########################################

    #les doublent de la truc x
    VisageObjectX=list()
    #les doublent de la truc y
    VisageObjectY=list()
    #axes des valeur x
    axesX=list()
    #axes des valeurs y
    axesY=list()
    ######################################### imprte image en matrix est met le variable #####################

    imgpil = Image.open(nomfichier)
    img = np.array(imgpil)
    imgtmp= np.array(imgpil)


    ######################################### Prepare les courbe ###############################

    #lacces de x
    for i in range(0,img.shape[0],10):
        axesX.append(0)
    #lacces de y
    for i in range(0,img.shape[1],10):
        axesY.append(0)

    ################################### Lire Image Est Detecte Le Color de Peu ###########################################

    s="salut"
    for x in range(0,img.shape[0],10):
        for y in range(0,img.shape[1],10):
            s=img[x,y]
            r=s[0]
            g=s[1]
            b=s[2]

            if (255 > r > 170 and 220 > g > 100 and 180 > b > 80):

                imgtmp[x,y]=np.array([255,0,0])
                axesX[int(x/10)]=1
                axesY[int(y/10)]=1


    #En determine maintenet lintervale de trace la courbeest en le trace + en stoke les demention dans une nouvelle lisste

    ############################################ En Trace La Courbw X ###############################################
    for x in range(img.shape[0]-1,img.shape[0],1):
        for y in range(0,img.shape[1],1):
            imgtmp[x,y]=np.array([255,255,255])
            
    dozy=False
    cmpy=0
    cmpf=False
    for i in range(0,img.shape[0],10):

        if(axesX[int(i/10)] == 1):
            cmpy=cmpy+1
        if(axesX[int(i/10)] == 0):
            cmpy=0
    # si le image est commence par indice 0
        if(cmpf and cmpy==0):
            VisageObjectX.append(i)
            for xp in range(img.shape[0]):
                for yp in range(img.shape[1]):
                    if(xp == i):
                        imgtmp[xp,yp]=np.array([0,0,255])       

    # 3 if pour la condition   
        if(cmpy > 1):
            dozy=False
            
        if(cmpy == 1 and axesX[int(i/10)+1] == 1 and axesX[int(i/10)+2] == 1 and  axesX[int(i/10)+3] == 1 and axesX[int(i/10)+5] == 1):
            dozy=True
            cmpf=True
            
        if(cmpy == 0):
            dozy=False
            cmpf=False
            
        if(dozy):        
            VisageObjectX.append(i)
            for xp in range(img.shape[0]):
                for yp in range(img.shape[1]):
                    if(xp == i):
                        imgtmp[xp,yp]=np.array([0,255,0])

    if(cmpf):
        VisageObjectX.append(i)
        for xp in range(img.shape[0]):
            for yp in range(img.shape[1]):
                if(xp == i):
                    imgtmp[xp,yp]=np.array([255,0,0])

    ####################################### En Trace La Courbw Y ##############################3


    dozy=False
    cmpy=0
    cmpf=False
    for i in range(0,img.shape[1],10):
        if(axesY[int(i/10)] == 1):
            cmpy=cmpy+1
        if(axesY[int(i/10)] == 0):
            cmpy=0
    #si lindice 0 deja existe
        if(cmpf and cmpy==0):
            VisageObjectY.append(i)
            for xp in range(img.shape[0]):
                for yp in range(img.shape[1]):
                    if(yp == i):
                        imgtmp[xp,yp]=np.array([0,0,255])       

    #ya que 3 choix    
        if(cmpy > 1):
            dozy=False
    
    # 10 c est pour optimise lalgorithme 
        if(cmpy == 1 and axesY[int(i/10)+1] == 1 and axesY[int(i/10)+2] == 1 and  axesY[int(i/10)+3] == 1 and axesY[int(i/10)+5] == 1):
            dozy=True
            cmpf=True
     
        if(cmpy == 0):
            dozy=False
            cmpf=False

     
        if(dozy):        
            VisageObjectY.append(i)
            for xp in range(img.shape[0]):
                for yp in range(img.shape[1]):
                    if(yp == i):
                        imgtmp[xp,yp]=np.array([0,255,0])
                        
    if(cmpf):
        VisageObjectY.append(i)
        for xp in range(img.shape[0]):
            for yp in range(img.shape[1]):
                if(yp == i):
                    imgtmp[xp,yp]=np.array([255,0,0])    





    ############ classe les visage dans tab des object #####################

    VisageTabObject=list()
    VisageTabTraite=list()
    # declaration du tab
    for i in range(0,len(VisageObjectX),2):
        VisageTabObject.append(Visage(VisageObjectX[i],VisageObjectX[i+1],VisageObjectY[i],VisageObjectY[i+1]))



    ############## la derbier verification pour viage #####################
    for i in VisageTabObject:
        if(i.detectionYeuxD() and i.detectionYeuxG() and  i.detectionDuBouche()):
            VisageTabTraite.append(i)
            


    saveimg = Image.fromarray(imgtmp)
    
    #########  affiche liste des visage  ########
    print(VisageTabObject)
    
    return saveimg

####################################### Les Function Des Module #############################################

def affiche(nomdufichier):
    detectvisage(nomdufichier).show()

