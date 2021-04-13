import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio


# areas = ['V1', 'V2', 'V4', 'FEF', 'VP', 'FST', 'V3A', 'MT', 'V4t', 'PITd', 'AITv', '46']
# areas = ['V3A', 'MT', 'V4t', 'PITd', 'AITv', '46']
# areas = ['V1', 'V2', 'V4', 'FEF', 'PO', 'VIP', 'CITv', 'FST', '46']
areas = ['V1']
populations = ['23E', '23I', '4E', '4I', '5E', '5I', '6E', '6I']
yticks = ['23', '4', '5', '6']
# ticks = [2, 4, 6, 8]

path = '/home/mcliu/program/multi-area-model-master/simulations/draw_figure/data/'

gids = open('/home/mcliu/program/multi-area-model-master/simulations/draw_figure/data//network_gids.txt')
g = gids.readlines()


def check_network_gids(gids):
    length = len(gids)
    for i in range(length - 1, -1, -1):
        # print(i)
        area, pop, gid_1, gid_2 = gids[i].split(',')
        if area not in areas:
            del gids[i]
            length -= 1
    return gids


def first_ids(gids, areas):
    for i in range(len(gids)):
        area, pop, gids_1, gids_2 = gids[i].split(',')
        if (area == areas) & (pop == '23E'):
            id = float(gids_1)
    return id


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


def pop_gid(gids, areas, population, id):
    for i in range(len(gids)):
        area, pop, gid_1, gid_2 = gids[i].split(',')
        if (pop == population) & (area == areas):
            return float(gid_2) - id


def plot_raster(x, y, gids, local, population):

    # for local in areas:
    #     plt.figure()
    #     for i in range(len(gids)):
            # set the excitation spike to bule and the inhibition to red
            if population.find('E') > (-1):
                my_color = 'b'
            else:
                my_color = 'r'
            # print(my_color)

            # limit areas spike data
            plt.scatter(x, y, c=my_color, s=10)

            # plot the population dividing line
            # for pop_value in ticks:
            #     plt.axhline(pop_value, c='k', lw=0.5)
            # print(my_x)
            # print(my_y)
            # plt.ylabel(local)

            plt.ylim((0, ticks[-1]))
            plt.xlim((0, 1000))
            # plt.xlabel('Times (ms)')
            # plt.ylabel('neuron ID')
            # plt.title('area: {}'.format(local))


for local in areas:
    # local_path = '{0}spikes_{1}.mat'.format(path, local)
    local_path = path + 'spikes_all.mat'
    data = scio.loadmat(local_path)['a'].tolist()
    # print(data)
    input_g = check_network_gids(g)
    # print(input_g)
    first_id = first_ids(input_g, local)
    # print(first_id)
    neuron_id, times = generator_area_data(input_g, data, local)
    # print(neuron_id)
    # print(times)
    ticks = []
    a = 0
    for pop in populations:
        pop_id = pop_gid(input_g, local, pop, first_id)
        if a % 2 != 0:
            ticks.append(pop_id)
        a += 1
    print(ticks)
    plt.figure()

    for population in populations:
        # print(population)
        neuron_id_1, times_1 = generator_pop_data(input_g, neuron_id, times, population, first_id)
        # print(neuron_id_1)
        # print(times_1)
        plot_raster(times_1, neuron_id_1, input_g, local, population)

    plt.yticks(ticks, yticks)
    for pop_value in ticks:
        plt.axhline(pop_value, c='k', lw=0.5)
    plt.title('{}'.format(local))
    # plt.show()
    plt.savefig('/home/mcliu/program/multi-area-model-master/simulations/draw_figure/{}.png'.format(local))
    print("Saving......")
# plt.figure()
# plt.scatter(times, neuron_id)
# plt.show()