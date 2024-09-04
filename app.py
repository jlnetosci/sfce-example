import streamlit as st
from st_flexible_callout_elements import flexible_error, flexible_success, flexible_warning, flexible_info, flexible_callout
from streamlit_extras.add_vertical_space import add_vertical_space
from time import sleep

def display_rainbow_text():
    colors = [
        {"text": "You", "bg_color": "#D8A0D8", "font_color": "#6A0D91"},
        {"text": "can", "bg_color": "#C2C2F0", "font_color": "#4B0082"},
        {"text": "also", "bg_color": "#99CCFF", "font_color": "#0033CC"},
        {"text": "do", "bg_color": "#B3FFB3", "font_color": "#009900"},
        {"text": "some", "bg_color": "#FFFF99", "font_color": "#CCCC00"},
        {"text": "fun", "bg_color": "#FFCC99", "font_color": "#CC6600"},
        {"text": "stuff", "bg_color": "#FFB3B3", "font_color": "#B30000"}
    ]

    with st.container():
        cols = st.columns(len(colors))
        for col, color in zip(cols, colors):
            with col:
                flexible_callout(
                    color["text"],
                    background_color=color["bg_color"],
                    font_color=color["font_color"],
                    font_size=18,
                    alignment="center",
                    padding=5
                )

st.title("Streamlit flexible callout elements")
st.sidebar.title("Flexible callout elements")

st.markdown("""
    <div style="text-align: justify;">
        This is an example page for the <a href="https://pypi.org/project/st-flexible-callout-elements/" target="_blank"><code>st-flexible-callout-elements</code></a> library. 
        For details please read the <a href="https://github.com/jlnetosci/st-flexible-callout-elements" target="_blank">documentation</a>.
    </div>
    """, unsafe_allow_html=True)

add_vertical_space(1)

flexible_error("This is a slightly larger error message.", font_size=20)
with st.expander("See code"):
    st.code('''flexible_error("This is a slightly larger error message", font_size=20)''', language="python")

add_vertical_space(1)

flexible_success("This is a centered success message", alignment="center")
with st.expander("See code"):
    st.code('''flexible_success("This is a centered success message", alignment="center")''', language="python")

add_vertical_space(1)

flexible_warning("This is right aligned a warning message <b><u>with html elements</b></u>", alignment="right")
with st.expander("See code"):
    st.code('''flexible_warning("This is a right aligned warning message <b><u>with html elements</b></u>", alignment="right"))''', language="python")

add_vertical_space(1)

flexible_info("This is a slightly smaller info message", font_size=10)
with st.expander("See code"):
    st.code("""flexible_info("This is a slightly smaller info message", font_size=10)""", language="python")

add_vertical_space(1)

flexible_callout("This is the standard flexible callout.")
with st.expander("See code"):
    st.code('''flexible_callout("This is a standard custom flexible callout.")''', language="python")

add_vertical_space(1)

flexible_callout("You can use custom colors!", background_color="#E0B0FF", font_color="#301934")
with st.expander("See code"):
    st.code('''flexible_callout("You can use custom colors!", background_color="#E0B0FF", font_color="#301934")''', language="python")

add_vertical_space(1)

display_rainbow_text()
with st.expander("See code"):
    st.code("""def display_rainbow_text():
    colors = [
        {"text": "You", "bg_color": "#D8A0D8", "font_color": "#6A0D91"},
        {"text": "can", "bg_color": "#C2C2F0", "font_color": "#4B0082"},
        {"text": "also", "bg_color": "#99CCFF", "font_color": "#0033CC"},
        {"text": "do", "bg_color": "#B3FFB3", "font_color": "#009900"},
        {"text": "some", "bg_color": "#FFFF99", "font_color": "#CCCC00"},
        {"text": "fun", "bg_color": "#FFCC99", "font_color": "#CC6600"},
        {"text": "stuff", "bg_color": "#FFB3B3", "font_color": "#B30000"}
    ]

    with st.container():
        cols = st.columns(len(colors))
        for col, color in zip(cols, colors):
            with col:
                flexible_callout(
                    color["text"],
                    background_color=color["bg_color"],
                    font_color=color["font_color"],
                    font_size=18,
                    alignment="center",
                    padding=5
                )

display_rainbow_text()""", language="python")

st.sidebar.markdown("""
    <div style="text-align: justify;">
        Please see the examples in the main page first.
    </div>
    """, unsafe_allow_html=True)

with st.sidebar:
    add_vertical_space(1)

flexible_info("Can be used in the sidebar.", container=st.sidebar)
with st.sidebar.expander("See code"):
    st.code("""flexible_info("Can be used in the sidebar.", container=st.sidebar)""", language="python")

with st.sidebar:
    add_vertical_space(1)

flexible_callout("Can have rounded boxes.", container=st.sidebar, background_color="#FFCCF2", font_color="#CC3385", border_radius=25)
with st.sidebar.expander("See code"):
    st.code("""flexible_callout("Can have rounded boxes.", container=st.sidebar, background_color="#FFCCF2", font_color="#CC3385", border_radius=25)""", language="python")

with st.sidebar:
    add_vertical_space(1)

flexible_callout("If the text is long it can also be justified within the element.", container=st.sidebar, alignment="justify", background_color="#99E6E6", font_color="#006666")
with st.sidebar.expander("See code"):
    st.code("""flexible_callout("If the text is long it can also be justified within the element.", container=st.sidebar, alignment="justify", background_color="#99E6E6", font_color="#006666")""", language="python")

with st.sidebar:
    add_vertical_space(1)

flexible_callout("Line height can also be customized within the element", container=st.sidebar, background_color="#FFD1C1", font_color="#CC5733", line_height=2)
with st.sidebar.expander("See code"):
    st.code("""flexible_callout("Line height can also be customized within the element", container=st.sidebar, background_color="#FFD1C1", font_color="#CC5733", line_height=2))""", language="python")
