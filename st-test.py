import streamlit as st
import plotly.graph_objects as go

def sankey(sources = None, targets = None, values = None, labels = None, 
node_pad = 15, node_thickness = 20, line_color = 'black', line_width = 
0.5, title = "Diagram"):
    label = labels or ["A1", "A2", "B1", "B2", "C1", "C2"]
    source = sources or [0, 0, 1, 1, 2, 2]
    target = targets or [2, 3, 3, 4, 4, 5]
    value = values or [8, 4, 2, 8, 4, 2]

    print("source =", source)
    print("target =", target)
    print("label =", label)
    print("value =", value)

    fig = go.Figure(go.Sankey(
        node = dict(
            pad=node_pad,
            thickness=node_thickness,
            line = dict(color = line_color, width = line_width),
            label = labels,
            color = "green"
        ),
        link = dict(
            source=source,
            target=target,
            value=value
        )
    ))
    fig.update_layout(title_text=title)
    
    return fig

st.write("TEST")
st.plotly_chart(sankey())
st.write("TEST")
