from pydantic import BaseModel
import numpy as np

class DictItem(BaseModel):
    key: str
    value: str


class EquationExtraction(BaseModel):
    id: str
    name: str
    description: str
    original_format: str
    latex_symbols: list[DictItem]
    narrative_assumptions: list[str]


class EquationExtractionResponse(BaseModel):
    equations: list[EquationExtraction]




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

def create_report(report_data: EquationExtractionResponse, report_path: str):
    """
    Creates an HTML report for the extracted equations.
    """
    html_content = HTML_HEAD + """
    <body>
        <div class="menu-bar">
            <button class="menu-button" onclick="alert('Validating equations...')">Validate Equations</button>
            <button class="menu-button" onclick="alert('Running numerical optimization...')">Numerical Optimization</button>
            <button class="menu-button" onclick="alert('Deriving relations...')">Derive Relations</button>
            <button class="menu-button" onclick="showHypergraph()">Relation Graph</button>
        </div>
        
        <h1>Equation Extraction Report</h1>
        <div class="container">
            <div class="equation-list">
    """
    
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
    
    # Add the graph
    html_content += generate_hypergraph(report_data.equations)
    
    # Close all remaining tags
    html_content += """
                </div>
            </div>
        </div>
        
        <!-- Vis.js library for network visualization -->
        <script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
        
        <script>
            function showHypergraph() {
                document.getElementById('hypergraph-modal').style.display = 'block';
                if (typeof initGraph === 'function') {
                    setTimeout(initGraph, 100);
                }
            }
            
            function hideHypergraph() {
                document.getElementById('hypergraph-modal').style.display = 'none';
            }
        </script>
    </body>
    </html>
    """
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(html_content)


