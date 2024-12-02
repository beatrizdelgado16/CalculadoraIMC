import tkinter as tk
from tkinter import messagebox
from src.imc_calculator import calculate_imc


def create_interface():
    def on_calculate():
        try:
            weight = float(weight_entry.get())
            height = float(height_entry.get()) / 100  # Converte de cm para metros
            imc = calculate_imc(weight, height)
            result_label.config(text=f"Seu IMC é: {imc:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Janela principal
    window = tk.Tk()
    window.title("Calculadora de IMC")

    # Layout
    tk.Label(window, text="Peso (kg):").grid(row=0, column=0, padx=10, pady=10)
    weight_entry = tk.Entry(window)
    weight_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(window, text="Altura (cm):").grid(row=1, column=0, padx=10, pady=10)
    height_entry = tk.Entry(window)
    height_entry.grid(row=1, column=1, padx=10, pady=10)

    calculate_button = tk.Button(window, text="Calcular IMC", command=on_calculate)
    calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    result_label = tk.Label(window, text="Seu IMC é: 0.00")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Inicia a interface
    window.mainloop()
