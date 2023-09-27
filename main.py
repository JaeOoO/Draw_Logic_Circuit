import schemdraw
from schemdraw.parsing import logicparse
import streamlit as st

schemdraw.theme('default')

st.title('Logic Expression To Logic Circuit')
st.text('made by JaeOoO')
st.text('')
expression = st.text_input('Write Your Logic Expression')
if st.button('Submit'):

    st.write(expression)

    with logicparse(expression) as drw:
        drw.save('temp.svg', transparent=False)
        image_bytes = drw.get_imagedata('svg')

    st.image('temp.svg')
    st.image(image_bytes)

    st.download_button(label='Download data as SVG', data=image_bytes, file_name='MyCircuit.svg')