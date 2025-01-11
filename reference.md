# Reference
<details><summary><code>client.<a href="src/axiomatic/client.py">trigger_error_sentry_debug_get</a>()</code></summary>
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

<details><summary><code>client.<a href="src/axiomatic/client.py">health_check_health_check_get</a>()</code></summary>
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
from axiomatic import Axiomatic, RequirementBody

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.requirements.check(
    request=[
        RequirementBody(
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

**request:** `typing.Sequence[RequirementBody]` 
    
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

## pic
<details><summary><code>client.pic.<a href="src/axiomatic/pic/client.py">find_mappings</a>(...)</code></summary>
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
from axiomatic import Axiomatic, Netlist, PicComponent, Statement

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.pic.find_mappings(
    statements=[
        Statement(
            id="id",
            statement="statement",
        )
    ],
    netlist=Netlist(
        name="name",
        instances={
            "key": PicComponent(
                component="component",
            )
        },
        connections={"key": "value"},
        ports={"key": "value"},
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

**statements:** `typing.Sequence[Statement]` 
    
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
<details><summary><code>client.document.<a href="src/axiomatic/document/client.py">extract_text</a>(...)</code></summary>
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
client.document.extract_text()

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

**method:** `typing.Optional[str]` — Method to use for text-only extraction.It uses a very simple pdf parser. 
    
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

Executes code in a secure environment
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

## Pic Circuit
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
from axiomatic import Axiomatic, Mapping, Netlist, PicComponent, Statement

client = Axiomatic(
    api_key="YOUR_API_KEY",
)
client.pic.circuit.optimize(
    netlist=Netlist(
        name="name",
        instances={
            "key": PicComponent(
                component="component",
            )
        },
        connections={"key": "value"},
        ports={"key": "value"},
    ),
    statements=[
        Statement(
            id="id",
            statement="statement",
        )
    ],
    mappings=[
        Mapping(
            statement_id="statement_id",
            expression_idx=1,
            variable="variable",
            computation_name="computation_name",
            computation_arguments={"key": 1.1},
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

**statements:** `typing.Sequence[Statement]` 
    
</dd>
</dl>

<dl>
<dd>

**mappings:** `typing.Sequence[Mapping]` 
    
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

