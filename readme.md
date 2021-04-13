The xxx-spikes-0001-0.gdf file recorded by the macaque brain network needs to be run, and converted into a. mat file and a neuron id file network_gids.txt recorded in all areas and populations.

When running these scripts, it is necessary to modify the suffix gdf of xxx-spikes-0001-0.gdf file to mat, using matlab to convert the gdf format file to mat format:

a = load('');
save('', a);

draw_img_static.py: This file is used to draw the static map of the required brain areas.

draw_img_dynamic: This file is used to draw the subgraph of the dynamic graph of the time window.

draw_topology: This file is used to paste the drawn subgraphs to the required scene in sequence.

draw_video: This file is used to splice all the generated topological subgraphs into cideo in time sequence.

draw_new_topology: This file is used to paste the topological subgraph of background image onto the background image with text description.
