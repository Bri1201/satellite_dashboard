import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.express as px
import pycountry
import warnings
from wordcloud import WordCloud
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
import figures
from figures import fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, world_map1, world_map2, wordcloud

data = pd.read_excel('data.xlsx', sheet_name='Database')
# Set page title and introduction
st.set_page_config(
    page_title="Satellite Visualisation",
    page_icon=":satellite:",
    layout="centered",
)

st.title(":satellite: Satellite Data Visualisation")
st.write("This data is sourced from UCS Satellite Database, which contains in-depth details on the 6,718 satellites "
         "currently orbiting Earth, including their country of origin, purpose, and other operational details.")
st.markdown("Assembled by experts at the Union of Concerned Scientists (UCS), the Satellite Database is a listing of "
            "the more than 6,718 operational satellites currently in orbit around Earth.")
st.markdown("Our intent in producing a dashboard as an exploration tool for specialists and non-specialists alike by "
            "visualising the data on operational satellites and presenting it in a format that can be easily "
            "interacted with for research and analysis.")

st.write("Click [here](https://www.ucsusa.org/resources/satellite-database) to visit the official website.")

st.title(":card_index: Attributes In Visualisation")
items = [
    "Name of Satellite, Alternate Names",
    "Country/Org of UN Registry",
    "Country of Operator/Owner",
    "Operator/Owner",
    "Users",
    "Purpose",
    "Detailed Purpose",
    "Class of Orbit",
    "Type of Orbit",
    "Contractor",
    "Comments"

]
explanations = [
    "The current or most popularly used name is listed first, with alternate or previously used names given in "
    "parentheses. ",
    "This indicates the country that is registered as responsible for the satellite in the United Nations Register of "
    "Space Objects. http://www.unoosa.org/oosa/en/osoindex.html “NR” indicates that the satellite has never been "
    "registered with the United Nations. ",
    "The satellite’s current operational controller. The operator is not necessarily the satellite’s owner, "
    "satellites may be leased. ",
    "The affiliation of the primary users of the satellite is described with one or more of the keywords: civil ("
    "academic, amateur), commercial, government (meteorological, scientific, etc.), military. Satellites can be "
    "multi-use, hosting, for example, dedicated transponders for both commercial and military applications. ",
    "The discipline in which the satellite is used in broad categories. The purposes listed are those self-reported "
    "by the satellite’s operator. A slash between terms indicates the satellite is used for multiple purposes. More "
    "detail on the purpose is given in column G ",
    "This column gives more detail about the satellite’s purpose, for example, Earth Observation satellites may "
    "perform Earth Science, Meteorology, Electronic Intelligence, Optical or Radar Imaging, etc. ",
    "Gives more detail about the usage",
    "We divide satellite orbits into two broad classes: (1) nearly circular orbits and (2) elliptical orbits.",
    "Nearly Circular Orbits are further classified:  Equatorial—low earth equatorial orbit, with inclination between "
    "0º and 20º Nonpolar Inclined—low earth intermediate orbit, with inclination between 20º and 85º Polar—low earth "
    "polar orbit, with inclination between 85º and 95º and greater than 104º Sun-synchronous—low earth "
    "sun-synchronous orbit, with inclination approximately between 95º and 104º, with sun-synchronous relationship "
    "between altitude and inclination  Elliptical Orbits are also further classified, as well:2  • Cislunar refers to "
    "cislunar orbits, which have an apogee greater than 318,200 km.  • Deep Highly Eccentric refers to deep highly "
    "eccentric earth orbits, which have orbital period greater than 25 hours and eccentricity greater than 0.5.  • "
    "Molniya refers to orbits with period between 11.5 and 12.5 hours, eccentricity between 0.5 and 0.77, "
    "and inclination between 62º and 64º. ",
    "The prime contractor for the satellite’s construction. The construction of satellites generally involves a "
    "number of subcontractors as well. Frequent corporate mergers mean that the name listed as the prime contractor "
    "may not be the name of that corporation today. ",
    "Comments on the purpose and ownership"
]

col1, col2 = st.columns(2)
with col1:
    # Display subheaders for each item
    for k in range(int(len(items)/2)+1):
        st.subheader(":page_facing_up: "+items[k])
        st.write(explanations[k])
with col2:
    for k in range(int(len(items)/2)+1, len(items)):
        st.subheader(":page_facing_up: "+items[k])
        st.write(explanations[k])

#Figure 1

st.header("\n\n:bar_chart: Figure 1: Distribution Of Owners")
st.plotly_chart(fig1, use_container_width=True)
st.write("This pie charts shows us the distribution of the countries who own satellites around the world")
st.write("Interactivity: Hover over the plot to see the count and country.")
st.write("              -Click on a legend to remove a country from the visualisation")

#Figure 2

st.header(":bar_chart: Figure 2: Purpose Of Satellites")
st.plotly_chart(fig2, use_container_width=True)
st.write("Visualisation to see what the satellites are being used for and the count of the same."
         "\nInteractivity: Hover over to see exact count!")


# Add more figures following the same structure (Figure 3 to Figure 9)

#Figure 3
st.header(":bar_chart: Figure 3: Number Of Satellites Launched By Contractor")
st.plotly_chart(fig3, use_container_width=True)
st.write("This graph describes the number of satellites launched by a contractor in a given year")
st.write("Interactivity: Hover over the dots to see exact counts\n "       
         "-Click on a legend to visualise "
         "without a given contractor")

#Figure 4
st.header(":bar_chart: Figure 4: Distribution Of Type & Class Of Orbit")
st.plotly_chart(fig4, use_container_width=True)
st.write("An Icicle to visualise distribution of type of orbit and class of orbit")
st.write("Interactivity: Click on a section to enlarge and hover to view details")

#Figure 5
st.header(" :bar_chart: Figure 5: Satellite Distribution by Country, and operator/owner(Sunburst)")
st.plotly_chart(fig5, use_container_width=True)
st.write("This graph can be used to visualise the country and operator/owner ")
st.write("Interaction: CLick on any of the parents to enlarge and hover to view details")

#Figure 6
st.header(":bar_chart: Figure 6: Satellite Distribution by Country, and operator/owner followed by Users(Treemap)")
st.plotly_chart(fig6, use_container_width=True)
st.write("This graph can be used to visualise the country and operator/owner ")
st.write("Interactivity: Click on any area to inspect in detail")

#Figure 7
st.header(":bar_chart: Figure 7: Satellite distribution by purpose and specific purpose (sunburst)")
st.plotly_chart(fig7, use_container_width=True)
st.write("A sunburst diagram to visualise the purpose of usage")
st.write("Interactivity : Click on a slice to interact in detail")

#Figure 8
st.header(":bar_chart: Figure 8: Satellite distribution by purpose and specific purpose (Treemap)")
st.plotly_chart(fig8, use_container_width=True)
st.write("A Treemap diagram to visualise the purpose of usage")
st.write("Interactivity : Click on a slice to interact in detail")

#Figure 9

all_comments = ' '.join(data['Comments'].dropna())

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_comments)

# Plot the WordCloud using Matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Comments')


st.header(":bar_chart: Figure 9: WordCloud of Comments describing use")
st.pyplot(plt)
st.write("visualisation of comments")

#Figure 10
st.header(":bar_chart: Figure 10: Number Of Satellite registered by each country by count")
st.plotly_chart(world_map1, use_container_width=True)
st.write("Choropleth map understanding the distribution of satellite ownership around the world")
st.write("Conclusion: Hover to see details about the given satellite")

#Figure 11
st.header(":bar_chart: Figure 11. Number Of Satellite registered by each country by Percentile")
st.plotly_chart(world_map2, use_container_width=True)
st.write("Choropleth map understanding the distribution of satellite ownership around the world")
st.write("Conclusion: Hover to see details about the given satellite")

# Continue adding figures (Figure 4 to Figure 9)

# You can customize the placeholders with your actual figures and content

# Footer and conclusion
st.markdown("Made by Brinda, Kadambari, Vanshika, Tharun")



