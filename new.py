import customtkinter as ctk
from datetime import datetime, timedelta

class AppRefugio:
    def __init__(self):
        # Configurar apariencia
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # Inicializar datos de ejemplo
        self.inicializar_datos_ejemplo()
        
        # Crear ventana principal
        self.root = ctk.CTk()
        self.root.title(" Refugio de Perritos 🐕 - Planificador ")
        self.root.geometry("1200x800")
        
        # Crear layout
        self.setup_ui()
    
    def inicializar_datos_ejemplo(self):
        """Inicializa datos de ejemplo para probar la aplicación."""
        # ===== DATOS DE EJEMPLO DE PERROS =====
        self.perros = [
            {
                "id": 1,
                "nombre": "Rex",
                "raza": "Pastor Alemán",
                "edad": "3 años",
                "salud": "✅ Sano",
                "fecha_ingreso": "15/01/2024",
                "disponible": True,
                "descripcion": "Muy juguetón, necesita ejercicio diario"
            },
            {
                "id": 2,
                "nombre": "Luna",
                "raza": "Labrador Retriever",
                "edad": "2 años",
                "salud": "✅ Sano",
                "fecha_ingreso": "20/02/2024",
                "disponible": True,
                "descripcion": "Tranquila y cariñosa, ideal para familias"
            },
            {
                "id": 3,
                "nombre": "Toby",
                "raza": "Mestizo",
                "edad": "5 años",
                "salud": "🟡 En tratamiento",
                "fecha_ingreso": "10/03/2024",
                "disponible": False,
                "descripcion": "Recuperándose de cirugía, necesita cuidados especiales"
            },
            {
                "id": 4,
                "nombre": "Bella",
                "raza": "Beagle",
                "edad": "4 años",
                "salud": "✅ Sano",
                "fecha_ingreso": "05/04/2024",
                "disponible": True,
                "descripcion": "Curiosa y activa, le encanta olfatear"
            },
            {
                "id": 5,
                "nombre": "Max",
                "raza": "Bulldog Francés",
                "edad": "1 año",
                "salud": "✅ Sano",
                "fecha_ingreso": "12/05/2024",
                "disponible": True,
                "descripcion": "Energético y amigable, necesita socialización"
            },
            {
                "id": 6,
                "nombre": "Coco",
                "raza": "Chihuahua",
                "edad": "6 meses",
                "salud": "🔴 Urgente",
                "fecha_ingreso": "18/06/2024",
                "disponible": False,
                "descripcion": "Desnutrido, necesita alimentación especial"
            }
        ]
        
        # ===== DATOS DE EJEMPLO DE EVENTOS =====
        hoy = datetime.now()
        self.eventos = [
            {
                "id": 1,
                "nombre": "Paseo Matutino",
                "tipo": "Paseo",
                "fecha": hoy.strftime("%d/%m/%Y"),
                "hora_inicio": "09:00",
                "hora_fin": "10:00",
                "perros": ["Rex", "Luna"],
                "recursos": ["Patio Grande", "Cuidador 1", "Correas"],
                "estado": "✅ Completado",
                "descripcion": "Paseo diario de los perros activos"
            },
            {
                "id": 2,
                "nombre": "Consulta Veterinaria",
                "tipo": "Veterinario",
                "fecha": hoy.strftime("%d/%m/%Y"),
                "hora_inicio": "11:00",
                "hora_fin": "12:00",
                "perros": ["Toby"],
                "recursos": ["Sala Veterinaria", "Dr. Ana", "Kit Médico"],
                "estado": "⏳ En curso",
                "descripcion": "Revisión post-operatoria"
            },
            {
                "id": 3,
                "nombre": "Sesión de Entrenamiento",
                "tipo": "Entrenamiento",
                "fecha": hoy.strftime("%d/%m/%Y"),
                "hora_inicio": "14:00",
                "hora_fin": "15:00",
                "perros": ["Max"],
                "recursos": ["Área de Entrenamiento", "Entrenador Luis"],
                "estado": "📅 Pendiente",
                "descripcion": "Entrenamiento básico de obediencia"
            },
            {
                "id": 4,
                "nombre": "Baño y Aseo",
                "tipo": "Higiene",
                "fecha": hoy.strftime("%d/%m/%Y"),
                "hora_inicio": "16:00",
                "hora_fin": "17:00",
                "perros": ["Bella", "Luna"],
                "recursos": ["Sala de Baño", "Peluquero", "Secador"],
                "estado": "📅 Pendiente",
                "descripcion": "Baño completo y corte de uñas"
            },
            {
                "id": 5,
                "nombre": "Visita de Adopción",
                "tipo": "Adopción",
                "fecha": (hoy + timedelta(days=1)).strftime("%d/%m/%Y"),
                "hora_inicio": "10:00",
                "hora_fin": "11:00",
                "perros": ["Rex"],
                "recursos": ["Sala de Visitas", "Coordinadora María"],
                "estado": "📅 Pendiente",
                "descripcion": "Familia interesada en adopción"
            }
        ]
        
        # ===== DATOS DE EJEMPLO DE RECURSOS =====
        self.recursos = {
            "personal": [
                {"nombre": "Dr. Ana", "tipo": "Veterinario", "disponible": True},
                {"nombre": "Entrenador Luis", "tipo": "Entrenador", "disponible": True},
                {"nombre": "Cuidador 1", "tipo": "Cuidador", "disponible": True},
                {"nombre": "Cuidador 2", "tipo": "Cuidador", "disponible": False},
                {"nombre": "Coordinadora María", "tipo": "Coordinación", "disponible": True},
                {"nombre": "Peluquero", "tipo": "Estética", "disponible": True}
            ],
            "instalaciones": [
                {"nombre": "Patio Grande", "tipo": "Espacio", "capacidad": "10 perros", "disponible": True},
                {"nombre": "Sala Veterinaria", "tipo": "Consultorio", "capacidad": "1 perro", "disponible": True},
                {"nombre": "Sala de Baño", "tipo": "Higiene", "capacidad": "2 perros", "disponible": True},
                {"nombre": "Sala de Visitas", "tipo": "Reunión", "capacidad": "4 personas", "disponible": True},
                {"nombre": "Área de Entrenamiento", "tipo": "Entrenamiento", "capacidad": "3 perros", "disponible": True},
                {"nombre": "Jaula Social", "tipo": "Alojamiento", "capacidad": "5 perros", "disponible": True}
            ],
            "equipos": [
                {"nombre": "Kit Médico", "tipo": "Veterinario", "cantidad": "2", "disponible": True},
                {"nombre": "Correas", "tipo": "Paseo", "cantidad": "15", "disponible": True},
                {"nombre": "Comederos", "tipo": "Alimentación", "cantidad": "20", "disponible": True},
                {"nombre": "Juguetes", "tipo": "Entretenimiento", "cantidad": "30", "disponible": True},
                {"nombre": "Camas", "tipo": "Descanso", "cantidad": "12", "disponible": True},
                {"nombre": "Transportín", "tipo": "Transporte", "cantidad": "5", "disponible": False}
            ]
        }
    
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
            ("🔍 Buscar", self.mostrar_buscar),
            ("🐕 Perros", self.mostrar_perros)  # Nuevo botón
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
        
        # Calcular estadísticas
        eventos_hoy = len([e for e in self.eventos if e['fecha'] == datetime.now().strftime('%d/%m/%Y')])
        """perros_activos = len([p for p in self.perros if p['disponible']])
        eventos_pendientes = len([e for e in self.eventos if e['estado'] == '📅 Pendiente'])
        eventos_completados = len([e for e in self.eventos if e['estado'] == '✅ Completado'])"""
        
        # Tarjetas de resumen
        """frame_cards = ctk.CTkFrame(self.main_frame)
        frame_cards.pack(pady=20, padx=20, fill="both", expand=True)
        
        cards = [
            ("📅 Eventos Hoy", str(eventos_hoy), "#3498db"),
            ("🐕 Perros Activos", str(perros_activos), "#2ecc71"),
            ("⚠️ Pendientes", str(eventos_pendientes), "#e74c3c"),
            ("✅ Completados", str(eventos_completados), "#f39c12")
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
        """
        # Próximos eventos
        ctk.CTkLabel(
            self.main_frame,
            text="📅 Eventos Proximos",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(pady=(40, 10))
        
        # Mostrar los próximos 3 eventos
        eventos_proximos = sorted(
            self.eventos,
            key=lambda x: datetime.strptime(f"{x['fecha']} {x['hora_inicio']}", "%d/%m/%Y %H:%M")
        )[:3]
    
        for evento in eventos_proximos:
            frame_evento = ctk.CTkFrame(
                self.main_frame,
                height=70,
                corner_radius=10
            )
            frame_evento.pack(fill="x", padx=40, pady=5)
            
            # Nombre y tipo
            ctk.CTkLabel(
                frame_evento,
                text=f"📋 {evento['nombre']}",
                font=ctk.CTkFont(size=14, weight="bold")
            ).place(relx=0.05, rely=0.3, anchor="w")
            
            ctk.CTkLabel(
                frame_evento,
                text=f"🏷️ {evento['tipo']}",
                font=ctk.CTkFont(size=12)
            ).place(relx=0.05, rely=0.7, anchor="w")
            
            # Fecha y hora
            ctk.CTkLabel(
                frame_evento,
                text=f"📅 {evento['fecha']}",
                font=ctk.CTkFont(size=12)
            ).place(relx=0.35, rely=0.3, anchor="w")
            
            ctk.CTkLabel(
                frame_evento,
                text=f"⏰ {evento['hora_inicio']} - {evento['hora_fin']}",
                font=ctk.CTkFont(size=12)
            ).place(relx=0.35, rely=0.7, anchor="w")
            
            # Perros
            perros_text = ", ".join(evento['perros'])
            ctk.CTkLabel(
                frame_evento,
                text=f"🐕 {perros_text}",
                font=ctk.CTkFont(size=12)
            ).place(relx=0.65, rely=0.3, anchor="w")
            
            # Estado
            ctk.CTkLabel(
                frame_evento,
                text=evento['estado'],
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color="white",
                fg_color={
                    "✅ Completado": "#2ecc71",
                    "📅 Pendiente": "#f39c12",
                    "⏳ En curso": "#3498db"
                }.get(evento['estado'], "#95a5a6"),
                corner_radius=15
            ).place(relx=0.9, rely=0.5, anchor="center")
    
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
        
        """ctk.CTkButton(
            frame_titulo,
            text="🔄 Actualizar",
            width=100,
            command=self.mostrar_eventos
        ).pack(side="right", padx=10)"""
        
        # Frame scrollable para eventos
        scroll_frame = ctk.CTkScrollableFrame(self.main_frame, height=500)
        scroll_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Encabezados de tabla
        frame_encabezados = ctk.CTkFrame(scroll_frame, height=40)
        frame_encabezados.pack(fill="x", pady=(0, 10))
        
        encabezados = ["ID", "Nombre", "Fecha", "Hora", "Tipo", "Perros", "Estado"]
        widths = [50, 200, 100, 120, 120, 150, 100]
        
        for i, (encabezado, width) in enumerate(zip(encabezados, widths)):
            ctk.CTkLabel(
                frame_encabezados,
                text=encabezado,
                font=ctk.CTkFont(size=12, weight="bold"),
                width=width
            ).place(relx=i/7, rely=0.5, anchor="w", x=10)
        
        # Mostrar eventos
        for evento in self.eventos:
            frame_evento = ctk.CTkFrame(
                scroll_frame,
                height=50,
                corner_radius=10
            )
            frame_evento.pack(fill="x", pady=5)
            
            # ID
            ctk.CTkLabel(
                frame_evento,
                text=str(evento['id']),
                font=ctk.CTkFont(size=12),
                width=50
            ).place(relx=0/7, rely=0.5, anchor="w", x=10)
            
            # Nombre
            ctk.CTkLabel(
                frame_evento,
                text=evento['nombre'],
                font=ctk.CTkFont(size=12),
                width=200
            ).place(relx=1/7, rely=0.5, anchor="w", x=10)
            
            # Fecha
            ctk.CTkLabel(
                frame_evento,
                text=evento['fecha'],
                font=ctk.CTkFont(size=12),
                width=100
            ).place(relx=2/7, rely=0.5, anchor="w", x=10)
            
            # Hora
            ctk.CTkLabel(
                frame_evento,
                text=f"{evento['hora_inicio']}-{evento['hora_fin']}",
                font=ctk.CTkFont(size=12),
                width=120
            ).place(relx=3/7, rely=0.5, anchor="w", x=10)
            
            # Tipo
            ctk.CTkLabel(
                frame_evento,
                text=evento['tipo'],
                font=ctk.CTkFont(size=12),
                width=120
            ).place(relx=4/7, rely=0.5, anchor="w", x=10)
            
            # Perros
            perros_text = ", ".join(evento['perros'])
            ctk.CTkLabel(
                frame_evento,
                text=perros_text[:20] + ("..." if len(perros_text) > 20 else ""),
                font=ctk.CTkFont(size=12),
                width=150
            ).place(relx=5/7, rely=0.5, anchor="w", x=10)
            
            # Estado
            estado_color = {
                "✅ Completado": "#2ecc71",
                "📅 Pendiente": "#f39c12",
                "⏳ En curso": "#3498db"
            }.get(evento['estado'], "#95a5a6")
            
            ctk.CTkLabel(
                frame_evento,
                text=evento['estado'],
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color="white",
                fg_color=estado_color,
                corner_radius=15,
                width=100
            ).place(relx=6/7, rely=0.5, anchor="w", x=10)
    
    def mostrar_nuevo(self):
        """Muestra formulario para nuevo evento."""
        self.limpiar_frame()
        
        ctk.CTkLabel(
            self.main_frame,
            text="➕ Nuevo Evento",
            font=ctk.CTkFont(size=24, weight="bold")
        ).pack(pady=30)
        
        # Formulario con más campos
        campos = [
            ("Nombre del Evento:", ctk.CTkEntry(self.main_frame, width=300, placeholder_text="Ej: Paseo Matutino")),
            ("Fecha:", ctk.CTkEntry(self.main_frame, width=150, placeholder_text="DD/MM/AAAA")),
            ("Hora Inicio:", ctk.CTkEntry(self.main_frame, width=100, placeholder_text="HH:MM")),
            ("Hora Fin:", ctk.CTkEntry(self.main_frame, width=100, placeholder_text="HH:MM")),
            ("Tipo de Evento:", ctk.CTkComboBox(self.main_frame, width=150, values=["Paseo", "Veterinario", "Entrenamiento", "Higiene", "Adopción", "Alimentación"])),
            ("Perros:", ctk.CTkEntry(self.main_frame, width=200, placeholder_text="Separados por comas"))
        ]
        
        for label, widget in campos:
            frame = ctk.CTkFrame(self.main_frame, height=40)
            frame.pack(fill="x", padx=80, pady=8)
            
            ctk.CTkLabel(frame, text=label, width=140).pack(side="left", padx=10)
            widget.pack(side="left", padx=10)
        
        # Descripción
        frame_desc = ctk.CTkFrame(self.main_frame, height=80)
        frame_desc.pack(fill="x", padx=80, pady=15)
        
        ctk.CTkLabel(frame_desc, text="Descripción:", width=140).pack(side="left", padx=10)
        textbox_desc = ctk.CTkTextbox(frame_desc, width=300, height=70)
        textbox_desc.pack(side="left", padx=10)
        
        # Botones
        frame_botones = ctk.CTkFrame(self.main_frame)
        frame_botones.pack(pady=30)
        
        ctk.CTkButton(
            frame_botones,
            text="✅ Crear Evento",
            fg_color="#2ecc71",
            width=150,
            height=40,
            command=self.crear_evento_ejemplo
        ).pack(side="left", padx=10)
        
        ctk.CTkButton(
            frame_botones,
            text="↩️ Cancelar",
            fg_color="#95a5a6",
            width=150,
            height=40,
            command=self.mostrar_dashboard
        ).pack(side="left", padx=10)
    
    def crear_evento_ejemplo(self):
        """Función de ejemplo para crear un evento."""
        print(f"✅ Evento creado")
        self.mostrar_eventos()
        
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
        tabview.add("👨‍⚕️ Personal")
        tabview.add("🏠 Instalaciones")
        tabview.add("🔧 Equipos")
        
        # ===== PESTAÑA PERSONAL =====
        frame_personal = ctk.CTkScrollableFrame(tabview.tab("👨‍⚕️ Personal"))
        frame_personal.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Encabezados
        encabezados_personal = ["Nombre", "Tipo", "Disponibilidad"]
        for i, enc in enumerate(encabezados_personal):
            ctk.CTkLabel(
                frame_personal,
                text=enc,
                font=ctk.CTkFont(size=12, weight="bold")
            ).grid(row=0, column=i, padx=20, pady=10, sticky="w")
        
        # Datos de personal
        for idx, recurso in enumerate(self.recursos["personal"], start=1):
            # Nombre
            ctk.CTkLabel(
                frame_personal,
                text=recurso["nombre"],
                font=ctk.CTkFont(size=12)
            ).grid(row=idx, column=0, padx=20, pady=5, sticky="w")
            
            # Tipo
            ctk.CTkLabel(
                frame_personal,
                text=recurso["tipo"],
                font=ctk.CTkFont(size=12)
            ).grid(row=idx, column=1, padx=20, pady=5, sticky="w")
            
            # Disponibilidad
            disponible_text = "✅ Disponible" if recurso["disponible"] else "❌ No disponible"
            disponible_color = "#2ecc71" if recurso["disponible"] else "#e74c3c"
            
            ctk.CTkLabel(
                frame_personal,
                text=disponible_text,
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color=disponible_color
            ).grid(row=idx, column=2, padx=20, pady=5, sticky="w")
        
        # ===== PESTAÑA INSTALACIONES =====
        frame_instalaciones = ctk.CTkScrollableFrame(tabview.tab("🏠 Instalaciones"))
        frame_instalaciones.pack(fill="both", expand=True, padx=10, pady=10)
        
        encabezados_inst = ["Nombre", "Tipo", "Capacidad", "Disponibilidad"]
        for i, enc in enumerate(encabezados_inst):
            ctk.CTkLabel(
                frame_instalaciones,
                text=enc,
                font=ctk.CTkFont(size=12, weight="bold")
            ).grid(row=0, column=i, padx=15, pady=10, sticky="w")
        
        for idx, recurso in enumerate(self.recursos["instalaciones"], start=1):
            ctk.CTkLabel(frame_instalaciones, text=recurso["nombre"]).grid(row=idx, column=0, padx=15, pady=5, sticky="w")
            ctk.CTkLabel(frame_instalaciones, text=recurso["tipo"]).grid(row=idx, column=1, padx=15, pady=5, sticky="w")
            ctk.CTkLabel(frame_instalaciones, text=recurso["capacidad"]).grid(row=idx, column=2, padx=15, pady=5, sticky="w")
            
            disp_text = "✅ Sí" if recurso["disponible"] else "❌ No"
            disp_color = "#2ecc71" if recurso["disponible"] else "#e74c3c"
            ctk.CTkLabel(frame_instalaciones, text=disp_text, text_color=disp_color).grid(row=idx, column=3, padx=15, pady=5, sticky="w")
        
        # ===== PESTAÑA EQUIPOS =====
        frame_equipos = ctk.CTkScrollableFrame(tabview.tab("🔧 Equipos"))
        frame_equipos.pack(fill="both", expand=True, padx=10, pady=10)
        
        encabezados_eq = ["Nombre", "Tipo", "Cantidad", "Disponibilidad"]
        for i, enc in enumerate(encabezados_eq):
            ctk.CTkLabel(
                frame_equipos,
                text=enc,
                font=ctk.CTkFont(size=12, weight="bold")
            ).grid(row=0, column=i, padx=15, pady=10, sticky="w")
        
        for idx, recurso in enumerate(self.recursos["equipos"], start=1):
            ctk.CTkLabel(frame_equipos, text=recurso["nombre"]).grid(row=idx, column=0, padx=15, pady=5, sticky="w")
            ctk.CTkLabel(frame_equipos, text=recurso["tipo"]).grid(row=idx, column=1, padx=15, pady=5, sticky="w")
            ctk.CTkLabel(frame_equipos, text=recurso["cantidad"]).grid(row=idx, column=2, padx=15, pady=5, sticky="w")
            
            disp_text = "✅ Sí" if recurso["disponible"] else "❌ No"
            disp_color = "#2ecc71" if recurso["disponible"] else "#e74c3c"
            ctk.CTkLabel(frame_equipos, text=disp_text, text_color=disp_color).grid(row=idx, column=3, padx=15, pady=5, sticky="w")
        
    def mostrar_perros(self):
        """Muestra la lista completa de perros."""
        self.limpiar_frame()
        
        ctk.CTkLabel(
            self.main_frame,
            text="🐕 Perros del Refugio",
            font=ctk.CTkFont(size=24, weight="bold")
        ).pack(pady=30)
        
        # Frame para las tarjetas de perros
        frame_perros = ctk.CTkScrollableFrame(self.main_frame)
        frame_perros.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Crear tarjetas para cada perro
        for perro in self.perros:
            self.crear_tarjeta_perro(frame_perros, perro)
    
    def crear_tarjeta_perro(self, parent, perro):
        """Crea una tarjeta visual para un perro."""
        # Determinar color de borde según estado de salud
        color_borde = {
            "✅ Sano": "#2ecc71",
            "🟡 En tratamiento": "#f39c12",
            "🔴 Urgente": "#e74c3c"
        }.get(perro["salud"], "#3498db")
        
        # Tarjeta principal
        card = ctk.CTkFrame(
            parent,
            border_width=2,
            border_color=color_borde,
            corner_radius=15
        )
        card.pack(fill="x", pady=10, padx=10)
        
        # Contenido de la tarjeta
        # Fila 1: Nombre y raza
        frame_fila1 = ctk.CTkFrame(card, fg_color="transparent")
        frame_fila1.pack(fill="x", padx=20, pady=(15, 5))
        
        ctk.CTkLabel(
            frame_fila1,
            text=perro["nombre"],
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(side="left")
        
        ctk.CTkLabel(
            frame_fila1,
            text=f"({perro['raza']})",
            font=ctk.CTkFont(size=14)
        ).pack(side="left", padx=10)
        
        # Estado de salud
        ctk.CTkLabel(
            frame_fila1,
            text=perro["salud"],
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=color_borde
        ).pack(side="right")
        
        # Fila 2: Información básica
        frame_fila2 = ctk.CTkFrame(card, fg_color="transparent")
        frame_fila2.pack(fill="x", padx=20, pady=5)
        
        # Edad
        ctk.CTkLabel(
            frame_fila2,
            text=f"🎂 {perro['edad']}",
            font=ctk.CTkFont(size=12)
        ).pack(side="left", padx=5)
        
        # Disponibilidad
        disp_text = "✅ Disponible para eventos" if perro["disponible"] else "⛔ No disponible"
        disp_color = "#2ecc71" if perro["disponible"] else "#e74c3c"
        
        ctk.CTkLabel(
            frame_fila2,
            text=disp_text,
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=disp_color
        ).pack(side="left", padx=20)
        
        # Fecha de ingreso
        ctk.CTkLabel(
            frame_fila2,
            text=f"📅 Ingreso: {perro['fecha_ingreso']}",
            font=ctk.CTkFont(size=11)
        ).pack(side="right", padx=5)
        
        # Fila 3: Descripción
        frame_fila3 = ctk.CTkFrame(card, fg_color="transparent")
        frame_fila3.pack(fill="x", padx=20, pady=(5, 15))
        
        ctk.CTkLabel(
            frame_fila3,
            text=f"📝 {perro['descripcion']}",
            font=ctk.CTkFont(size=11),
            justify="left"
        ).pack(anchor="w")
    
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
        
        # Campo para nombre del perro
        ctk.CTkLabel(
            frame_input,
            text="Nombre del Perro:",
            font=ctk.CTkFont(size=14)
        ).pack(side="left", padx=10)
        
        # ComboBox con nombres de perros
        nombres_perros = [p["nombre"] for p in self.perros]
        self.combo_perro_buscar = ctk.CTkComboBox(
            frame_input,
            values=nombres_perros,
            width=200
        )
        self.combo_perro_buscar.pack(side="left", padx=10)
        
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
            text="Selecciona un perro y haz clic en 'Buscar Eventos'",
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
        
        # Checkboxes para recursos (ejemplo)
        recursos_ejemplo = ["Patio Grande", "Sala Veterinaria", "Cuidador 1", "Kit Médico"]
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
        nombre_perro = self.combo_perro_buscar.get().strip()
        
        if not nombre_perro:
            ctk.CTkLabel(
                self.frame_resultados_perro,
                text="⚠️ Por favor selecciona un perro",
                font=ctk.CTkFont(size=14),
                text_color="orange"
            ).pack(pady=50)
            return
        
        # Buscar eventos que involucren a este perro
        eventos_encontrados = []
        for evento in self.eventos:
            if nombre_perro in evento['perros']:
                eventos_encontrados.append(evento)
        
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
                text=evento['nombre'],
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
                text=f"{evento['fecha']} {evento['hora_inicio']}-{evento['hora_fin']}",
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
                text=evento['tipo'],
                font=ctk.CTkFont(size=12)
            ).pack(side="left")
            
            # Recursos
            if evento.get('recursos'):
                frame_recursos = ctk.CTkFrame(frame_detalles, fg_color="transparent")
                frame_recursos.pack(anchor="w", pady=2)
                
                ctk.CTkLabel(
                    frame_recursos,
                    text="🛠️",
                    font=ctk.CTkFont(size=12)
                ).pack(side="left", padx=(0, 5))
                
                recursos_texto = ", ".join(evento['recursos'][:3])
                if len(evento['recursos']) > 3:
                    recursos_texto += f" y {len(evento['recursos']) - 3} más"
                
                ctk.CTkLabel(
                    frame_recursos,
                    text=recursos_texto,
                    font=ctk.CTkFont(size=12)
                ).pack(side="left")
            
            # Estado
            estado_colors = {
                "✅ Completado": "#2ecc71",
                "📅 Pendiente": "#f39c12",
                "⏳ En curso": "#3498db"
            }
            
            estado_color = estado_colors.get(evento['estado'], "#95a5a6")
            
            ctk.CTkLabel(
                frame_evento,
                text=evento['estado'],
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color="white",
                fg_color=estado_color,
                corner_radius=15
            ).pack(side="right", padx=10, ipadx=10, ipady=2)
    
    def buscar_hueco(self):
        """Busca huecos disponibles."""
        # Limpiar resultados anteriores
        for widget in self.frame_resultados_hueco.winfo_children():
            widget.destroy()
        
        try:
            duracion = int(self.entry_duracion.get())
        except ValueError:
            duracion = 60
        
        # Obtener recursos seleccionados
        recursos_seleccionados = []
        for checkbox, var in self.checkboxes_recursos:
            if var.get() == "on":
                recursos_seleccionados.append(checkbox.cget("text"))
        
        # Mostrar búsqueda en progreso
        ctk.CTkLabel(
            self.frame_resultados_hueco,
            text=f"🔍 Buscando huecos de {duracion} minutos...",
            font=ctk.CTkFont(size=14)
        ).pack(pady=20)
        
        # Simular búsqueda (en un sistema real, aquí iría la lógica)
        import random
        huecos_simulados = [
            ("Hoy", "15:30 - 16:30"),
            ("Mañana", "10:00 - 11:00"),
            ("Mañana", "14:00 - 15:00"),
            ("Pasado mañana", "09:00 - 10:00")
        ]
        
        hueco_encontrado = random.choice(huecos_simulados)
        
        # Mostrar resultado
        ctk.CTkLabel(
            self.frame_resultados_hueco,
            text="✅ Hueco encontrado:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#2ecc71"
        ).pack(pady=10)
        
        ctk.CTkLabel(
            self.frame_resultados_hueco,
            text=f"📅 {hueco_encontrado[0]}",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=5)
        
        ctk.CTkLabel(
            self.frame_resultados_hueco,
            text=f"⏰ {hueco_encontrado[1]}",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(pady=10)
        
        # Mostrar recursos seleccionados
        if recursos_seleccionados:
            ctk.CTkLabel(
                self.frame_resultados_hueco,
                text=f"🛠️ Recursos: {', '.join(recursos_seleccionados)}",
                font=ctk.CTkFont(size=12)
            ).pack(pady=10)
        
        # Botón para reservar
        ctk.CTkButton(
            self.frame_resultados_hueco,
            text="📅 Reservar este Hueco",
            fg_color="#3498db",
            command=lambda: print(f"Reservando hueco: {hueco_encontrado}")
        ).pack(pady=20)
    
    def limpiar_frame(self):
        """Limpia el frame principal."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def guardar(self):
        """Guarda los datos (simulado)."""
        # En una aplicación real, aquí guardarías los datos
        print("💾 Datos guardados exitosamente")
        
        # Mostrar mensaje temporal
        for widget in self.main_frame.winfo_children():
            if isinstance(widget, ctk.CTkLabel) and "guardados" in widget.cget("text").lower():
                return
        
        msg = ctk.CTkLabel(
            self.main_frame,
            text="💾 Datos guardados exitosamente",
            font=ctk.CTkFont(size=12),
            text_color="#2ecc71"
        )
        msg.place(relx=0.5, rely=0.95, anchor="center")
        self.root.after(2000, msg.destroy)
    
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