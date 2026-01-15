## Design Overview

### City Graph
The city will be represented as a weighted graph using custom adjacency lists.

### Trip State Machine
Trips move through:
REQUESTED → ASSIGNED → ONGOING → COMPLETED
or CANCELLED.

### Rollback Strategy
A stack-based rollback manager will restore previous system states.

### GUI
Tkinter is used for desktop GUI.
