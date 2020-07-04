from skimage import io,img_as_ubyte
import matplotlib.pyplot as plt
import numpy as np
import moviepy.editor as mpy
import glob



def get_matrix_rgb(nombre_de_imagen):
    matrix = io.imread(nombre_de_imagen)
    return matrix

def convertion_gris(nombre_de_imagen,r_1,g_1,b_1):
    image = get_matrix_rgb(nombre_de_imagen)
    h,w,c = image.shape 
    image_bw = np.zeros((h,w))
    for i in range(h):
        for j in range(w): 
            valr=image[i,j,0]
            valg=image[i,j,1]
            valb=image[i,j,2]
            image_bw[i,j] = r_1*float(valr)+g_1*float(valg)+b_1*float(valb)
    return image_bw

def convertion_blak_white(image,r_1,g_1,b_1,umbral):
    imag_rgb = get_matrix_rgb(image)
    h,w,c = imag_rgb.shape 
    image_bw = np.zeros((h,w))
    for i in range(h):
        for j in range(w): 
            valr=imag_rgb[i,j,0]
            valg=imag_rgb[i,j,1]
            valb=imag_rgb[i,j,2]
            var = r_1*float(valr)+g_1*float(valg)+b_1*float(valb)
            if var>=umbral:
                image_bw[i,j] = 1                
    return image_bw

def mostrar_imagen_de_array(imagen):
    plt.rcParams['image.cmap'] = 'gray'
    plt.imshow(imagen)
    plt.title("Imagen en blanco y negro")
    plt.show()

# -------------------Animación-----------------------------------------------------
def create_frames(image,r_1,g_1,b_1):
    plt.rcParams['image.cmap'] = 'gray'
    imag_rgb = get_matrix_rgb(image)
    h,w,c = imag_rgb.shape 
    images = []
    for umbral in range (60,130):
        image_bw = np.zeros((h,w))
        for i in range(h):
            for j in range(w): 
                valr=imag_rgb[i,j,0]
                valg=imag_rgb[i,j,1]
                valb=imag_rgb[i,j,2]
                var = r_1*float(valr)+g_1*float(valg)+b_1*float(valb)
                if var>=umbral:
                    image_bw[i,j] = 1
        images.append(image_bw)
    plt.rcParams['image.cmap'] = 'gray'
    fps = 7
    clip = mpy.ImageSequenceClip(images,scale = 1.0)
    clip.write_gif('movie.gif')
    #io.imsave("Images/Frames/imag_generada{0:0000006d}.png".format(umbral-59),img_as_ubyte(image_bw))

def animar():
    plt.rcParams['image.cmap'] = 'gray'
    file_list = sorted(glob.glob("./Images/Frames/*.png"))
    fps = 71
    clip = mpy.ImageSequenceClip(file_list, fps=fps)
    clip.write_gif('movie.gif')


imagen = "Images/lena.png"
#i_matri_rgb = get_matrix_rgb(imagen)
#i_matri_gris = convertion_gris(imagen,0.2126,0.7152,0.0722)
#i_matri_bw = convertion_blak_white(imagen,0.2126,0.7152,0.0722,120)
#mostrar_imagen_de_array(i_matri_bw)
create_frames(imagen,0.2126,0.7152,0.0722)
#animar()
