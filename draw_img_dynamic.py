import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio

'''
set parameters of moving window
'''
# ms
window_step = 5
window_size = 100
window_number = (1000 - window_size) / window_step
'''
what areas are needed
'''
# areas = ['V1', 'V2', 'V4', 'FEF', 'VP', 'FST', 'V3A', 'MT', 'V4t', 'PITd', 'AITv', '46']
# areas = ['V3A', 'MT', 'V4t', 'PITd', 'AITv', '46']
areas = ['V1', 'V2', 'V4', 'FEF', 'PO', 'VIP', 'CITv', 'FST', '46']
# populations name
populations = ['23E', '23I', '4E', '4I', '5E', '5I', '6E', '6I']
yticks = ['23', '4', '5', '6']
# ticks = [2, 4, 6, 8]

# the location where the activation pulse data is saved
path = '/home/mcliu/program/multi-area-model-master/simulations/draw_figure/data/'

# the location where the neuron network gids data is saved
gids = open('/home/mcliu/program/multi-area-model-master/simulations/draw_figure/data/network_gids.txt')
g = gids.readlines()

'''
extract the gids of the required areas from the total gids
'''
def check_network_gids(gids):
    length = len(gids)
    for i in range(length - 1, -1, -1):
        # print(i)
        area, pop, gid_1, gid_2 = gids[i].split(',')
        if area not in areas:
            del gids[i]
            length -= 1
    return gids


'''
calculate the id of the first neuron in each area
'''
def first_ids(gids, areas):
    for i in range(len(gids)):
        area, pop, gids_1, gids_2 = gids[i].split(',')
        if (area == areas) & (pop == '23E'):
            id = float(gids_1)
    return id


'''
extract the data of the required area from the total neuron pulse activation data
'''
def generator_area_data(gids, data, areas):
    neuron_id = []
    times = []
    index = []
    for i in range(len(gids)):
        area, pop, gid_1, gid_2 = gids[i].split(',')

        if area == areas:
            gid1_1 = float(gid_1)
            gid2_2 = float(gid_2)
            # print(gid1_1)
            # print(gid2_2)

            for j in range(len(data)):
                if (data[j][0] >= gid1_1) & (data[j][0] <= gid2_2):
                    index.append(j)
    for i in index:
        neuron_id.append(data[i][0])
        times.append(data[i][1])
    return neuron_id, times


'''
extract the required population data from the area
'''
def generator_pop_data(gids, neuron, time, population, first):
    neuron_id = []
    times = []
    index = []
    for i in range(len(gids)):
        area, pop, gid_1, gid_2 = gids[i].split(',')

        if pop == population:
            gid1_1 = float(gid_1)
            gid2_2 = float(gid_2)
            # print(gid1_1)
            # print(gid2_2)

            for j in range(len(neuron)):
                if (neuron[j] >= gid1_1) & (neuron[j] <= gid2_2):
                    index.append(j)
    for i in index:
        neuron_id.append(neuron[i] - first)
        times.append(time[i])
    return neuron_id, times


'''
extract the last neuron id of each population in each desired area
'''
def pop_gid(gids, areas, population, id):
    for i in range(len(gids)):
        area, pop, gid_1, gid_2 = gids[i].split(',')
        if (pop == population) & (area == areas):
            return float(gid_2) - id


'''
draw a scatter plot
'''
def plot_raster(x, y, gids, windows_stp, local, population):
        # set the excitation spike to bule and the inhibition to red
        if population.find('E') > (-1):
            my_color = 'b'
        else:
            my_color = 'r'
        # print(my_color)
        plt.scatter(x, y, c=my_color, s=10)

        # plot the population dividing line
        plt.ylim((0, ticks[-1]))
        plt.xlim((0, window_size))
        # plt.xlabel('Times (ms)')
        # plt.ylabel('neuron ID')
        # plt.title('area: {}'.format(local))


for local in areas:
    # local_path = '{0}spikes_{1}.mat'.format(path, local)
    local_path = path + 'spikes_all.mat'
    data = scio.loadmat(local_path)['a'].tolist()
    # print(d)
    # print(str_to_float(Dataset))
    # print(times)
    input_g = check_network_gids(g)
    # print(input_g)
    first_id = first_ids(input_g, local)
    print(first_id)
    neuron_id, times = generator_area_data(input_g, data, local)
    ticks = []
    a = 0
    for pop in populations:
        pop_id = pop_gid(input_g, local, pop, first_id)
        if a % 2 != 0:
            ticks.append(pop_id)
        a += 1
    print(ticks)
    # plt.figure()
    for i in range(int(window_number)):
        time = []
        neuron = []
        plt.figure()
        for j in range(len(times)):
            if (times[j] >= i * window_step) & (times[j] < (i * window_step + window_size)):
                # if times[j] < (i + 1) * window_size:
                time.append(times[j] - i * window_step)
                # neuron.append(neuron_id[j] - first_id)
                neuron.append(neuron_id[j])

        for population in populations:
            # print(population)
            neuron_id_1, times_1 = generator_pop_data(input_g, neuron, time, population, first_id)
            # print(neuron_id_1)
            # print(times_1)
            plot_raster(times_1, neuron_id_1, input_g, i * window_step, local, population)

        plt.yticks(ticks, yticks)
        for pop_value in ticks:
            plt.axhline(pop_value, c='k', lw=0.5)
        plt.show()
        # plt.savefig('/home/mcliu/program/multi-area-model-master/simulations/draw_figure/img_6_monkey/area_{0}/Raster_{1}.png'.format(local, i + 1),
        #             transparent=True)
        print("Saving......")