# 🔢 MATRIX PRO DESKTOP — Software de Álgebra Linear

> Um software de alta performance para operações de álgebra linear desenvolvido em Python. Integra a biblioteca NumPy para cálculos complexos, CustomTkinter para uma UI moderna e apresenta processamento seguro de dados via JSON com tratamento robusto de exceções.

[![Python](https://img.shields.io/badge/python-3.7+-3776ab.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Latest-blue.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![NumPy](https://img.shields.io/badge/NumPy-1.20+-red.svg)](https://numpy.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Production-brightgreen.svg)]()
[![Academic](https://img.shields.io/badge/Academic-Mathematics-success.svg)]()

<div align="center">

**[🚀 Instalação](#-instalação-e-execução) • [📖 Documentação](#-arquitetura-e-estrutura) • [🔬 Operações](#-operações-de-álgebra-linear) • [📊 Exemplos](#-exemplos-práticos) • [🧮 Matemática](#-conceitos-matemáticos)**

</div>

---

## 🌟 Visão Geral

**MATRIX PRO DESKTOP** é um software educacional e profissional que simplifica operações complexas de álgebra linear. Combinando a velocidade de **NumPy** com a interface intuitiva de **CustomTkinter**, oferece acesso fácil a cálculos que normalmente requerem linguagens de programação avançadas ou MATLAB.

### ✨ Destaques Principais

- 🚀 **Performance Alto**: Powered by NumPy (C backend)
- 🔢 **8 Operações Principais**: Soma, subtração, multiplicação, escalar, transposta, determinante, inversa, rank
- 🎨 **Interface Dark Mode**: Design moderno e profissional
- 📐 **Suporte Completo a Matrizes**: Qualquer dimensão (m×n)
- 🔒 **Entrada Segura**: JSON parsing ao invés de eval()
- 📊 **Visualização Clara**: Resultado em formato monoespaciado
- ⚠️ **Tratamento Robusto**: Exceções com mensagens claras
- 📝 **Arquitetura MVC**: Separação clara Model-View-Controller
- 🧮 **Operações Avançadas**: Determinante, inversa, rank
- ✅ **Validação de Entrada**: Verifica dimensionalidade

---

## 🔬 Operações de Álgebra Linear

### 📟 Operações Básicas

#### 1️⃣ **Soma (A + B)**

Adiciona elemento por elemento:

```
A = [1  2]     B = [5  6]     A+B = [6   8]
    [3  4]         [7  8]          [10 12]

Fórmula:
(A + B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ
```

**Entrada**:
```
Matriz A: [[1,2],[3,4]]
Matriz B: [[5,6],[7,8]]
Clique: Soma (A+B)
```

**Resultado**:
```
[[ 6.  8.]
 [10. 12.]]
```

**Requisito**: Matrizes A e B devem ter mesma dimensão (m×n)

---

#### 2️⃣ **Subtração (A - B)**

Subtrai elemento por elemento:

```
A = [10  12]     B = [5  6]     A-B = [5   6]
    [20  24]         [7  8]          [13 16]

Fórmula:
(A - B)ᵢⱼ = Aᵢⱼ - Bᵢⱼ
```

**Requisito**: Mesma dimensão

---

#### 3️⃣ **Multiplicação de Matrizes (A × B)**

Operação mais complexa - produto escalar entre linhas e colunas:

```
A (2×2)     B (2×2)     A×B (2×2)

[1 2]       [5 6]       [1×5+2×7  1×6+2×8]
[3 4]   ×   [7 8]    =  [3×5+4×7  3��6+4×8]

                      = [19  22]
                        [43  50]

Fórmula:
(A × B)ᵢⱼ = Σₖ Aᵢₖ × Bₖⱼ
```

**Requisito**: Colunas de A = Linhas de B (A: m×n, B: n×p → resultado: m×p)

**Exemplos**:
```
[2×3] × [3×2] = [2×2] ✓
[2×2] × [3×2] = Erro ✗ (incompatível)
```

---

#### 4️⃣ **Multiplicação por Escalar (A × s)**

Multiplica cada elemento por um número:

```
A = [1 2]     s = 3     A×s = [3  6]
    [3 4]                     [9 12]

Fórmula:
(A × s)ᵢⱼ = Aᵢⱼ × s
```

**Sem requisitos**: Funciona com qualquer matriz e escalar

---

### 📐 Operações Avançadas

#### 5️⃣ **Transposta (Aᵀ)**

Troca linhas por colunas:

```
A = [1 2 3]     Aᵀ = [1 4]
    [4 5 6]          [2 5]
                     [3 6]

A é 2×3 → Aᵀ é 3×2

Fórmula:
(Aᵀ)ᵢⱼ = Aⱼᵢ
```

**Visualização**:
```
Antes (2×3):        Depois (3×2):
col1 col2 col3      col1 col2
  1    2    3   →     1    4    (linha 1)
  4    5    6         2    5    (linha 2)
                      3    6    (linha 3)
```

---

#### 6️⃣ **Determinante (det A)**

Número único que descreve propriedades da matriz:

```
Para matriz 2×2:
A = [a b]
    [c d]
det(A) = ad - bc

Exemplo:
A = [1 2]
    [3 4]
det(A) = 1×4 - 2×3 = 4 - 6 = -2
```

**Significado**:
- det = 0: Matriz singular (não invertível)
- det ≠ 0: Matriz regular (invertível)
- |det| = escala de transformação linear

**Para matriz 3×3**:
```
A = [1 2 3]
    [4 5 6]
    [7 8 9]

det(A) = 1×(5×9 - 6×8) - 2×(4×9 - 6×7) + 3×(4×8 - 5×7)
       = 1×(-3) - 2×(-6) + 3×(-3)
       = -3 + 12 - 9
       = 0  (matriz singular)
```

---

#### 7️⃣ **Inversa (A⁻¹)**

Matriz que, multiplicada por A, dá identidade:

```
A × A⁻¹ = I (identidade)

Exemplo:
A = [1 2]
    [3 4]

A⁻¹ = [-2    1  ]
      [ 1.5 -0.5]

Verificação:
[1 2] × [-2   1  ]  = [1 0]
[3 4]   [ 1.5 -0.5]   [0 1] ✓ Identidade
```

**Requisitos**:
- A DEVE ser quadrada (m×m)
- det(A) ≠ 0 (não singular)

**Erro comum**:
```
A = [1 0]
    [2 0]
det(A) = 0 → ERRO! Não invertível
```

---

#### 8️⃣ **Posto/Rank (rank A)**

Número de linhas/colunas linearmente independentes:

```
A = [1 2 3]
    [4 5 6]
    [7 8 9]

rank(A) = 2  (3ª linha é combinação das outras)

Propriedades:
- rank(A) ≤ min(m, n)  onde A é m×n
- rank(A) = m = n → A é não-singular
- rank(A) < n → A é singular
```

**Aplicações**:
- Determinar se sistema tem solução única
- Verificar independência linear
- Análise de espaço vetorial

---

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia | Versão | Propósito |
|-----------|-----------|--------|----------|
| **Linguagem** | Python | 3.7+ | Lógica e estrutura |
| **GUI** | CustomTkinter | Latest | Interface Dark Mode |
| **Computação** | NumPy | 1.20+ | Operações matriciais |
| **Segurança** | JSON | Nativo | Parse seguro |
| **Persistência** | JSON | Nativo | Salvar/carregar |

### Por que NumPy?

- ✅ **Performance**: Implementado em C (10-100× mais rápido)
- ✅ **Confiabilidade**: Padrão ouro em computação científica
- ✅ **Suporte**: Comunidade global, documentação completa
- ✅ **Integração**: Funciona com SciPy, Pandas, Matplotlib

### Por que JSON ao invés de eval()?

```python
# ❌ INSEGURO:
eval("[[1,2],[3,4]]")  # Poderia ser __import__('os').system(...)

# ✅ SEGURO:
json.loads("[[1,2],[3,4]]")  # Apenas dados, sem execução
```

---

## 🏗️ Arquitetura e Estrutura

### 📊 Padrão MVC

```
┌──────────────────┐
│   MatrixApp      │  ← VIEW (Interface)
│  (CustomTkinter) │
└────────┬─────────┘
         │
    ┌────▼────────────┐
    │ execute_         │
    │ operation()      │  ← CONTROLLER (Orquestração)
    └────┬────────────┘
         │
    ┌────▼──────────────────┐
    │ MatrixEngine.         │  ← MODEL (Lógica)
    │ calculate()           │
    └────┬──────────────────┘
         │
    ┌────▼──────────────────┐
    │ NumPy                 │
    │ (np.add, np.dot, ...) │  ← FRAMEWORK (Computação)
    └───────────────────────┘
```

### 🧩 Estrutura do Código

```
matriz.py
│
├── 📦 CLASSE: MatrixEngine (Model)
│   ├── @staticmethod parse_matrix()
│   │   └── JSON → NumPy Array
│   │
│   └── @staticmethod calculate()
│       ├── Operação: add, sub, mul_m, mul_s
│       ├── Operação: trans, det, inv, rank
│       └── NumPy backend
│
└── 🎮 CLASSE: MatrixApp (CustomTkinter)
    ├── INICIALIZAÇÃO
    │   ├── __init__()
    │   └── setup_ui()
    │
    ├── SIDEBAR (Entrada)
    │   ├── Entry: Matriz A
    │   ├── Entry: Matriz B
    │   └── Entry: Escalar
    │
    ├── GRID DE OPERAÇÕES
    │   ├── Botões 2×4
    │   ├── Cores por tipo
    │   └── Commands
    │
    ├── RESULTADO
    │   └── Textbox (Consolas)
    │
    └── MÉTODOS
        ├── execute_operation()
        ├── show_result()
        └── Tratamento de erros
```

---

## 📚 Documentação das Classes

### 1️⃣ `MatrixEngine` — Camada de Lógica

**Responsabilidade**: Operações matemáticas com NumPy

```python
class MatrixEngine:
    """Encapsula operações matemáticas de alto desempenho."""
```

---

#### **Método: `parse_matrix(string_data)` - Static**

```python
@staticmethod
def parse_matrix(string_data):
    """Converte string de entrada em array NumPy de forma segura."""
    try:
        # Usa JSON.loads (seguro) ao invés de eval()
        data = json.loads(string_data)
        return np.array(data, dtype=float)
    except Exception:
        raise ValueError("Formato inválido. Use: [[1,2],[3,4]]")
```

**O que faz**:
1. Recebe string: `"[[1,2],[3,4]]"`
2. Parse JSON: `[[1, 2], [3, 4]]`
3. Converte para NumPy: `np.array([[1., 2.], [3., 4.]])`
4. Retorna array

**Exemplo**:
```python
mat = MatrixEngine.parse_matrix("[[1,2],[3,4]]")
# Resultado: array([[1., 2.],
#                   [3., 4.]])
```

**Validações**:
- ✅ `[[1,2],[3,4]]` - OK
- ❌ `"1,2,3,4"` - Erro (não é matriz 2D)
- ❌ `[[1,2],3]` - Erro (inconsistente)

---

#### **Método: `calculate(op_type, matrix_a, matrix_b, scalar)` - Static**

```python
@staticmethod
def calculate(op_type, matrix_a, matrix_b=None, scalar=None):
    """Centralizador de operações (DRY - Don't Repeat Yourself)."""
    try:
        # Operações binárias (2 matrizes)
        if op_type == "add":
            return np.add(matrix_a, matrix_b)
        if op_type == "sub":
            return np.subtract(matrix_a, matrix_b)
        if op_type == "mul_m":
            return np.dot(matrix_a, matrix_b)  # Multiplicação matricial
        
        # Operação com escalar
        if op_type == "mul_s":
            return np.multiply(matrix_a, scalar)
        
        # Operações unárias (1 matriz)
        if op_type == "trans":
            return matrix_a.T  # Transposta
        if op_type == "det":
            return np.linalg.det(matrix_a)  # Determinante
        if op_type == "inv":
            return np.linalg.inv(matrix_a)  # Inversa
        if op_type == "rank":
            return np.linalg.matrix_rank(matrix_a)  # Rank
    
    except Exception as e:
        raise RuntimeError(f"Erro matemático: {str(e)}")
```

**Operações**:

| Op Type | Função | NumPy | Requer |
|---------|--------|-------|---------|
| `add` | A + B | `np.add()` | A, B (mesma dim) |
| `sub` | A - B | `np.subtract()` | A, B (mesma dim) |
| `mul_m` | A × B | `np.dot()` | A, B (compatível) |
| `mul_s` | A × s | `np.multiply()` | A, s (escalar) |
| `trans` | Aᵀ | `.T` | A |
| `det` | det(A) | `np.linalg.det()` | A (quadrada) |
| `inv` | A⁻¹ | `np.linalg.inv()` | A (invertível) |
| `rank` | rank(A) | `np.linalg.matrix_rank()` | A |

---

### 2️⃣ `MatrixApp` — Interface (CustomTkinter)

**Responsabilidade**: Gerenciar UI e coordenar com MatrixEngine

```python
class MatrixApp(ctk.CTk):
    """Interface gráfica para operações matriciais."""
```

---

#### **Método: `setup_ui()`**

```python
def setup_ui(self):
    # Configuração de Grid
    self.grid_columnconfigure(1, weight=1)
    self.grid_rowconfigure(0, weight=1)
    
    # SIDEBAR - Entradas
    self.sidebar = ctk.CTkFrame(self, width=300, corner_radius=0)
    self.sidebar.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    
    ctk.CTkLabel(self.sidebar, 
                text="ENTRADA DE DADOS", 
                font=("Roboto", 16, "bold")).pack(pady=20)
    
    # Matriz A
    self.entry_a = ctk.CTkEntry(
        self.sidebar,
        placeholder_text="Matriz A: [[1,2],[3,4]]",
        width=250
    )
    self.entry_a.pack(pady=10, padx=20)
    
    # Matriz B
    self.entry_b = ctk.CTkEntry(
        self.sidebar,
        placeholder_text="Matriz B: [[5,6],[7,8]]",
        width=250
    )
    self.entry_b.pack(pady=10, padx=20)
    
    # Escalar
    self.entry_scalar = ctk.CTkEntry(
        self.sidebar,
        placeholder_text="Escalar (ex: 2.5)",
        width=250
    )
    self.entry_scalar.pack(pady=10, padx=20)
    
    # PAINEL PRINCIPAL - Operações
    self.main_frame = ctk.CTkFrame(self)
    self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
    
    ctk.CTkLabel(self.main_frame,
                text="OPERAÇÕES DISPONÍVEIS",
                font=("Roboto", 20, "bold")).pack(pady=20)
    
    # Grid de botões 2×4
    btn_grid = ctk.CTkFrame(self.main_frame, fg_color="transparent")
    btn_grid.pack(fill="both", expand=True, padx=20)
    
    ops = [
        ("Soma (A+B)", "add", "#2ecc71"),
        ("Subtração (A-B)", "sub", "#e74c3c"),
        ("Multiplicar (A*B)", "mul_m", "#3498db"),
        ("Escalar (A*s)", "mul_s", "#9b59b6"),
        ("Transposta A", "trans", "#34495e"),
        ("Determinante A", "det", "#f1c40f"),
        ("Inversa A", "inv", "#d35400"),
        ("Posto (Rank) A", "rank", "#16a085")
    ]
    
    for i, (text, cmd, color) in enumerate(ops):
        btn = ctk.CTkButton(
            btn_grid,
            text=text,
            fg_color=color,
            command=lambda c=cmd: self.execute_operation(c)
        )
        btn.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="ew")
    
    # Display de Resultado
    self.result_box = ctk.CTkTextbox(
        self.main_frame,
        height=200,
        font=("Consolas", 14)
    )
    self.result_box.pack(fill="x", padx=20, pady=20)
```

---

#### **Método: `execute_operation(op)`**

```python
def execute_operation(self, op):
    """Executa operação matricial com tratamento de erros."""
    try:
        # 1. Parse da matriz A (sempre necessária)
        m_a = MatrixEngine.parse_matrix(self.entry_a.get())
        m_b = None
        scalar = None
        
        # 2. Parse condicional baseado na operação
        if op in ["add", "sub", "mul_m"]:
            m_b = MatrixEngine.parse_matrix(self.entry_b.get())
        
        if op == "mul_s":
            scalar = float(self.entry_scalar.get())
        
        # 3. Executar cálculo
        res = MatrixEngine.calculate(op, m_a, m_b, scalar)
        
        # 4. Exibir resultado
        self.show_result(op, res)
    
    except Exception as e:
        messagebox.showerror("Erro Operacional", str(e))
```

**Fluxo**:
```
Clique botão → execute_operation() → parse → calculate() → show_result()
```

---

#### **Método: `show_result(op, res)`**

```python
def show_result(self, op, res):
    """Exibe resultado formatado no textbox."""
    self.result_box.delete("1.0", "end")
    header = f"--- RESULTADO: {op.upper()} ---\n\n"
    self.result_box.insert("1.0", header + str(res))
```

**Exemplo**:
```
--- RESULTADO: ADD ---

[[ 6.  8.]
 [10. 12.]]
```

---

## 📊 Exemplos Práticos

### Exemplo 1: Soma Básica

```
ENTRADA:
Matriz A: [[1,2],[3,4]]
Matriz B: [[5,6],[7,8]]
Clique: Soma (A+B)

PROCESSAMENTO:
1. parse_matrix("[[1,2],[3,4]]") → array([[1., 2.], [3., 4.]])
2. parse_matrix("[[5,6],[7,8]]") → array([[5., 6.], [7., 8.]])
3. np.add(...) → array([[6., 8.], [10., 12.]])

RESULTADO:
--- RESULTADO: ADD ---

[[ 6.  8.]
 [10. 12.]]
```

---

### Exemplo 2: Multiplicação Matricial

```
ENTRADA:
Matriz A: [[1,2],[3,4],[5,6]]  (3×2)
Matriz B: [[7,8,9],[10,11,12]]  (2×3)
Clique: Multiplicar (A*B)

PROCESSAMENTO:
A (3×2) × B (2×3) = resultado (3×3) ✓

[1×7+2×10  1×8+2×11  1×9+2×12]     [27  30  33]
[3×7+4×10  3×8+4×11  3×9+4×12]  =  [61  70  79]
[5×7+6×10  5×8+6×11  5×9+6×12]     [95 110 125]

RESULTADO:
--- RESULTADO: MUL_M ---

[[ 27.  30.  33.]
 [ 61.  70.  79.]
 [ 95. 110. 125.]]
```

---

### Exemplo 3: Determinante

```
ENTRADA:
Matriz A: [[1,2],[3,4]]  (2×2)
Clique: Determinante A

PROCESSAMENTO:
det([1 2]) = 1×4 - 2×3 = 4 - 6 = -2
   [3 4]

RESULTADO:
--- RESULTADO: DET ---

-2.0
```

---

### Exemplo 4: Inversa

```
ENTRADA:
Matriz A: [[1,2],[3,4]]
Clique: Inversa A

PROCESSAMENTO:
det(A) = -2 (não zero, pode inverter)

A⁻¹ = 1/det(A) × [d  -b]
                  [-c  a]

    = 1/(-2) × [4  -2]   = [-2.0   1.0]
               [-3  1]     [ 1.5  -0.5]

RESULTADO:
--- RESULTADO: INV ---

[[-2.   1. ]
 [ 1.5 -0.5]]

VERIFICAÇÃO:
[[1,2],[3,4]] × [[-2,1],[1.5,-0.5]] = [[1,0],[0,1]] ✓
```

---

### Exemplo 5: Transposta

```
ENTRADA:
Matriz A: [[1,2,3],[4,5,6]]  (2×3)
Clique: Transposta A

PROCESSAMENTO:
Aᵀ = [1 4]  (3×2)
     [2 5]
     [3 6]

RESULTADO:
--- RESULTADO: TRANS ---

[[1. 4.]
 [2. 5.]
 [3. 6.]]
```

---

## 🔧 Formatos de Entrada

### ✅ Aceitos

```
[[1,2],[3,4]]           (2×2)
[[1.5,2.3],[3.7,4.2]]   (Com decimais)
[[1],[2],[3]]           (3×1 - coluna)
[[1,2,3,4,5]]           (1×5 - linha)
[[0,0],[0,0]]           (Zeros)
[[-1,2],[-3,4]]         (Negativos)
```

### ❌ Rejeitos

```
"1,2,3,4"               (Não é 2D)
"[[1,2],3]"             (Inconsistente)
"[[1,2],[3,4"           (Mal formado)
"matrix A"              (Texto puro)
"[[1,a],[3,4]]"         (Contém letra)
```

---

## 🎨 Interface

### Layout

```
┌──────────────────┬────────────────────────────────┐
│                  │                                │
│  ENTRADA         │     OPERAÇÕES DISPONÍVEIS     │
│  DE DADOS        │                                │
│                  │  ┌──────────┬──────────┐      │
│  [Matriz A]      │  │  SOMA    │  SUBTRACT│      │
│  [Matriz B]      │  ├──────────┼──────────┤      │
│  [Escalar]       │  │  MULT    │ ESCALAR  │      │
│                  │  ├──────────┼──────────┤      │
│                  │  │  TRANS   │   DET    │      │
│                  │  ├──────────┼──────────┤      │
│                  │  │   INV    │   RANK   │      │
│                  │  └──────────┴──────────┘      │
│                  │                                │
│                  │  ┌─────────────────────────┐  │
│                  │  │    RESULTADO            │  │
│                  │  │  [[ 6.  8.]             │  │
│                  │  │   [10. 12.]]            │  │
│                  │  └─────────────────────────┘  │
│                  │                                │
└──────────────────┴────────────────────────────────┘
```

### Cores

```
🟢 Verde (#2ecc71)      - Soma (aditivo)
🔴 Vermelho (#e74c3c)   - Subtração (negativo)
🔵 Azul (#3498db)       - Multiplicação
🟣 Roxo (#9b59b6)       - Escalar
⚫ Cinza (#34495e)       - Transposta
🟡 Amarelo (#f1c40f)    - Determinante
🟠 Laranja (#d35400)    - Inversa
🟦 Teal (#16a085)       - Rank
```

---

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia | Versão | Propósito |
|-----------|-----------|--------|----------|
| **Linguagem** | Python | 3.7+ | Lógica e estrutura |
| **GUI** | CustomTkinter | Latest | Interface Dark Mode |
| **Computação** | NumPy | 1.20+ | Operações matriciais |
| **Validação** | JSON | Nativo | Parse seguro |

---

## 🚀 Possíveis Melhorias Futuras

- [ ] **Resolução de Sistemas**: Ax = b
- [ ] **Autovalores e Autovetores**: Eigenvalues/Eigenvectors
- [ ] **Decomposições**: QR, SVD, Cholesky
- [ ] **Plotagem**: Visualizar matrizes em gráficos
- [ ] **Operações em Lote**: Salvar/carregar múltiplas matrizes
- [ ] **Historico**: Guardar operações anteriores
- [ ] **Exportação**: Salvar resultado em CSV
- [ ] **Matrizes Especiais**: Identidade, zeros, aleatória
- [ ] **Modo Científico**: Notação científica
- [ ] **Temas**: Light/Dark customizável

---

## 📋 Instalação e Execução

### ✅ Pré-requisitos

- Python 3.7+
- pip

### 🔧 Passos

1. **Clone o repositório**:
```bash
git clone https://github.com/luisguigui/matriz-code.git
cd matriz-code
```

2. **Crie ambiente virtual**:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Instale dependências**:
```bash
pip install -r requirements.txt
```

4. **Execute**:
```bash
python matriz.py
```

5. **Interface deve aparecer**:
   - Sidebar esquerda com campos de entrada
   - Grid de operações à direita
   - Comece inserindo matrizes!

---

## 📄 requirements.txt

```
customtkinter>=5.0.0
numpy>=1.20.0
```

---

## 🐛 Troubleshooting

### ❌ Problema: "ModuleNotFoundError: numpy"
**Solução**: `pip install numpy`

### ❌ Problema: "Formato inválido"
**Causa**: Entrada não segue JSON  
**Solução**: Use `[[1,2],[3,4]]` exatamente

### ❌ Problema: "Matrizes incompatíveis"
**Causa**: Dimensões não permitem a operação  
**Solução**: Verifique as regras (A+B precisa mesma dim, etc)

### ❌ Problema: "Matriz singular"
**Causa**: Determinante = 0, não pode inverter  
**Solução**: Escolha outra matriz

### ❌ Problema: Resultado vazio
**Causa**: Não clicou em nenhum botão após entrar dados  
**Solução**: Clique em uma operação

---

## ⚙️ Configuração Avançada

### Modificar Cores

```python
ops = [
    ("Soma (A+B)", "add", "#00ff00"),  # Seu verde
    ("Subtração (A-B)", "sub", "#ff0000"),  # Seu vermelho
    # ...
]
```

### Modificar Tamanho da Janela

```python
self.geometry("900x600")  # Mude para seus valores
```

### Adicionar Fonte Customizada

```python
ctk.CTkLabel(self.main_frame,
            text="OPERAÇÕES",
            font=("Arial", 24, "bold"))
```

### Adicionar Nova Operação

```python
# 1. Adicionar ao ops list:
("Minha Op", "my_op", "#ffffff")

# 2. Adicionar ao MatrixEngine.calculate():
if op_type == "my_op":
    return minha_funcao(matrix_a)

# 3. Pronto! Botão aparecerá automaticamente
```

---

## 💡 Dicas de Uso

1. **Copie de Excel**: Copie uma matriz e ajuste para JSON
2. **Teste primeiro**: Use matrizes pequenas (2×2) para entender
3. **Múltiplas operações**: Reutilize matrizes entre operações
4. **Verifique dimensões**: Sempre saiba m×n de cada matriz
5. **Use números redondos**: 1, 2, 3... para testes

---

## 🔬 Conceitos Matemáticos

### Matriz

Arranjo retangular de números:

```
A = [1 2 3]  ← linha
    [4 5 6]
    ↑
    coluna

Dimensão: 2×3 (2 linhas, 3 colunas)
Aᵢⱼ: elemento na linha i, coluna j
A₁₂ = 2 (linha 1, coluna 2)
```

### Operações Lineares

Propriedades importantes:

```
Associatividade: (A+B)+C = A+(B+C)
Comutatividade:  A+B = B+A (soma)
                 A×B ≠ B×A (produto - NÃO comutativo!)
Elemento neutro: A + 0 = A
                 A × I = A
```

### Definições

```
Matriz Quadrada: m = n (ex: 3×3)
Matriz Identidade: I = [[1,0,0],[0,1,0],[0,0,1]]
Matriz Singular: det(A) = 0 (não invertível)
Matriz Invertível: det(A) ≠ 0 (A⁻¹ existe)
```

---

## ✒️ Autor

**Luis Guilherme G.B.**

- 🐙 GitHub: [@luisguigui](https://github.com/luisguigui)
- 💼 Portfólio: Desenvolvedor Python Full-Stack
- 📧 Contato: Abra uma issue no repositório

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Use livremente em projetos acadêmicos e comerciais!

---

## 🌟 Se gostou, considere dar uma ⭐!

```
   🔢 ÁLGEBRA LINEAR PARA TODOS!

   Sem precisar compilar MATLAB
   ou aprender C++ BLAS

   ⭐ Python + NumPy = Poder ⭐
```

---

**Última atualização**: 2026-04-20  
**Versão**: 2.0 — Academic Edition  
**Status**: ✅ Production Ready  
**Foco**: Precisão, Educação, Performance
```

---
