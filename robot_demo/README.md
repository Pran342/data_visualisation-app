## Function Documentation
```
### 1. init_session()
**Function**: Initialize session state  
**Input**: None  
**Output**: None  
**Note**: Creates 11 session_state variables to control interface states, including `json_data` (processed network data) and `show_left_panel` (left panel visibility status).

### 2. process_capability_data(raw_data)
**Function**: Raw data transformation  
**Input**:  
- `raw_data: List[Dict]` - Raw event stream JSON array  
**Output**:  
python
{
  "nodes": List[Dict],  # Node list (with id/real_name/type attributes)
  "edges": List[Dict],  # Weighted edges (with source/target/time attributes)
  "min_timestamp": float,  # Minimum timestamp
  "max_time": float      # Maximum time span
}

3. json_editor_component()
​​Function​​: Dual-column JSON editor
​​Input​​: None
​​Output​​: None
​​Note​​: Transfers data through st.session_state.raw_json with real-time syntax highlighting and validation.

4. build_network_graph(data)
​​Function​​: Network graph construction
​​Input​​:
data: Dict - Output from process_capability_data
​​Output​​:
nx.DiGraph - Directed graph with attributes
​​Node Attributes​​:
label: Display label
real_name: Original name
node_type: capability/provider
color: Node color
size: Node size

5. generate_network_graph(data)
​​Function​​: Network visualization rendering
​​Input​​:
data: Dict - Output from process_capability_data
​​Output​​:
plt.Figure - Matplotlib figure object
​​Exception​​: Returns None if generation fails

6. plot_path(G, path, title)
​​Function​​: Path highlighting visualization
​​Input​​:
G: nx.DiGraph - Network graph
path: List[str] - Node ID sequence
title: str - Chart title
​​Output​​: None
​​Effect​​: Directly renders path diagram in Streamlit

7. path_analysis_panel()
​​Function​​: Path analysis control panel
​​Input​​: None
​​Output​​: None
​​Side Effect​​: Updates st.session_state.path_results with three path calculation results

8. main()
​​Function​​: System entry function
​​Input:None
Output:None
