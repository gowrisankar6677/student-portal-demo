

**\*(When this file is viewed on GitHub, the diagram will render automatically.)\***



**---**



**### \*\*2. Python Script to Generate Flowchart Image\*\***  

**```python**

**# file: create\_flowchart.py**

**from graphviz import Digraph**



**dot = Digraph()**



**dot.node("A", "Start")**

**dot.node("B", "Is it raining?")**

**dot.node("C", "Take an umbrella")**

**dot.node("D", "Wear sunglasses")**

**dot.node("E", "Go outside")**



**dot.edges(\["AB", "BC", "BD"])**

**dot.edge("C", "E")**

**dot.edge("D", "E")**



**dot.render("flowchart", format="png", cleanup=True)**

**print("Flowchart saved as flowchart.png")**



