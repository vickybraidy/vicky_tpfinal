import tkinter as tk
from tkinter import ttk, messagebox
import requests

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vinoteca Virtual")
        self.geometry("600x400")
        
        # Crear pestañas
        self.tab_control = ttk.Notebook(self)
        
        self.tab_bodegas = ttk.Frame(self.tab_control)
        self.tab_cepas = ttk.Frame(self.tab_control)
        self.tab_vinos = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.tab_bodegas, text='Bodegas')
        self.tab_control.add(self.tab_cepas, text='Cepas')
        self.tab_control.add(self.tab_vinos, text='Vinos')
        
        self.tab_control.pack(expand=1, fill='both')
        
        self.create_bodegas_tab()
        self.create_cepas_tab()
        self.create_vinos_tab()
        
    def create_bodegas_tab(self):
        ttk.Label(self.tab_bodegas, text="ID Bodega:").grid(column=0, row=0, padx=10, pady=10)
        self.bodega_id_entry = ttk.Entry(self.tab_bodegas)
        self.bodega_id_entry.grid(column=1, row=0, padx=10, pady=10)
        
        ttk.Button(self.tab_bodegas, text="Buscar Bodega", command=self.buscar_bodega).grid(column=2, row=0, padx=10, pady=10)
        self.bodega_result = tk.Text(self.tab_bodegas, height=10, width=50)
        self.bodega_result.grid(column=0, row=1, columnspan=3, padx=10, pady=10)
        
    def create_cepas_tab(self):
        ttk.Label(self.tab_cepas, text="ID Cepa:").grid(column=0, row=0, padx=10, pady=10)
        self.cepa_id_entry = ttk.Entry(self.tab_cepas)
        self.cepa_id_entry.grid(column=1, row=0, padx=10, pady=10)
        
        ttk.Button(self.tab_cepas, text="Buscar Cepa", command=self.buscar_cepa).grid(column=2, row=0, padx=10, pady=10)
        self.cepa_result = tk.Text(self.tab_cepas, height=10, width=50)
        self.cepa_result.grid(column=0, row=1, columnspan=3, padx=10, pady=10)
        
    def create_vinos_tab(self):
        ttk.Label(self.tab_vinos, text="ID Vino:").grid(column=0, row=0, padx=10, pady=10)
        self.vino_id_entry = ttk.Entry(self.tab_vinos)
        self.vino_id_entry.grid(column=1, row=0, padx=10, pady=10)
        
        ttk.Button(self.tab_vinos, text="Buscar Vino", command=self.buscar_vino).grid(column=2, row=0, padx=10, pady=10)
        self.vino_result = tk.Text(self.tab_vinos, height=10, width=50)
        self.vino_result.grid(column=0, row=1, columnspan=3, padx=10, pady=10)
        
    def buscar_bodega(self):
        bodega_id = self.bodega_id_entry.get()
        response = requests.get(f'http://127.0.0.1:5000/api/bodegas/{bodega_id}')
        if response.status_code == 200:
            self.bodega_result.delete(1.0, tk.END)
            self.bodega_result.insert(tk.END, response.json())
        else:
            messagebox.showerror("Error", "Bodega no encontrada")
            
    def buscar_cepa(self):
        cepa_id = self.cepa_id_entry.get()
        response = requests.get(f'http://127.0.0.1:5000/api/cepas/{cepa_id}')
        if response.status_code == 200:
            self.cepa_result.delete(1.0, tk.END)
            self.cepa_result.insert(tk.END, response.json())
        else:
            messagebox.showerror("Error", "Cepa no encontrada")
            
    def buscar_vino(self):
        vino_id = self.vino_id_entry.get()
        response = requests.get(f'http://127.0.0.1:5000/api/vinos/{vino_id}')
        if response.status_code == 200:
            self.vino_result.delete(1.0, tk.END)
            self.vino_result.insert(tk.END, response.json())
        else:
            673
            messagebox.showerror("Error", "Vino no encontrado")
            
if __name__ == "__main__":
    app = App()
    app.mainloop()
