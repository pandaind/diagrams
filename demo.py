from diagrams import Diagram, Edge, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
import os

# Define the output directory and filename
output_directory = "output"  # Replace with your desired folder name
output_filename = os.path.join(output_directory, "demo")  # Full path to save the file

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
    "label": "Web Service Architecture",
    "labelloc": "t",
    "dpi": "300",
    "style": "filled",
    "splines": "curved",       # Change to "polyline", "spline", "curved", "ortho", "none", or "line" as needed
}

# Define node attributes
node_attr = {
    "fillcolor": "#2b2b2b",    # Dark gray fill color for nodes
    "fontcolor": "white",      # White font color for node text
    "fontname": "Helvetica",   # Clean font for better readability
    "fontsize": "18",          # Font size for node text
    "penwidth": "1.5",         # Slightly thicker lines for nodes
    "labelfontsize": "18",  # Font size for labels, smaller to create space
    "labelloc": "b",  # Position label below the icon (node)
    "margin": "0.6,0.5", # Increased vertical margin for more space between icon and label
    #"shape": "box",  # Box shape for nodes for a cleaner look
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

# Pass the graph, node, and edge attributes to the Diagram object
with Diagram(show=False, filename=output_filename, outformat="png", graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr):
    lb = ELB("\nLoad Balancer")
    # Create a cluster for web servers
    with Cluster("Web Cluster", graph_attr={"bgcolor": "#1e1e1e", "fontcolor": "white", "margin": "20", "nodesep": "1"}):
        web1 = EC2("\nWeb Server 1")
        web2 = EC2("\nWeb Server 2")
    db = RDS("\nUser Database")

    # Define common edge style
    traffic_edge = Edge(label="routes traffic", fontcolor="white", fontsize="18", fontname="Helvetica")
    data_edge = Edge(label="stores data", fontcolor="white", fontsize="18", fontname="Helvetica")

    # Connect nodes using the defined edge styles
    lb >> traffic_edge >> [web1,
                           web2] >> data_edge >> db