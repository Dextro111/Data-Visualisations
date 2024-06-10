from pygal_maps_world.maps import World

wm = World()
wm.title = "North, Central and South America"

wm.add("North America", ["ca", 'mx', "us"])
wm.add("Central America", ['bz', 'cr', 'gt', 'hm', 'ni', 'pa', 'sv'])
wm.add("South America", ['ar','bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy' 'pe', 'py', 'sr', 'uy', 've'])
wm.add("Dex_World", ["ng", "gh"], c="green")

wm.render_to_file("America.svg")