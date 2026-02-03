
import customtkinter as ctk
from datetime import datetime

class AppRefugio:
    def __init__(self):
        # Configurar apariencia
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # Crear ventana principal
        self.root = ctk.CTk()
        self.root.title(" Refugio de Perritos 🐕 - Planificador ")
        self.root.geometry("1200x800")
        
        # Crear layout
        self.setup_ui()
        
    def setup_ui(self):
        """Configura la interfaz de usuario."""
        # Grid layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        
        # ===== SIDEBAR =====
        self.sidebar = ctk.CTkFrame(self.root, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        # Logo/título
        ctk.CTkLabel(
            self.sidebar,
            text="🐕 Refugio",
            font=ctk.CTkFont(size=24, weight="bold")
        ).pack(pady=(20, 10))
        
        ctk.CTkLabel(
            self.sidebar,
            text="Planificador",
            font=ctk.CTkFont(size=14)
        ).pack(pady=(0, 30))
        
        # Botones de navegación
        botones_nav = [
            ("📅 Eventos", self.mostrar_eventos),
            ("➕ Nuevo", self.mostrar_nuevo),
            ("📊 Recursos", self.mostrar_recursos),
            ("🔍 Buscar", self.mostrar_buscar)
        ]
        
        for texto, comando in botones_nav:
            btn = ctk.CTkButton(
                self.sidebar,
                text=texto,
                command=comando,
                height=40,
                font=ctk.CTkFont(size=14)
            )
            btn.pack(pady=5, padx=20, fill="x")
        
        # Separador
        ctk.CTkFrame(self.sidebar, height=2).pack(pady=20, padx=20, fill="x")
        
        # Botones inferiores
        ctk.CTkButton(
            self.sidebar,
            text="💾 Guardar",
            command=self.guardar,
            fg_color="#2be378",
            height=40
        ).pack(pady=5, padx=20, fill="x")
        
        ctk.CTkButton(
            self.sidebar,
            text="🚪 Salir",
            command=self.salir,
            fg_color="#e74c3c",
            height=40
        ).pack(pady=5, padx=20, fill="x")
    
        # ===== CONTENIDO PRINCIPAL =====
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=10)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        # Mostrar dashboard por defecto
        self.mostrar_dashboard()
    
    def mostrar_dashboard(self):
        """Muestra el dashboard principal."""
        self.limpiar_frame()
        
        # Título
        ctk.CTkLabel(
            self.main_frame,
            text="🏠 Dashboard",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(pady=(30, 10))
        
        ctk.CTkLabel(
            self.main_frame,
            text=f"Bienvenido al sistema - {datetime.now().strftime('%d/%m/%Y')}",
            font=ctk.CTkFont(size=16)
        ).pack(pady=(0, 30))
        
        # Tarjetas de resumen
        frame_cards = ctk.CTkFrame(self.main_frame)
        frame_cards.pack(pady=20, padx=20, fill="both", expand=True)
        
        cards = [
            ("📅 Eventos Hoy", "5", "#3498db"),
            ("🐕 ", "12", "#2ecc71"),
            ("⚠️ Pendientes", "3", "#e74c3c"),
            ("✅ Completados", "", "#f39c12")
        ]
        
        for i, (titulo, valor, color) in enumerate(cards):
            card = ctk.CTkFrame(
                frame_cards,
                border_width=2,
                border_color=color,
                corner_radius=15
            )
            card.grid(row=i//2, column=i%2, padx=15, pady=15, sticky="nsew")
            
            ctk.CTkLabel(
                card,
                text=titulo,
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(pady=(20, 5))
            
            ctk.CTkLabel(
                card,
                text=valor,
                font=ctk.CTkFont(size=32, weight="bold")
            ).pack(pady=(5, 20))
            
            # Configurar expansión
            frame_cards.grid_columnconfigure(i%2, weight=1)
            frame_cards.grid_rowconfigure(i//2, weight=1)
    
    def mostrar_eventos(self):
        """Muestra la lista de eventos."""
        self.limpiar_frame()
        
        # Título y botón
        frame_titulo = ctk.CTkFrame(self.main_frame)
        frame_titulo.pack(fill="x", padx=20, pady=20)
        
        ctk.CTkLabel(
            frame_titulo,
            text="📅 Eventos Programados",
            font=ctk.CTkFont(size=24, weight="bold")
        ).pack(side="left", padx=10)
        
        ctk.CTkButton(
            frame_titulo,
            text="🔄 Actualizar",
            width=100
        ).pack(side="right", padx=10)
        
        # Tabla de eventos
        eventos = []
        
        for evento in eventos:
            frame_evento = ctk.CTkFrame(
                self.main_frame,
                height=60,
                corner_radius=10
            )
            frame_evento.pack(fill="x", padx=40, pady=5)
            
            for i, valor in enumerate(evento):
                ctk.CTkLabel(
                    frame_evento,
                    text=valor,
                    font=ctk.CTkFont(size=14)
                ).place(relx=0.05 + i*0.23, rely=0.5, anchor="w")
    
    def mostrar_nuevo(self):
        """Muestra formulario para nuevo evento."""
        self.limpiar_frame()
        
        ctk.CTkLabel(
            self.main_frame,
            text="➕ Nuevo Evento",
            font=ctk.CTkFont(size=24, weight="bold")
        ).pack(pady=30)
        
        # Formulario
        campos = [
            ("Nombre del Evento:", ctk.CTkEntry(self.main_frame, width=300)),
            ("Fecha:", ctk.CTkEntry(self.main_frame, width=150)),
            ("Hora Inicio:", ctk.CTkEntry(self.main_frame, width=100)),
            ("Hora Fin:", ctk.CTkEntry(self.main_frame, width=100))
        ]
        
        for label, entry in campos:
            frame = ctk.CTkFrame(self.main_frame, height=40)
            frame.pack(fill="x", padx=80, pady=10)
            
            ctk.CTkLabel(frame, text=label, width=120).pack(side="left", padx=10)
            entry.pack(side="left", padx=10)
        
        # Botones
        frame_botones = ctk.CTkFrame(self.main_frame)
        frame_botones.pack(pady=30)
        
        ctk.CTkButton(
            frame_botones,
            text="✅ Crear",
            fg_color="#2ecc71",
            width=120,
            height=40
        ).pack(side="left", padx=10)
        
        ctk.CTkButton(
            frame_botones,
            text="↩️ Cancelar",
            fg_color="#95a5a6",
            width=120,
            height=40,
            command=self.mostrar_dashboard
        ).pack(side="left", padx=10)
    
    def mostrar_recursos(self):
        """Muestra la lista de recursos."""
        self.limpiar_frame()
        
        ctk.CTkLabel(
            self.main_frame,
            text="📊 Recursos del Refugio",
            font=ctk.CTkFont(size=24, weight="bold")
        ).pack(pady=30)
        
        # Pestañas
        tabview = ctk.CTkTabview(self.main_frame)
        tabview.pack(fill="both", expand=True, padx=40, pady=20)
        
        # Añadir pestañas
        tabview.add("🐕 Perros")
        tabview.add("👨‍⚕️ Personal")
        tabview.add("🏠 Instalaciones")
        
        # Contenido de pestaña Perros
        perros = [
            ["Rex", "Pastor Alemán", "3 años", "✅ Sano"],
            ["Luna", "Labrador", "2 años", "✅ Sano"],
            ["Toby", "Mestizo", "5 años", "🔴 Enfermo"]
        ]
        
        for perro in perros:
            frame = ctk.CTkFrame(tabview.tab("🐕 Perros"))
            frame.pack(fill="x", padx=10, pady=5)
            
            for valor in perro:
                ctk.CTkLabel(frame, text=valor).pack(side="left", padx=20)
    
    def mostrar_buscar(self):
        """Muestra búsqueda de huecos y eventos por perro."""
        self.limpiar_frame()
        
        # Usar pestañas para separar las dos funcionalidades de búsqueda
        tabview = ctk.CTkTabview(self.main_frame)
        tabview.pack(fill="both", expand=True, padx=20, pady=20)
        
        # ===== PESTAÑA 1: BÚSQUEDA DE EVENTOS POR PERRO =====
        tabview.add("🐕 Buscar Eventos por Perro")
        frame_perro = tabview.tab("🐕 Buscar Eventos por Perro")
        
        ctk.CTkLabel(
            frame_perro,
            text="🔍 Buscar Eventos de un Perro Específico",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(pady=20)
        
        # Frame para entrada de datos
        frame_input = ctk.CTkFrame(frame_perro)
        frame_input.pack(pady=20, padx=40, fill="x")
        
        # Campo para nombre o ID del perro
        ctk.CTkLabel(
            frame_input,
            text="Nombre o ID del Perro:",
            font=ctk.CTkFont(size=14)
        ).pack(side="left", padx=10)
        
        self.entry_perro_buscar = ctk.CTkEntry(frame_input, width=200)
        self.entry_perro_buscar.pack(side="left", padx=10)
        
        # Botón de búsqueda
        ctk.CTkButton(
            frame_input,
            text="🔍 Buscar Eventos",
            command=self.buscar_eventos_por_perro,
            fg_color="#9b59b6",
            width=150,
            height=35
        ).pack(side="left", padx=20)
        
        # Frame para resultados
        self.frame_resultados_perro = ctk.CTkScrollableFrame(
            frame_perro,
            height=400
        )
        self.frame_resultados_perro.pack(pady=20, padx=40, fill="both", expand=True)
        
        # Label inicial
        self.label_resultados_perro = ctk.CTkLabel(
            self.frame_resultados_perro,
            text="Ingresa el nombre de un perro y haz clic en 'Buscar Eventos'",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        self.label_resultados_perro.pack(pady=50)
        
        # ===== PESTAÑA 2: BÚSQUEDA DE HUECOS =====
        tabview.add("⏰ Buscar Hueco Disponible")
        frame_hueco = tabview.tab("⏰ Buscar Hueco Disponible")
        
        ctk.CTkLabel(
            frame_hueco,
            text="🔍 Buscar Hueco Disponible",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(pady=30)
        
        # Controles de búsqueda
        frame_duracion = ctk.CTkFrame(frame_hueco)
        frame_duracion.pack(pady=10)
        
        ctk.CTkLabel(
            frame_duracion,
            text="Duración (minutos):",
            font=ctk.CTkFont(size=14)
        ).pack(side="left", padx=10)
        
        self.entry_duracion = ctk.CTkEntry(frame_duracion, width=100)
        self.entry_duracion.insert(0, "60")
        self.entry_duracion.pack(side="left", padx=10)
        
        # Selección de recursos
        ctk.CTkLabel(
            frame_hueco,
            text="Recursos necesarios:",
            font=ctk.CTkFont(size=14)
        ).pack(pady=10)
        
        self.frame_recursos = ctk.CTkFrame(frame_hueco)
        self.frame_recursos.pack(pady=10)
        
        # Ejemplo de checkboxes para recursos
        recursos_ejemplo = ["Patio", "Veterinario", "Cuidador", "Jaula Grande"]
        self.checkboxes_recursos = []
        
        for recurso in recursos_ejemplo:
            var = ctk.StringVar(value="off")
            checkbox = ctk.CTkCheckBox(
                self.frame_recursos,
                text=recurso,
                variable=var,
                onvalue="on",
                offvalue="off"
            )
            checkbox.pack(side="left", padx=10)
            self.checkboxes_recursos.append((checkbox, var))
        
        # Botón de búsqueda
        ctk.CTkButton(
            frame_hueco,
            text="🔍 Buscar Hueco",
            command=self.buscar_hueco,
            fg_color="#3498db",
            width=200,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=30)
        
        # Frame para resultados de huecos
        self.frame_resultados_hueco = ctk.CTkFrame(frame_hueco)
        self.frame_resultados_hueco.pack(pady=20, padx=40, fill="both", expand=True)
    
    def buscar_eventos_por_perro(self):
        """Busca y muestra los eventos de un perro específico."""
        # Limpiar resultados anteriores
        for widget in self.frame_resultados_perro.winfo_children():
            widget.destroy()
        
        # Obtener nombre del perro
        nombre_perro = self.entry_perro_buscar.get().strip()
        
        if not nombre_perro:
            ctk.CTkLabel(
                self.frame_resultados_perro,
                text="⚠️ Por favor ingresa un nombre de perro",
                font=ctk.CTkFont(size=14),
                text_color="orange"
            ).pack(pady=50)
            return
        
        # Aquí normalmente conectarías con tu lógica de negocio
        # Por ahora, simularé datos de ejemplo
        eventos_encontrados = self.simular_busqueda_eventos_perro(nombre_perro)
        
        if not eventos_encontrados:
            ctk.CTkLabel(
                self.frame_resultados_perro,
                text=f"😔 No se encontraron eventos para '{nombre_perro}'",
                font=ctk.CTkFont(size=14),
                text_color="gray"
            ).pack(pady=50)
            return
        
        # Mostrar encabezado
        ctk.CTkLabel(
            self.frame_resultados_perro,
            text=f"📅 Eventos encontrados para '{nombre_perro}': {len(eventos_encontrados)}",
            font=ctk.CTkFont(size=16, weight="bold")
        ).pack(pady=(10, 20))
        
        # Mostrar cada evento
        for i, evento in enumerate(eventos_encontrados, 1):
            frame_evento = ctk.CTkFrame(
                self.frame_resultados_perro,
                corner_radius=10,
                border_width=1,
                border_color="#ddd"
            )
            frame_evento.pack(fill="x", pady=5, padx=10)
            
            # Número de evento
            ctk.CTkLabel(
                frame_evento,
                text=f"{i}.",
                font=ctk.CTkFont(size=14, weight="bold"),
                width=30
            ).pack(side="left", padx=10)
            
            # Detalles del evento
            frame_detalles = ctk.CTkFrame(frame_evento, fg_color="transparent")
            frame_detalles.pack(side="left", fill="both", expand=True, padx=10, pady=10)
            
            # Nombre del evento
            ctk.CTkLabel(
                frame_detalles,
                text=evento["nombre"],
                font=ctk.CTkFont(size=14, weight="bold")
            ).pack(anchor="w")
            
            # Fecha y hora
            frame_horario = ctk.CTkFrame(frame_detalles, fg_color="transparent")
            frame_horario.pack(anchor="w", pady=2)
            
            ctk.CTkLabel(
                frame_horario,
                text="📅",
                font=ctk.CTkFont(size=12)
            ).pack(side="left", padx=(0, 5))
            
            ctk.CTkLabel(
                frame_horario,
                text=evento["fecha_hora"],
                font=ctk.CTkFont(size=12)
            ).pack(side="left")
            
            # Tipo de evento
            frame_tipo = ctk.CTkFrame(frame_detalles, fg_color="transparent")
            frame_tipo.pack(anchor="w", pady=2)
            
            ctk.CTkLabel(
                frame_tipo,
                text="🏷️",
                font=ctk.CTkFont(size=12)
            ).pack(side="left", padx=(0, 5))
            
            ctk.CTkLabel(
                frame_tipo,
                text=evento["tipo"],
                font=ctk.CTkFont(size=12)
            ).pack(side="left")
            
            # Recursos
            if evento.get("recursos"):
                frame_recursos = ctk.CTkFrame(frame_detalles, fg_color="transparent")
                frame_recursos.pack(anchor="w", pady=2)
                
                ctk.CTkLabel(
                    frame_recursos,
                    text="🛠️",
                    font=ctk.CTkFont(size=12)
                ).pack(side="left", padx=(0, 5))
                
                recursos_texto = ", ".join(evento["recursos"])
                ctk.CTkLabel(
                    frame_recursos,
                    text=recursos_texto,
                    font=ctk.CTkFont(size=12)
                ).pack(side="left")
            
            # Estado
            estado_colors = {
                "completado": "#2ecc71",
                "pendiente": "#f39c12",
                "cancelado": "#e74c3c"
            }
            
            ctk.CTkLabel(
                frame_evento,
                text=evento["estado"].upper(),
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color="white",
                fg_color=estado_colors.get(evento["estado"], "#3498db"),
                corner_radius=15
            ).pack(side="right", padx=10, ipadx=10, ipady=2)
    
    def simular_busqueda_eventos_perro(self, nombre_perro):
        """Simula la búsqueda de eventos para un perro (datos de ejemplo)."""
        # Datos de ejemplo - en una aplicación real, esto vendría de tu base de datos
        datos_ejemplo = {
            "rex": [
                {
                    "nombre": "Paseo Matutino",
                    "tipo": "Paseo",
                    "fecha_hora": "22/12/2025 09:00 - 10:00",
                    "recursos": ["Patio", "Correa", "Cuidador"],
                    "estado": "completado"
                },
                {
                    "nombre": "Consulta Veterinaria",
                    "tipo": "Veterinario",
                    "fecha_hora": "22/12/2025 11:00 - 11:30",
                    "recursos": ["Sala Veterinaria", "Dr. Ana"],
                    "estado": "pendiente"
                },
                {
                    "nombre": "Sesión de Entrenamiento",
                    "tipo": "Entrenamiento",
                    "fecha_hora": "23/12/2025 15:00 - 16:00",
                    "recursos": ["Patio", "Entrenador Luis"],
                    "estado": "pendiente"
                }
            ],
            "luna": [
                {
                    "nombre": "Baño y Aseo",
                    "tipo": "Higiene",
                    "fecha_hora": "21/12/2025 14:00 - 15:00",
                    "recursos": ["Sala de Baño", "Shampoo especial"],
                    "estado": "completado"
                },
                {
                    "nombre": "Socialización",
                    "tipo": "Social",
                    "fecha_hora": "22/12/2025 16:00 - 17:00",
                    "recursos": ["Patio", "Jaula Social"],
                    "estado": "pendiente"
                }
            ],
            "toby": [
                {
                    "nombre": "Tratamiento Médico",
                    "tipo": "Veterinario",
                    "fecha_hora": "20/12/2025 10:00 - 11:00",
                    "recursos": ["Sala Aislamiento", "Dr. Carlos"],
                    "estado": "completado"
                }
            ]
        }
        
        # Buscar en minúsculas para hacer la búsqueda case-insensitive
        nombre_buscar = nombre_perro.lower()
        
        # Buscar coincidencias exactas o parciales
        for nombre_perro_db, eventos in datos_ejemplo.items():
            if nombre_buscar in nombre_perro_db or nombre_perro_db.startswith(nombre_buscar):
                return eventos
        
        # Si no se encuentra, devolver lista vacía
        return []
    
    def buscar_hueco(self):
        """Busca huecos disponibles (funcionalidad existente)."""
        # Limpiar resultados anteriores
        for widget in self.frame_resultados_hueco.winfo_children():
            widget.destroy()
        
        duracion = self.entry_duracion.get()
        
        # Aquí iría tu lógica de búsqueda de huecos
        # Por ahora, solo mostrar mensaje
        ctk.CTkLabel(
            self.frame_resultados_hueco,
            text=f"🔍 Buscando huecos de {duracion} minutos...",
            font=ctk.CTkFont(size=14)
        ).pack(pady=50)
        
        # Simular resultado
        ctk.CTkLabel(
            self.frame_resultados_hueco,
            text="✅ Hueco encontrado: 23/12/2025 10:30 - 11:30",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#2ecc71"
        ).pack(pady=10)
    
    def limpiar_frame(self):
        """Limpia el frame principal."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def guardar(self):
        """Guarda los datos."""
        # Aquí iría la lógica de guardado
        print("💾 Datos guardados")
    
    def salir(self):
        """Sale de la aplicación."""
        self.root.quit()
    
    def run(self):
        """Ejecuta la aplicación."""
        self.root.mainloop()

# ============ USO ============
if __name__ == "__main__":
    app = AppRefugio()
    app.run()
    
    