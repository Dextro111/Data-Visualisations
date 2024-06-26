import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#   Make an API call and store the Response

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status Code:", r.status_code)

#   Store API response in a variable
response_dict = r.json()
print("Total Repositories:", response_dict["total_count"])

#  Explore information about the repo
repo_dicts = response_dict['items']
#print("Repositories returned:", len(repo_dicts))

#  Examine the first repo
#repo_dict = repo_dicts[0]
# print("\nSelected information about first repository:")
# for repo_dict in repo_dicts:
#     print("Name:", repo_dict["name"])
#     print("Owner:", repo_dict["owner"]["login"])
#     print("Stars:", repo_dict["stargazers_count"])
#     print("Repository:", repo_dict["html_url"])
#     print("Created:", repo_dict["created_at"])
#     print("Updated:", repo_dict["updated_at"])
#     print("Description:", repo_dict["description"])
    
# print("\nkeys:", len(repo_dict))
#for key in sorted(repo_dict.keys()):
#    print(key)
names, plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    
    plot_dict = {
        "value": repo_dict["stargazers_count"],
        "label": repo_dict["description"],
        "xlink": repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

#  Make Visualizations
my_style = LS("#333366", base_style=LCS)

#  Store Configurations
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size =18
my_config.truncate_label= 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred Python Projects On Github"
chart.x_labels = names

chart.add("", plot_dicts)
chart.render_to_file('repos.svg')