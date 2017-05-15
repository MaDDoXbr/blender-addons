import bpy
op = bpy.context.active_operator

op.at_cursor = True
op.smooth_mesh = True
op.tri_face = False
op.sphere_mesh = True
op.subdivision_x = 128
op.subdivision_y = 128
op.meshsize = 2.0
op.meshsize_x = 2.0
op.meshsize_y = 2.0
op.random_seed = 387
op.x_offset = 0.0
op.y_offset = 0.0
op.noise_size = 1.0
op.noise_size_x = 1.0
op.noise_size_y = 1.0
op.noise_type = 'planet_noise'
op.basis_type = '3'
op.vl_basis_type = '3'
op.distortion = 1.0299999713897705
op.hard_noise = '0'
op.noise_depth = 1
op.amplitude = 0.5
op.frequency = 2.0
op.dimension = 1.0
op.lacunarity = 2.0
op.moffset = 1.0
op.gain = 1.0
op.marble_bias = '0'
op.marble_sharp = '0'
op.marble_shape = '0'
op.height = 1.0
op.invert = True
op.offset = 0.0
op.edge_falloff = '0'
op.falloff_size_x = 4.0
op.falloff_size_y = 4.0
op.edge_level = 0.0
op.plateaulevel = 1.0
op.sealevel = -1.0
op.strata = 5.0
op.strata_type = '3'
op.water_plane = False
op.water_level = 0.009999999776482582
op.use_mat = False
op.sel_land_mat = ''
op.sel_water_mat = ''
op.show_noise_settings = True
op.show_terrain_settings = True
op.refresh = True
op.auto_refresh = True