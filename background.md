I want to quickly create a fancy demo of an agent system for a product demo.

The demo front end should show a graph of the agent system, with nodes representing the agents and edges representing the messages between them.
It should be dark theme. We'll use neon colors. if an agent is talking, it's neon color should glow.


We also want to show the use of MCP servers and tool usage

Let's create a dummy agent system that does the following:

1. Raises a customer support ticket suggesting that a recommender system recommendations are not working for a customer.
2. Assign the ticket to a manager agent.
3. Assing the ticket to an analyst agent. The analyst agent uses an MCP server to call a tool that looks at the customers in a similar segments recommendations (Segments by Age, Country, Customer Value)
4. The analyst agent finds these customers tend to like games with a higher volatility.
5. The analyst agent raises a ticket to the machine learning expert agent to fix the issue and increase the priority of recommendations
6. A suggested fix is sent to a security agent to approve.
7. The security agent checks using SEMGREP MCP server to see if the fix is safe.
8. A machine learning expert checks the fix, approves it.
9. The Machine learning engineer announces the fix is ready to deploy to the manager agent.


“Support → Fix → Announce” loop (end-to-end).

Front end dark themed, neon colors.
Build a tiny React app that streams agent events to a live graph view:

Renderer- consider the following ideas, but customize:

React Flow (battle-tested node editor; easy custom nodes + edges). Use ELK.js or Dagre for clean layered layouts; React Flow has examples with ELK baked in.
React Flow
+1
GitHub

Or Cytoscape.js if you need big-graph performance and graph algorithms (centrality, filtering).
js.cytoscape.org
PMC

Layout: ELK (layered/DAG) → great for “tool call pipelines.” Dagre is a simpler alternative.
GitHub
+1

Event stream: Your agent runtime emits JSON events (agent_started, tool_called, message_sent, approval_wait, error) over WebSocket/SSE; the frontend updates nodes/edges live.

Status UX that demos well:

Node color by state (idle/running/blocked/error).

Edge thickness by token or latency.

Click a node → right pane shows prompt, output, cost, and artifacts (file links, PR URLs).

“Approve” button on human-in-the-loop nodes (mirrors LangGraph’s HITL pattern).
LangChain AI

Tie-in to your stack: if you’re using LangGraph already, you can emit the same traces to LangSmith/Phoenix for deep dive while your React view handles the showpiece.
LangSmith
Arize AI