import os

import diagrams.custom
from diagrams import Diagram

# Define the output directory and filename
output_directory = "output"  # Replace with your desired folder name
output_filename = os.path.join(output_directory, "virtual_thread")  # Full path to save the file

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Define graph attributes for a dark webpage
graph_attr = {
    "bgcolor": "back",  # Transparent background to blend with dark webpage
    "fontname": "Helvetica",   # Clean font for better readability
    "fontsize": "18",          # Font size for text
    "fontcolor": "white",      # Font color for overall graph text
    "penwidth": "1.5",         # Slightly thicker lines for better visibility
    "rankdir": "LR",           # Left to Right direction for the diagram
    "label": "Virtual Thread Lifecycle",
    "labelloc": "t",
    "dpi": "300",
    "style": "filled",
    "splines": "ortho",       # Change to "polyline", "spline", "curved", "ortho", "none", or "line" as needed
}

# Define node attributes
node_attr = {
    "color": "lightgray",      # Light gray color for edges
    "fillcolor": "#2b2b2b",    # Dark gray fill color for nodes
    "fontcolor": "white",      # White font color for node text
    "fontname": "Helvetica",   # Clean font for better readability
    "fontsize": "18",          # Font size for node text
    "penwidth": "1.5",         # Slightly thicker lines for nodes
    "labelfontsize": "18",  # Font size for labels, smaller to create space
    "labelloc": "m",  # Position label below the icon (node)
}

# Define edge attributes
edge_attr = {
    "color": "lightgray",      # Light gray color for edges
    "penwidth": "1.5",         # Thicker edge lines for better visibility
    "fontcolor": "white",      # White font color for edge labels (if any)
    "fontname": "Helvetica",   # Clean font for better readability
    "arrowhead": "normal",  # Normal arrowhead style
    "arrowtail": "none",  # No tail to make connection clearer
}

with Diagram(show=True, filename=output_filename, outformat="png", graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr):
    new = diagrams.custom.Node("New \n(Created)")
    runnable = diagrams.custom.Node("Runnable")
    running = diagrams.custom.Node("Running")
    blocked = diagrams.custom.Node("Blocked \n(Waiting)")
    terminated = diagrams.custom.Node("Terminated")

    new >> runnable >> running >> [blocked, terminated]
    blocked >> runnable
