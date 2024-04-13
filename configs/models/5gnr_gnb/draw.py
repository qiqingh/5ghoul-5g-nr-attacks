import json
from graphviz import Digraph

# Load the state machine from the JSON file
with open('nr-softmodem.json', 'r') as file:
    state_machine = json.load(file)

# Create a new directed graph for visualizing the state machine
dot = Digraph(comment='State Machine')

# Add nodes (states) to the graph
for state in state_machine['StatesNodes']:
    dot.node(state, state)

# Add edges (transitions) to the graph
for state, transitions in state_machine['StatesTransitions'].items():
    if transitions.get('to_state'):
        for to_state, details in transitions['to_state'].items():
            dot.edge(state, details['dst_state_name'], label=details.get('trigger', 'No Trigger'))

# Render the graph to a file (e.g., as a PNG image)
dot.render('state_machine', format='png', view=True)
