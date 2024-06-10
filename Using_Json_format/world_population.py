import json
from country_codes import get_country_code
from pygal_maps_world.maps import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
#  Loading the data
filename = "population_data.json"

with open(filename) as f:
    pop_data = json.load(f)

#   Dict. of population data for each country
cc_population = {}
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population
        
#  Group the countries into 3 population levels
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop

# See how many countries are in each level
print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))

wm_style = RS("#336699", base_style=LCS)
wm = World(style = wm_style)
wm._title = "World Population in 2010, by Country" 
wm.add("0-10M", cc_pop_1)
wm.add("10M-1Bn", cc_pop_2)
wm.add("> 1Bn", cc_pop_3) 

wm.render_to_file("world_pops.svg")