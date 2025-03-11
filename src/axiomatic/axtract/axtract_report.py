from .relation_graph import generate_relation_graph
from .. import EquationExtractionResponse
import os
import re

HTML_HEAD = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Equation Extraction Report</title>
        <meta charset="UTF-8">
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script id="MathJax-script" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <style>
            :root {
                --system1-bg: #fff;
                --system1-text: #000;
                --system1-border: #000;
                --system1-highlight: #000;
            }
            
            body { 
                font-family: 'Chicago', 'Helvetica', sans-serif;
                margin: 8px; 
                padding: 0;
                background-color: var(--system1-bg);
                color: var(--system1-text);
                font-size: 12px;
            }
            
            /* Menu Bar Styles */
            .menu-bar {
                background: var(--system1-bg);
                border-bottom: 1px solid var(--system1-border);
                padding: 2px;
                display: flex;
                gap: 16px;
                margin-bottom: 8px;
            }
            
            .menu-button {
                background: var(--system1-bg);
                border: 1.5px solid var(--system1-border);
                border-radius: 8px;
                padding: 2px 8px;
                font-family: 'Chicago', 'Helvetica', sans-serif;
                font-size: 12px;
                cursor: pointer;
                position: relative;
                white-space: nowrap;
            }
            
            .menu-button:active {
                background: var(--system1-text);
                color: var(--system1-bg);
            }
            
            h1 { 
                margin: 0 0 16px 0;
                padding: 4px;
                font-size: 14px;
                font-weight: bold;
                text-align: center;
                border-bottom: 1.5px solid var(--system1-border);
            }
            
            .container {
                display: flex;
                gap: 16px;
                height: calc(100vh - 100px);
            }
            
            .equation-list {
                width: 300px;
                border: 1.5px solid var(--system1-border);
                border-radius: 8px;
                padding: 8px;
                overflow-y: auto;
            }
            
            .equation-item { 
                border: 1.5px solid transparent;
                margin-bottom: 12px;
                padding: 8px;
                cursor: pointer;
                border-radius: 4px;
            }
            
            .equation-item:hover { 
                background: var(--system1-text);
                color: var(--system1-bg);
            }
            
            .equation-item.active {
                background: var(--system1-text);
                color: var(--system1-bg);
            }
            
            .details-panel {
                flex: 1;
                border: 1.5px solid var(--system1-border);
                border-radius: 8px;
                padding: 16px;
                overflow-y: auto;
            }
            
            .details-panel.empty {
                display: flex;
                align-items: center;
                justify-content: center;
                font-style: italic;
            }
            
            .equation-details h2 {
                margin: 0 0 16px 0;
                font-size: 14px;
                text-align: center;
            }
            
            .equation-details p {
                margin: 16px 0 8px 0;
            }
            
            .symbol-table { 
                width: 100%; 
                border-collapse: collapse;
                margin-top: 8px;
                border: 1.5px solid var(--system1-border);
            }
            
            .symbol-table td, .symbol-table th { 
                border: 1px solid var(--system1-border);
                padding: 6px 8px;
                text-align: left;
            }
            
            .symbol-table th {
                background: var(--system1-text);
                color: var(--system1-bg);
                font-weight: bold;
            }
            
            .equation-title {
                margin: 0 0 8px 0;
                font-size: 12px;
                font-weight: bold;
            }

            /* MathJax container spacing */
            .mjx-chtml {
                margin: 8px 0 !important;
            }

            /* Classic System 1 scrollbar */
            ::-webkit-scrollbar {
                width: 16px;
                height: 16px;
            }
            
            ::-webkit-scrollbar-track {
                background: var(--system1-bg);
                border: 1.5px solid var(--system1-border);
            }
            
            ::-webkit-scrollbar-thumb {
                background: var(--system1-text);
                border: 1.5px solid var(--system1-border);
            }
            
            ::-webkit-scrollbar-button {
                display: none;
            }
        </style>
        <script>
            function showDetails(eqId) {
                document.querySelectorAll('.equation-item').forEach(item => {
                    item.classList.remove('active');
                });
                
                document.getElementById('eq-item-' + eqId).classList.add('active');
                
                document.querySelectorAll('.equation-details').forEach(detail => {
                    detail.style.display = 'none';
                });
                document.getElementById('empty-message').style.display = 'none';
                document.getElementById('details-' + eqId).style.display = 'block';
            }
        </script>
    </head>
"""


def create_report(report_data: EquationExtractionResponse, report_path: str = "./report.html"):
    """
    Creates an HTML report for the extracted equations.
    """
    html_content = (
        HTML_HEAD
        + """
    <body>
        <div class="menu-bar">
            <a href="#" onclick="showHypergraph()">Relation Graph</a>
        </div>
        
        <h1>Equation Extraction Report</h1>
        <div class="container">
            <div class="equation-list">
    """
    )

    # Add equations to the list
    for i, eq in enumerate(report_data.equations):
        html_content += f"""
                <div class="equation-item" id="eq-item-{i}" onclick="showDetails({i})">
                    <div class="equation-title">{eq.name}</div>
                    \\[{eq.original_format}\\]
                </div>
        """

    html_content += """
            </div>
            <div class="details-panel">
                <div id="empty-message" style="text-align: center; color: #666;">
                    Select an equation to view details
                </div>
    """

    # Add equation details
    for i, eq in enumerate(report_data.equations):
        html_content += f"""
                <div class="equation-details" id="details-{i}" style="display: none;">
                    <h2>{eq.name}</h2>
                    <p><strong>Description:</strong></p>
                    <p>{eq.description}</p>
                    
                    <p><strong>Original Format:</strong></p>
                    \\[{eq.original_format}\\]
                    
                    <p><strong>Symbols:</strong></p>
                    <table class="symbol-table">
                        <tr>
                            <th>Symbol</th>
                            <th>Description</th>
                        </tr>
        """

        for symbol in eq.latex_symbols:
            html_content += f"""
                        <tr>
                            <td>\\({symbol.key}\\)</td>
                            <td>{symbol.value}</td>
                        </tr>
            """

        html_content += """
                    </table>
                </div>
        """

    html_content += """
            </div>
        </div>
        
        <!-- Graph Modal -->
        <div id="hypergraph-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
             background: rgba(0,0,0,0.8); z-index: 1000;">
            <div style="position: relative; width: 90%; height: 90%; margin: 2% auto; background: var(--system1-bg); 
                 padding: 20px; border-radius: 8px; overflow: hidden;">
                <button onclick="hideHypergraph()" style="position: absolute; right: 10px; top: 10px; z-index: 1001;" 
                        class="menu-button">Close</button>
                <div id="graph-container" style="width: 100%; height: 100%;">
    """

    # Generate the relation graph as a separate HTML file
    graph_html = generate_relation_graph(report_data.equations)
    graph_file_path = os.path.join(os.path.dirname(report_path), "relation_graph.html")
    with open(graph_file_path, "w", encoding="utf-8") as f:
        f.write(graph_html)

    # Extract just the graph content from the full HTML
    # This avoids duplicate HTML, head, body tags
    graph_content = extract_graph_content(graph_html)
    html_content += graph_content

    # Add the relation graph link to the main menu with proper styling
    html_content = html_content.replace(
        '<a href="#" onclick="showHypergraph()">Relation Graph</a>',
        f'<a href="{os.path.basename(graph_file_path)}" target="_blank" class="menu-button">Relation Graph</a>',
    )

    # Remove the menu-item related code since we're using menu-button class
    html_content = re.sub(r"\.menu-item \{.*?\}", "", html_content, flags=re.DOTALL)

    # Remove the showHypergraph and hideHypergraph functions
    html_content = re.sub(
        r"<script>\s*function showHypergraph\(\).*?function hideHypergraph\(\).*?</script>",
        "",
        html_content,
        flags=re.DOTALL,
    )

    # Close all remaining tags if needed
    if "</div></div></div>" not in html_content:
        html_content += """
                </div>
            </div>
        </div>
        """

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html_content)


def extract_graph_content(graph_html: str) -> str:
    """
    Extracts the relevant graph content from the full HTML generated by pyvis.

    Args:
        graph_html: Full HTML string from pyvis

    Returns:
        String containing just the graph-specific content
    """
    # Find where the actual graph content starts (after the body tag)
    body_start = graph_html.find("<body>")
    if body_start != -1:
        content_start = body_start + len("<body>")
        # Find where the content ends (before closing body tag)
        body_end = graph_html.find("</body>")
        if body_end != -1:
            # Extract just the graph content
            return graph_html[content_start:body_end]

    # Fallback if we can't parse it properly
    return graph_html
