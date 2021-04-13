import cv2

img_path = '/home/mcliu/program/multi-area-model-master/simulations/draw_figure/img_all_areas/topology_new_img/'
fps = 8
# size = (640, 480)
# size = (1400, 1200)
size = (2000, 1100)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
videoWriter = cv2.VideoWriter('/home/mcliu/program/multi-area-model-master/simulations/draw_figure/img_all_areas/topology_new_video/video2.avi',
                              fourcc, fps, size)

for i in range(1000):
    frame = cv2.imread(img_path+'Raster_'+str(i+1)+'.png')
    videoWriter.write(frame)
    print("Creating......")
videoWriter.release()