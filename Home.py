import streamlit as st
import pandas

# sets page layout to wide (I forgot to do this)
st.set_page_config(layout="wide")

# good to use header (another mistake)
st.header("Elevated Tracking")
st.text("""
Elevated Tracking has 15 years of experience in helping corporations track and reduce 
their emissions. Our customers gain a deep understanding of where there emissions are
coming from allowing them to cut them quickly. on average customers can see a 30% 
reduction in emission in the first 6 months.
""")

# good to use sub header, (anouther mistake)
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

# NOTE - sep is defaulted to ","
df = pandas.read_csv("data.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        # header should have been writen with an f String & ".title" to capitalize names
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.text(row["role"])
        # could have been writen - (images/" + row["image"])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.text(row["role"])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in df[8:12].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.text(row["role"])
        st.image(f"images/{row['image']}")