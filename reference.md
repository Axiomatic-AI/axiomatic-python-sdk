# Reference
<details><summary><code>client.<a href="src/axiomatic/base_client.py">trigger_error_sentry_debug_get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.trigger_error_sentry_debug_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/axiomatic/base_client.py">health_check_health_check_get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.health_check_health_check_get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## requirements
<details><summary><code>client.requirements.<a href="src/axiomatic/requirements/client.py">check</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic, UserRequirement

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.requirements.check(
    request=[
        UserRequirement(
            latex_symbol="latex_symbol",
            requirement_name="requirement_name",
            tolerance=1.1,
            value=1.1,
            units="units",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Sequence[UserRequirement]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## lean
<details><summary><code>client.lean.<a href="src/axiomatic/lean/client.py">execute</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.lean.execute(
    code="code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lean.<a href="src/axiomatic/lean/client.py">suggest</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.lean.suggest(
    prompt="prompt",
    code_prefix="code_prefix",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**code_prefix:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## experimental
<details><summary><code>client.experimental.<a href="src/axiomatic/experimental/client.py">assistant</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Interactive assistant for IDE extension
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.experimental.assistant(
    query="query",
    context="context",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## formalization
<details><summary><code>client.formalization.<a href="src/axiomatic/formalization/client.py">formalize</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Formalize a query into a dictionary of constraints
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.formalization.formalize(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[typing.Literal["PIC"]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.formalization.<a href="src/axiomatic/formalization/client.py">validate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validate a set of values with respect to a dictionary of constraints
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic, FormalizeResponse

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.formalization.validate(
    constraints=FormalizeResponse(
        variables={"key": "value"},
        expressions=[],
    ),
    values={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**constraints:** `FormalizeResponse` 
    
</dd>
</dl>

<dl>
<dd>

**values:** `typing.Dict[str, str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## generic
<details><summary><code>client.generic.<a href="src/axiomatic/generic/client.py">statement</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.generic.statement(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Document
<details><summary><code>client.document.<a href="src/axiomatic/document/client.py">text</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Extracts text from documents
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.document.text()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**method:** `typing.Optional[str]` — Method to use for text-only extraction.It uses a very simple pdf text extractor. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document.<a href="src/axiomatic/document/client.py">parse</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Extracts text from documents. It uses advanced pdf segmentation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.document.parse()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**method:** `typing.Optional[str]` — Method to use for text extraction
    
</dd>
</dl>

<dl>
<dd>

**ocr:** `typing.Optional[bool]` — Whether to use OCR
    
</dd>
</dl>

<dl>
<dd>

**layout_model:** `typing.Optional[str]` — Method for layout parsing
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tools
<details><summary><code>client.tools.<a href="src/axiomatic/tools/client.py">schedule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schedule a job to execute python code for long running executions and return the standard output. If an error occurs, it will be returned in the error_trace field. The Following tools are currently supported: fdtd, femwell, optiland, jaxfem
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.tools.schedule(
    tool_name="tool_name",
    code="code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/axiomatic/tools/client.py">status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of the remote execution job for a given tool using the job_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.tools.status(
    job_id="job_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CodeExecution Python
<details><summary><code>client.code_execution.python.<a href="src/axiomatic/code_execution/python/client.py">execute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute python code, and return the standard output. If an error occurs, it will be returned in the error_trace field. Importing from the following modules is supported: gdsfactory, z3, json
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.code_execution.python.execute(
    code="code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Formalization Constraints
<details><summary><code>client.formalization.constraints.<a href="src/axiomatic/formalization/constraints/client.py">verify</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verifies that a set of constraints are consistent
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic, FormalizeResponse

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.formalization.constraints.verify(
    constraints=FormalizeResponse(
        variables={"key": "value"},
        expressions=[],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**constraints:** `FormalizeResponse` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Formalization Solution
<details><summary><code>client.formalization.solution.<a href="src/axiomatic/formalization/solution/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Finds a solution to a set of constraints provided partial values
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic, FormalizeResponse

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.formalization.solution.find(
    constraints=FormalizeResponse(
        variables={"key": "value"},
        expressions=[],
    ),
    values={"key": 1},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**constraints:** `FormalizeResponse` 
    
</dd>
</dl>

<dl>
<dd>

**values:** `typing.Dict[str, SolutionBodyValuesValue]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Fso Lens
<details><summary><code>client.fso.lens.<a href="src/axiomatic/fso/lens/client.py">generate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate GDS factory code to create a PIC component
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.fso.lens.generate(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Lean Z3
<details><summary><code>client.lean.z_3.<a href="src/axiomatic/lean/z_3/client.py">execute</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.lean.z_3.execute(
    code="code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Pic Document
<details><summary><code>client.pic.document.<a href="src/axiomatic/pic/document/client.py">summarize</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate GDS factory code to create a PIC component
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.pic.document.summarize(
    markdown="markdown",
    images={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**markdown:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**images:** `typing.Dict[str, str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Pic Circuit
<details><summary><code>client.pic.circuit.<a href="src/axiomatic/pic/circuit/client.py">validate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates a set of statements against a netlist.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic, Computation, Netlist, StatementDictionary

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.pic.circuit.validate(
    netlist=Netlist(),
    statements=StatementDictionary(),
    mapping={
        "key": Computation(
            name="name",
            arguments={"key": 1.1},
        )
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**netlist:** `Netlist` 
    
</dd>
</dl>

<dl>
<dd>

**statements:** `StatementDictionary` 
    
</dd>
</dl>

<dl>
<dd>

**mapping:** `typing.Dict[str, Computation]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pic.circuit.<a href="src/axiomatic/pic/circuit/client.py">formalize</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Formalize a query about a circuit into a dictionary of constraints
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.pic.circuit.formalize(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pic.circuit.<a href="src/axiomatic/pic/circuit/client.py">mapping</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Map variables in the constraints to computations on the netlist.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic, Netlist, StatementDictionary

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.pic.circuit.mapping(
    statements=StatementDictionary(),
    netlist=Netlist(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**statements:** `StatementDictionary` 
    
</dd>
</dl>

<dl>
<dd>

**netlist:** `Netlist` 
    
</dd>
</dl>

<dl>
<dd>

**max_iter:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pic.circuit.<a href="src/axiomatic/pic/circuit/client.py">generate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate GDS factory code to create a circuit
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.pic.circuit.generate(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pic.circuit.<a href="src/axiomatic/pic/circuit/client.py">refine</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refine GDS factory code to create a circuit
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.pic.circuit.refine(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**feedback:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pic.circuit.<a href="src/axiomatic/pic/circuit/client.py">optimize</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optimize a PIC circuit with given cost and constraints
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import (
    Axiomatic,
    Computation,
    Netlist,
    Parameter,
    StatementDictionary,
)

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.pic.circuit.optimize(
    netlist=Netlist(),
    statements=StatementDictionary(),
    mapping={
        "key": Computation(
            name="name",
            arguments={"key": 1.1},
        )
    },
    parameters=[
        Parameter(
            path="path",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**netlist:** `Netlist` 
    
</dd>
</dl>

<dl>
<dd>

**statements:** `StatementDictionary` 
    
</dd>
</dl>

<dl>
<dd>

**mapping:** `typing.Dict[str, Computation]` 
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Sequence[Parameter]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pic.circuit.<a href="src/axiomatic/pic/circuit/client.py">verify</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verifies that the code for a circuit
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.pic.circuit.verify(
    code="code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pic.circuit.<a href="src/axiomatic/pic/circuit/client.py">placementoptimize</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optimizes the placement of a circuit
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.pic.circuit.placementoptimize(
    netlist={"key": "value"},
    method="method",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**netlist:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pic.circuit.<a href="src/axiomatic/pic/circuit/client.py">get_sax_spectrum</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the spectrum of a circuit over various wavelengths and settings
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic, Netlist

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.pic.circuit.get_sax_spectrum(
    netlist=Netlist(),
    settings={"key": "value"},
    wls=[1.1],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**netlist:** `Netlist` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `Settings` 
    
</dd>
</dl>

<dl>
<dd>

**wls:** `typing.Sequence[float]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Pic Component
<details><summary><code>client.pic.component.<a href="src/axiomatic/pic/component/client.py">generate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate GDS factory code to create a PIC component
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.pic.component.generate(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pic.component.<a href="src/axiomatic/pic/component/client.py">refine</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refine GDS factory code to create a circuit
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.pic.component.refine(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**feedback:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Requirements DataFiles
<details><summary><code>client.requirements.data_files.<a href="src/axiomatic/requirements/data_files/client.py">retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides database for user menu later used to compose reqs in AXtract
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from axiomatic import Axiomatic

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.requirements.data_files.retrieve()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

