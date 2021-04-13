from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np

back_ground_path = '/home/mcliu/program/multi-area-model-master/simulations/draw_figure/img_all_areas/background/Brian7.png'
font_path = '/home/mcliu/program/multi-area-model-master/simulations/draw_figure/data/msyh.ttf'
# picture_1 = Image.open('/home/mcliu/program/multi-area-model-master/simulations/draw_figure/img_6_monkey/background/picture_1.png')
# picture_1 = picture_1.resize((600, 300))
picture_2 = Image.open('/home/mcliu/program/multi-area-model-master/simulations/draw_figure/img_all_areas/background/paste_picuure2.jpg')
picture_2 = picture_2.resize((359, 450))
# areas = ['V1', 'V2']
# pos = [(1215, 720), (1040, 620)]
# areas = ['V4', 'FEF']
# pos= [(570, 820), (175, 460)]
# areas = ['V1', 'V2', 'V4', 'FEF', 'VP', 'FST', 'V3A', 'MT', 'V4t', 'PITd', 'AITv', '46']
areas = ['V1', 'V2', 'V4', 'FEF', 'PO', 'VIP', 'CITv', 'FST', '46']
# areas = ['V1', 'V2']
# pos = [(1215, 720), (1040, 620), (570, 820), (175, 460), (745, 495), (640, 10),
#        (900, 200), (470, 180), (250, 90), (635, 330), (360, 570), (5, 290)]
pos = [(1215, 720), (1040, 620), (900, 200), (175, 460), (640, 10), (635, 330), (575, 820), (745, 495), (5, 290)]
# pos = [(745, 495), (640, 10)]

window_step = 5
window_size = 100
window_number = (1000 - window_size) / window_step

sub_path = '/home/mcliu/program/multi-area-model-master/simulations/draw_figure/img_all_areas/'
# icon = Image.open('/home/mcliu/program/multi-area-model-master/simulations/draw_figure/img_1000_singlar/area_V1/Raster_48.png')

# img_w, img_h = img.size


# print(img_w)


# def transparent_back(img):
#     threshold = 100
#     dist = 5
#     img = img.convert('RGBA')
#     arr = np.array(np.asarray(img))
#     print(arr)
#     r, g, b, a = np.rollaxis(arr, axis=-1)
#     mask = ((r > threshold)
#             & (g > threshold)
#             & (b > threshold)
#             & (np.abs(r - g) < dist)
#             & (np.abs(r - b) < dist)
#             & (np.abs(g - b) < dist))
#     arr[mask, 3] = 0
#     img = Image.fromarray(arr, mode='RGBA')
#     # img.show()
#     return img


def paste_img(img_1, img_2, position, a):
    img_1.paste(img_2, position, mask=a)
    return img_1


def get_path(path):
    img_path = []
    for area in areas:
        area_path = path + 'area_' + area + '/'
        img_path.append(area_path)
        # print(area_path)
    return img_path


path = get_path(sub_path)
# print(path)

filenames = []
for filename in os.listdir(path[0]):
    filenames.append(filename)

for i in range(len(filenames)):
    img = Image.open(back_ground_path)
    img_w, img_h = img.size
    # for w in range(img_w):
    #     for h in range(img_h):
    #         r, g, b = img.getpixel((w, h))
    #         # print(r)
    #         if (r <= 100) & (g <= 100) & (b <= 100):
    #             img.putpixel((w, h), (0, 0, 0))
    #         else:
    #             img.putpixel((w, h), (255, 255, 255))

    img = img.resize((1400, 1200))
    # img.show()
    # img = img.convert('RGBA')
    index = filenames[i][7: -4]

    for j in range(len(areas)):
        img_sub = Image.open('{0}{1}'.format(path[j], filenames[i]))
        img_sub = img_sub.resize((200, 200))
        # img_sub = transparent_back(img_sub)
        r, g, b, a = img_sub.split()
        # picture1_r, picture1_g, picture1_b, picture1_a = picture_1.split()

        image = paste_img(img, img_sub, pos[j], a)
        # image = paste_img(image, picture_1, (0, 850), picture1_a)
        image.paste(picture_2, (0, 650))

        font = ImageFont.truetype(font=font_path, size=20)
        draw = ImageDraw.Draw(image)
        draw.text((pos[j][0] + 90, pos[j][1] - 10), '{}'.format(areas[j]), fill=(0, 0, 0), font=font)
    font_txt = ImageFont.truetype(font=font_path, size=30)
    set_time = window_size + window_step * float(index)
    # draw.text((995, 100), 'simulation time: {} (ms)'.format(set_time), fill=(0, 0, 0), font=font_txt)
    draw.text((995, 0), 'simulation time: {} (ms)'.format(set_time), fill=(0, 0, 0), font=font_txt)
    # image.show()
    image.save('/home/mcliu/program/multi-area-model-master/simulations/draw_figure/img_all_areas/topology_img/Raster_{}.png'.format(index))
    print("Saving......")


# image = icon.resize((200, 200))
# img.paste(image, (600, 30), mask=None)
# img.show()