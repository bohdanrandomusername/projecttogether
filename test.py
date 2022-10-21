import streamlit as st
import pandas as pd
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

import streamlit as st
import psycopg2

# Initialize connection.
# Uses st.experimental_singleton to only run once.
#@st.experimental_singleton
#def init_connection():
#    return psycopg2.connect(**st.secrets["postgres"])

#conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
#@st.experimental_memo(ttl=600)
#def run_query(query):
#    with conn.cursor() as cur:
#        cur.execute(query)
#        return cur.fetchall()

#rows = run_query("SELECT * from messages;")
#zip_rows = list(zip(*rows))
#zip_map = list(zip(("id", "ts", "msg", "channel_id", "lang"), zip_rows))
#st.write(pd.DataFrame({k: vals for k, vals in zip_map}))
# Print results.
#for row in rows:
#    st.write(row)
