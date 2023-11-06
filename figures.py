import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pandas as pd
import plotly.express as px
import pycountry
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Define your figures
# You can replace fig1, fig2, etc. with your actual figures
data = pd.read_excel('data.xlsx', sheet_name='Database')
data = data.drop(columns=[col for col in data.columns if col.startswith('Unnamed')])
data_owners = data['Country of Operator/Owner'].value_counts().reset_index(name='Counts')
data_owners.columns = ['Country of Operator/Owner', 'Counts']
fig1 = px.pie(
    data_owners,
    names='Country of Operator/Owner',
    values="Counts",
    color="Counts",
    title=" ")
fig1.update_traces(textposition='inside')
fig1.update_layout(
    uniformtext_minsize=12,
    uniformtext_mode='hide',
    margin=dict(l=10, r=10, t=50, b=10),
    paper_bgcolor="mintcream",
    title=dict(x=0.5)
)

data_purpose = data['Purpose'].value_counts().reset_index(name='Counts')
data_purpose.columns = ['Purpose', 'Counts']
fig2 = px.bar(
    data_purpose[:5],
    x='Purpose',
    y="Counts",
    color="Counts",
    title=" ")
fig2.update_layout(
    margin=dict(l=10, r=10, t=50, b=10),
    paper_bgcolor="#D6EAF8",
    title=dict(x=0.5))

data['Date of Launch'] = pd.to_datetime(
    data['Date of Launch'], errors='coerce').dt.strftime('%d-%m-%Y')
data['Date of Launch'] = data['Date of Launch'].map(lambda x: str(x)[-4:])
data_contractors = data['Contractor'].value_counts().reset_index(name='Counts')
data_contractors.columns = ['Contractor', 'Counts']
data_contractors.sort_values(by='Counts', ascending=False, inplace=True,)
top_contractors = data_contractors['Contractor'].head(6).to_list()
data_contractors_date = data[[
    'Date of Launch', 'Contractor']].value_counts().reset_index(name='Counts')
data_contractors_date.sort_values(by='Date of Launch', inplace=True,)
data_contractors_date = data_contractors_date[data_contractors_date['Contractor'].isin(
    top_contractors)]
fig3 = px.line(
    data_contractors_date,
    x="Date of Launch",
    y="Counts",
    color='Contractor',
    markers=True,
    title=" ")
fig3.update_layout(
    margin=dict(l=10, r=10, t=50, b=10),
    paper_bgcolor="papayawhip",
    title=dict(x=0.5))

newDf = data[['Class of Orbit', 'Type of Orbit']]
orbit_counts = data.groupby(['Class of Orbit','Type of Orbit']).size().reset_index(name='Count')
total_count = orbit_counts['Count'].sum()

# Add a new column 'Percentage' to store the percentage of counts
orbit_counts['Percentage'] = (orbit_counts['Count'] / total_count) * 100
descriptions = [r"A non-inclined orbit is an orbit coplanar with a plane of reference. <br>The orbital inclination is "
                r"0° for prograde orbits, and π (180°) for retrograde ones.<br> If the plane of reference is a "
                r"massive spheroid body's equatorial plane, <br>these orbits are called equatorial; if the plane of "
                r"reference <br>is the ecliptic plane, they are called ecliptic. ",
                r"A Sun-synchronous orbit (SSO), also called a heliosynchronous orbit, <br> is a nearly polar orbit "
                r"around a planet, in which the satellite passes over any <br>given point of the planet's surface at "
                r"the same local mean solar time.",
                r"A polar orbit is one in which a satellite passes above or nearly above<br> both poles of the body being orbited (usually a planet such as the Earth, but possibly<br> another body such as the Moon or Sun) on each revolution. It has an <br>inclination of about 60 - 90 degrees to the body's equator.[1] A <br>satellite in a polar orbit will pass over the equator at a different longitude <br>on each of its orbits. ",
                r"A near-equatorial orbit is an orbit that lies close to the equatorial <br>plane of the object "
                r"orbited. Such an orbit has an inclination near 0°. On Earth, such <br>orbits lie on the celestial "
                r"equator, the great circle of the imaginary <br>celestial sphere on the same plane as the equator of "
                r"Earth",
                r"A Molniya orbit is a type of satellite orbit designed to provide communications <br>and remote sensing coverage over high latitudes. It is a highly elliptical <br>orbit with an inclination of 63.4 degrees, an argument of perigee of 270 <br>degrees, and an orbital period of approximately half a sidereal <br>day.",
                r"A deep highly eccentric orbit (HEO) is an elliptic orbit with high eccentricity, <br>usually "
                r"referring to one around Earth. Examples of inclined HEO orbits <br>include Molniya orbits, "
                r"named after the Molniya Soviet communication satellites<br> which used them, and Tundra orbits. ",
                r"In astrodynamics or celestial mechanics, an elliptic orbit or elliptical orbit <br>is a Kepler orbit with an eccentricity of less than 1; this includes the <br>special case of a circular orbit, with eccentricity equal to 0. In a stricter <br>sense, it is a Kepler orbit with the eccentricity greater than 0 <br>and less than 1 (thus excluding the circular orbit). In a wider sense, it is <br>a Kepler's orbit with negative energy. This includes the radial elliptic orbit, with eccentricity equal to 1. ",
                r"A synchronous orbit is an orbit in which an orbiting body (usually a satellite) <br>has a period equal to the average rotational period of the body being orbited<br> (usually a planet), and in the same direction of rotation as that body.[1] ",
                r"Cislunar is Latin for 'on this side of the moon' and generally refers to the <br>volume between Earth and the moon. Cislunar space includes LEO, Medium Earth <br>Orbit, GEO, as well as other orbits, such as Low Lunar Orbit and NRHO, the <br>intended orbit for the Gateway.28"]


fig4 = px.icicle(orbit_counts, path=[ 'Class of Orbit',"Type of Orbit"], values='Percentage')
fig4.update_traces(root_color="lightgrey")
fig4.update_layout(margin = dict(t=50, l=25, r=25, b=25))

# Select the relevant columns
dN = data[['Country of Operator/Owner', 'Operator/Owner', 'Users']]

# Remove rows with missing data (NaN)
dN = dN.dropna()

# Count the number of satellites for each combination of 'Country', 'Operator/Owner', and 'Users'
dN = dN.groupby(['Country of Operator/Owner', 'Operator/Owner', 'Users']).size().reset_index(name='Count')

fig5 = px.sunburst(dN, path=['Country of Operator/Owner', 'Operator/Owner'], values='Count')

# Customize the layout if needed
fig5.update_layout(title=' ')

fig6 = px.treemap(dN, path=['Country of Operator/Owner', 'Operator/Owner', 'Users'], values='Count')

# Customize the layout if needed
fig6.update_layout(title=' ')

# Show the tree map

# Select the relevant columns
#'Users', 'Purpose','Detailed Purpose'
dN2 = data[['Users', 'Purpose', 'Detailed Purpose']]

# Remove rows with missing data (NaN)
dN2 = dN2.dropna()

# Count the number of satellites for each combination of 'Country', 'Operator/Owner', and 'Users'
dN2 = dN2.groupby(['Users', 'Purpose', 'Detailed Purpose']).size().reset_index(name='Count')

fig7 = px.sunburst(dN2, path=['Users', 'Purpose', 'Detailed Purpose'], values='Count')

# Customize the layout if needed
fig7.update_layout(title=' ')

fig8 = px.treemap(dN2, path=['Users', 'Purpose', 'Detailed Purpose'], values='Count')

# Customize the layout if needed
fig8.update_layout(title=' ')

countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_3


data_country = data['Country of Operator/Owner'].value_counts().reset_index(name='Count')
data_country.columns = ['Country of Operator/Owner', 'Count']

codes = [countries.get(country, country)
         for country in data_country['Country of Operator/Owner']]
data_country['iso_codes'] = codes
data_country['iso_codes'] = data_country['iso_codes'].replace(
    ['Russia', 'South Korea', 'Bolivia', 'Venezuela', 'Czech Republic', 'Laos', 'China/Sri Lanka'], ['RUS', 'KOR', 'BOL', 'VEN', 'CZE', 'LAO', 'LKA'])
data_country['percentile'] = data_country['Count'].rank(
    method='max').apply(lambda x: 100.0*(x-1)/(len(data_country)-1))


world_map1 = px.choropleth(data_country, locations="iso_codes",
                           color="Count",
                           color_continuous_scale="deep",
                           hover_data=['Country of Operator/Owner', 'Count'],
                           title=" ",
                           height=600,
                           width=1500)

world_map1.update_layout(
    margin=dict(l=10, r=10, t=50, b=10),
    title=dict(x=0.5))

world_map2 = px.choropleth(data_country, locations="iso_codes",
                           color="percentile",
                           color_continuous_scale="deep",
                           range_color=(0, 100),
                           hover_data=['Country of Operator/Owner', 'Count'],
                           title=" ",
                           height=600,
                           width=1500)

world_map2.update_layout(
    margin=dict(l=10, r=10, t=50, b=10),
    title=dict(x=0.5))

all_comments = ' '.join(data['Comments'].dropna())

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_comments)

# Plot the WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Comments')
#plt.show()
wordcloud_image = "wordcloud.png"
plt.savefig(wordcloud_image, bbox_inches='tight')
