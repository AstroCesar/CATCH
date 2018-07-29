import numpy as np
import matplotlib.pyplot as plt

##########################################################################################
##############################    INPUT USER SECTION     ######################################
##########################################################################################

name_file='name-input.txt' #name of the file that contains the data, must be in text format
name_output_file='name-output.txt' #output name
colx=1  #column that contains the first set of data (default 1, first column)
coly=2  #column that contains the second set of data (default 2, second column)
option=1  #option 1 is to capture the data within a circle, option 2 is for a square
centerX_user,centerY_user=260.994124, -26.3534167  #center of the object (two coordinates)
radio_user=5 #circumference radius
lado_user=8 #the value of the square's side
##########################################################################################
##########################################################################################
##########################################################################################
df=np.genfromtxt(name_file)  #open file
x=df[:,colx-1]   #x coordinates of the objects, only for graphic representation
y=df[:,coly-1]   #y coordinates of the objects, only for graphic representation
l_col=np.shape(df)[1] #number of columns in the file

################################## FUNCIONES ########################################################

def circulo(center_x,center_y,radio,arreglo):
    """function that takes all the points that are inside a certain 
       radius and center entered, for a previously loaded data sets.
    """
    radio_interno=np.sqrt(((arreglo[:,colx-1]-center_x)**2+(arreglo[:,coly-1]-center_y)**2))
    u=np.where(radio_interno<radio)
    output_circulo=arreglo[u]
    coordx_true=output_circulo[:,colx-1]
    coordy_true=output_circulo[:,coly-1]
    return output_circulo,coordx_true, coordy_true

def cuadrado(center_x,center_y,lado,arreglo):
    """function that takes all the points that are contained in a square, which has side = side and 
    center = (center_x, center_y), for a set of previously loaded data
    """
    verti1x,verti2x=center_x+(lado/2),center_x-(lado/2)
    verti1y,verti2y=center_y+(lado/2),center_y-(lado/2)
    cond=np.where(np.logical_and(arreglo[:,colx-1]<verti1x,arreglo[:,colx-1]>verti2x))
    cond2=np.where(np.logical_and(arreglo[:,coly-1]<verti1y,arreglo[:,coly-1]>verti2y))
    output_cuadrado=arreglo[np.intersect1d(cond,cond2)]
    corx_cua=output_cuadrado[:,colx-1]
    cory_cua=output_cuadrado[:,coly-1]
    return output_cuadrado,corx_cua,cory_cua


if option==1:
    ################## CIRCUMFERENCE OUTPUT  ###########################################################
    opt="circ_"   #is added to the start of the name of the output file, to recognize the chosen option
    output_arreglo,coordenadas_x,coordenadas_y=circulo(centerX_user,centerY_user,radio_user,df)
    ################## representative plot of the data #######################################
    plt.scatter (x,y)
    plt.scatter (coordenadas_x,coordenadas_y,c="red")
    plt.xlim(centerX_user-(radio_user+(radio_user*0.7)),centerX_user+radio_user+(radio_user*0.7))
    plt.ylim(centerY_user-(radio_user+(radio_user*0.7)),centerY_user+radio_user+(radio_user*0.7))

    
elif option==2:
     ##################  SQUARE OUTPUT ###########################################################
    opt="squ_"  #is added to the start of the name of the output file, to recognize the chosen option
    output_arreglo,coordenadas_x,coordenadas_y=cuadrado(centerX_user,centerY_user,lado_user,df)
    ################## Prepresentative plot of the data  #######################################
    plt.scatter(x,y)
    plt.scatter(coordenadas_x,coordenadas_y,c="red")
    plt.xlim(centerX_user-(lado_user+(lado_user*0.3)),centerX_user+lado_user+(lado_user*0.3))
    plt.ylim(centerY_user-(lado_user+(lado_user*0.3)),centerY_user+lado_user+(lado_user*0.3))


#################################### OUTPUT FILE ######################################################
#output format, first two columns are the coord., the other columns are given the 4.2f format
formato="%11.7f %11.7f" + " %4.2f"*(l_col-2)  
np.savetxt(opt+name_output_file,np.c_[output_arreglo],fmt=formato)  #output file



    