from controlador import ControladorRefugio
from ui import VentanaPrincipal

def main():
    """Función principal"""
    print("=" * 60)
    print(" " * 10 + "🐕 REFUGIO CANINO - SISTEMA DE GESTIÓN")
    print("=" * 60)
    print("\nIniciando aplicación...")
    
    # Crear controlador
    controlador = ControladorRefugio()
    
    # Crear y ejecutar interfaz gráfica
    app = VentanaPrincipal(controlador)
    
    print("✅ Aplicación iniciada correctamente")
    print("👉 Por favor, use la ventana gráfica para interactuar con el sistema\n")
    
    # Iniciar el loop de la interfaz
    app.mainloop()
    
    print("\n👋 Aplicación cerrada")
    print("=" * 60)

if __name__ == "__main__":
    main()
