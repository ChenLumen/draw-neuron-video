from PIL import Image
import os


path = '/home/mcliu/program/multi-area-model-master/simulations/draw_figure/img_all_areas/picture/'
picture_path = '/home/mcliu/program/multi-area-model-master/simulations/draw_figure/img_all_areas/topology_img/'


num = 1
filenames = []
for filename in os.listdir(path):
    filenames.append(filename)
picture_names = []
for name in os.listdir(picture_path):
    picture_names.append(name)

length = len(picture_names)
slice_pic = length / len(filenames)

for i in range(len(filenames)):
    image = Image.open('{0}ppt{1}.JPG'.format(path, i + 1))
    image = image.resize((2000, 1100))
    for j in range(length * num):
        if (j <= (i + 1) * slice_pic * num) & (j >= i * slice_pic * num):
            if j % num == 0:
                 img = Image.open('{0}Raster_{1}.png'.format(picture_path, int(j / num + 1)))
                 img = img.resize((1250, 1050))
                 image.paste(img, (50, 30))
                 # index = picture_names[j][7: -4]
            # image.show()
            image.save('/home/mcliu/program/multi-area-model-master/simulations/draw_figure/img_all_areas/topology_new_img/Raster_{}.png'.format(j + 1))
            print('Saving......')