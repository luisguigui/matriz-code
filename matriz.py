import customtkinter as ctk
import numpy as np
from tkinter import messagebox
import json

# --- CAMADA DE LÓGICA (BUSINESS LOGIC) ---
class MatrixEngine:
    """Encapsula operações matemáticas de alto desempenho usando NumPy."""
    
    @staticmethod
    def parse_matrix(string_data):
        """Converte string de entrada em array NumPy de forma segura."""
        try:
            # Substitui eval() por json.loads para segurança
            data = json.loads(string_data)
            return np.array(data, dtype=float)
        except Exception:
            raise ValueError("Formato inválido. Use: [[1,2],[3,4]]")

    @staticmethod
    def calculate(op_type, matrix_a, matrix_b=None, scalar=None):
        """Centralizador de operações para evitar repetição de código (DRY)."""
        try:
            if op_type == "add": return np.add(matrix_a, matrix_b)
            if op_type == "sub": return np.subtract(matrix_a, matrix_b)
            if op_type == "mul_m": return np.dot(matrix_a, matrix_b)
            if op_type == "mul_s": return np.multiply(matrix_a, scalar)
            if op_type == "trans": return matrix_a.T
            if op_type == "det": return np.linalg.det(matrix_a)
            if op_type == "inv": return np.linalg.inv(matrix_a)
            if op_type == "rank": return np.linalg.matrix_rank(matrix_a)
        except Exception as e:
            raise RuntimeError(f"Erro matemático: {str(e)}")

# --- CAMADA DE INTERFACE (VIEW) ---
class MatrixApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Matrix Pro Desktop - v2.0")
        self.geometry("900x600")
        ctk.set_appearance_mode("dark")
        
        self.matrix_a = None
        self.matrix_b = None

        self.setup_ui()

    def setup_ui(self):
        # Configuração de Grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar (Inputs)
        self.sidebar = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        ctk.CTkLabel(self.sidebar, text="ENTRADA DE DADOS", font=("Roboto", 16, "bold")).pack(pady=20)

        self.entry_a = ctk.CTkEntry(self.sidebar, placeholder_text="Matriz A: [[1,2],[3,4]]", width=250)
        self.entry_a.pack(pady=10, padx=20)

        self.entry_b = ctk.CTkEntry(self.sidebar, placeholder_text="Matriz B: [[5,6],[7,8]]", width=250)
        self.entry_b.pack(pady=10, padx=20)

        self.entry_scalar = ctk.CTkEntry(self.sidebar, placeholder_text="Escalar (ex: 2.5)", width=250)
        self.entry_scalar.pack(pady=10, padx=20)

        # Painel Principal (Operações)
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        ctk.CTkLabel(self.main_frame, text="OPERAÇÕES DISPONÍVEIS", font=("Roboto", 20, "bold")).pack(pady=20)

        # Grid de botões formatado
        btn_grid = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_grid.pack(fill="both", expand=True, padx=20)

        ops = [
            ("Soma (A+B)", "add", "#2ecc71"), ("Subtração (A-B)", "sub", "#e74c3c"),
            ("Multiplicar (A*B)", "mul_m", "#3498db"), ("Escalar (A*s)", "mul_s", "#9b59b6"),
            ("Transposta A", "trans", "#34495e"), ("Determinante A", "det", "#f1c40f"),
            ("Inversa A", "inv", "#d35400"), ("Posto (Rank) A", "rank", "#16a085")
        ]

        for i, (text, cmd, color) in enumerate(ops):
            btn = ctk.CTkButton(btn_grid, text=text, fg_color=color, 
                               command=lambda c=cmd: self.execute_operation(c))
            btn.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="ew")

        # Display de Resultado
        self.result_box = ctk.CTkTextbox(self.main_frame, height=200, font=("Consolas", 14))
        self.result_box.pack(fill="x", padx=20, pady=20)

    def execute_operation(self, op):
        try:
            # Parsing dinâmico
            m_a = MatrixEngine.parse_matrix(self.entry_a.get())
            m_b = None
            scalar = None

            if op in ["add", "sub", "mul_m"]:
                m_b = MatrixEngine.parse_matrix(self.entry_b.get())
            
            if op == "mul_s":
                scalar = float(self.entry_scalar.get())

            # Cálculo
            res = MatrixEngine.calculate(op, m_a, m_b, scalar)
            
            # Formatação de saída
            self.show_result(op, res)

        except Exception as e:
            messagebox.showerror("Erro Operacional", str(e))

    def show_result(self, op, res):
        self.result_box.delete("1.0", "end")
        header = f"--- RESULTADO: {op.upper()} ---\n\n"
        self.result_box.insert("1.0", header + str(res))

if __name__ == "__main__":
    app = MatrixApp()
    app.mainloop()