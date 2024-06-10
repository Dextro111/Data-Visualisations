from pygal_maps_world.maps import World

wm = World()
wm.title = "Population of Countries In North America"
wm.add("North America", {"ca": 1000, "us": 100000, 'mx': 1000})

wm.render_to_file("NA_pops.svg")