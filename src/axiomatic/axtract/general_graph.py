from .axtract_report import EquationExtraction, EquationExtractionResponse
from pyvis.network import Network

def normalize_latex_symbol(symbol: str) -> str:
    """
    Normalizes LaTeX symbols by removing unnecessary outer braces.
    For example: '{\vec{r}}' and '\vec{r}' will both become '\vec{r}'
    
    Args:
        symbol: LaTeX symbol string
    Returns:
        Normalized symbol string
    """
    # Remove outer braces if they exist
    symbol = symbol.strip()
    while symbol.startswith('{') and symbol.endswith('}'):
        symbol = symbol[1:-1].strip()
    return symbol

def generate_graph(equations_response: EquationExtractionResponse, output_path: str):
    """
    Generates a standalone HTML file with a bipartite graph visualization.
    Green nodes represent equations, red nodes represent variables.
    
    Args:
        equations_response: EquationExtractionResponse object
        output_path: Path where to save the HTML file
    """
    
    # Create a new network
    net = Network(
        height="900px",
        width="100%",
        bgcolor="#ffffff",
        font_color="#000000"
    )
    
    # Track all variables to avoid duplicates
    all_variables = set()
    
    # Get the equations list from the response object
    equations = equations_response.equations
    
    # Add equation nodes (green) and variable nodes (red)
    for eq in equations:
        # Add equation node with unique identifier
        eq_name = f"Eq: {eq.name} ({eq.id})"  # Add ID to make each node unique
        net.add_node(
            eq_name,
            label=eq.name,
            color="#90EE90",  # Light green for equations
            shape="box",
            size=30,
            font=dict(
                size=14,
                color="#000000"  # Black text for better contrast on light green
            ),
            title=f"{eq.name}\n{eq.original_format}\n{eq.description}"
        )
        
        # Add variable nodes and edges
        for symbol in eq.latex_symbols:
            # Normalize the variable name
            var_name = normalize_latex_symbol(symbol.key)
            if var_name not in all_variables:
                net.add_node(
                    var_name,
                    label=var_name,
                    color="#E74C3C",  # Red for variables
                    shape="dot",
                    size=20,
                    font=dict(
                        size=16,
                        color="#000000"
                    ),
                    title=f"{var_name}: {symbol.value}"
                )
                all_variables.add(var_name)
            
            # Add edge between equation and variable
            net.add_edge(eq_name, var_name, color="#7F8C8D", width=1.5)
    
    # Configure physics for better layout
    net.set_options("""
    {
      "physics": {
        "barnesHut": {
          "gravitationalConstant": -2000,
          "centralGravity": 0.3,
          "springLength": 150,
          "springConstant": 0.04,
          "damping": 0.09,
          "avoidOverlap": 0.1
        },
        "minVelocity": 0.75
      }
    }
    """)
    
    # Save the graph
    net.save_graph(output_path)