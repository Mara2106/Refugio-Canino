import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime, timedelta
from evento import Evento

class VentanaPrincipal(ctk.CTk):
    """Ventana principal de la aplicación"""
    
    def __init__(self, controlador):
        super().__init__()
        
        self.controlador = controlador
        
        # Configuración de la ventana
        self.title(" Planificador de Eventos - Refugio Canino🐕")
        self.geometry("1200x700")
        
        # Configurar tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Crear interfaz
        self.crear_widgets()
        
        # Cargar datos
        self.cargar_datos_iniciales()
    
    def crear_widgets(self):
        """Crea todos los widgets de la interfaz"""
        
        # ===== PANEL IZQUIERDO (Menú) =====
        self.panel_menu = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.panel_menu.pack(side="left", fill="y", padx=0, pady=0)
        self.panel_menu.pack_propagate(False)
        
        # Título
        self.label_titulo = ctk.CTkLabel(
            self.panel_menu,
            text="🐕 REFUGIO\nCANINO",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.label_titulo.pack(pady=20)
        
        # Botones del menú
        self.btn_inicio = ctk.CTkButton(
            self.panel_menu,
            text="🏠 Inicio",
            command=self.mostrar_inicio,
            height=40
        )
        self.btn_inicio.pack(pady=10, padx=20, fill="x")
        
        self.btn_eventos = ctk.CTkButton(
            self.panel_menu,
            text="📅 Eventos",
            command=self.mostrar_eventos,
            height=40
        )
        self.btn_eventos.pack(pady=10, padx=20, fill="x")
        
        self.btn_recursos = ctk.CTkButton(
            self.panel_menu,
            text="📦 Recursos",
            command=self.mostrar_recursos,
            height=40
        )
        self.btn_recursos.pack(pady=10, padx=20, fill="x")
        
        self.btn_buscar = ctk.CTkButton(
            self.panel_menu,
            text="🔍 Buscar Hueco",
            command=self.mostrar_buscar_hueco,
            height=40
        )
        self.btn_buscar.pack(pady=10, padx=20, fill="x")
        
        # Separador
        ctk.CTkLabel(self.panel_menu, text="").pack(expand=True)
        
        # Botón guardar
        self.btn_guardar = ctk.CTkButton(
            self.panel_menu,
            text="💾 Guardar",
            command=self.guardar_datos,
            height=40,
            fg_color="green",
            hover_color="darkgreen"
        )
        self.btn_guardar.pack(pady=10, padx=20, fill="x")
        
        # Botón salir
        self.btn_salir = ctk.CTkButton(
            self.panel_menu,
            text="Salir",
            command=self.salir,
            height=40,
            fg_color="red",
            hover_color="maroon"
        )
        self.btn_salir.pack(pady=10, padx=20, fill="x")
        
        # ===== PANEL PRINCIPAL (Contenido) =====
        self.panel_principal = ctk.CTkFrame(self, corner_radius=0)
        self.panel_principal.pack(side="right", fill="both", expand=True, padx=0, pady=0)
        
        # Mostrar pantalla de inicio por defecto
        self.mostrar_inicio()
    
    def limpiar_panel_principal(self):
        """Limpia el panel principal"""
        for widget in self.panel_principal.winfo_children():
            widget.destroy()
    
    # ========== PANTALLA INICIO ==========
    
    def mostrar_inicio(self):
        """Muestra la pantalla de inicio con estadísticas"""
        self.limpiar_panel_principal()
        
        # Título
        titulo = ctk.CTkLabel(
            self.panel_principal,
            text="🏠 Panel de Control",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        titulo.pack(pady=20)
        
        # Frame para estadísticas
        frame_stats = ctk.CTkFrame(self.panel_principal)
        frame_stats.pack(pady=20, padx=40, fill="both", expand=True)
        
        # Obtener estadísticas
        stats = self.controlador.obtener_estadisticas()
        
        # Crear tarjetas de estadísticas
        frame_tarjetas = ctk.CTkFrame(frame_stats, fg_color="transparent")
        frame_tarjetas.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Configurar grid
        frame_tarjetas.grid_columnconfigure((0, 1, 2), weight=1)
        frame_tarjetas.grid_rowconfigure((0, 1), weight=1)
        
        # Tarjetas
        self.crear_tarjeta_stat(frame_tarjetas, "🐕 Perros", stats['total_perros'], 0, 0)
        self.crear_tarjeta_stat(frame_tarjetas, "👥 Personal", stats['total_personal'], 0, 1)
        self.crear_tarjeta_stat(frame_tarjetas, "🏢 Espacios", stats['total_espacios'], 0, 2)
        self.crear_tarjeta_stat(frame_tarjetas, "📅 Eventos Totales", stats['total_eventos'], 1, 0)
        self.crear_tarjeta_stat(frame_tarjetas, "🔜 Próximos", stats['eventos_futuros'], 1, 1)
        self.crear_tarjeta_stat(frame_tarjetas, "✅ Completados", stats['eventos_pasados'], 1, 2)
        
        # Eventos de hoy
        frame_hoy = ctk.CTkFrame(frame_stats)
        frame_hoy.pack(pady=20, padx=20, fill="both", expand=True)
        
        label_hoy = ctk.CTkLabel(
            frame_hoy,
            text="📋 Eventos de Hoy",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        label_hoy.pack(pady=10)
        
        eventos_hoy = self.controlador.obtener_eventos_hoy()
        
        if eventos_hoy:
            for evento in eventos_hoy:
                texto = f"{evento.inicio.strftime('%H:%M')} - {evento.tipo}"
                label_evento = ctk.CTkLabel(frame_hoy, text=texto, anchor="w")
                label_evento.pack(pady=5, padx=20, fill="x")
        else:
            label_sin = ctk.CTkLabel(frame_hoy, text="No hay eventos programados para hoy")
            label_sin.pack(pady=10)
    
    def crear_tarjeta_stat(self, parent, titulo, valor, row, col):
        """Crea una tarjeta de estadística"""
        tarjeta = ctk.CTkFrame(parent, corner_radius=10)
        tarjeta.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        
        label_titulo = ctk.CTkLabel(
            tarjeta,
            text=titulo,
            font=ctk.CTkFont(size=14)
        )
        label_titulo.pack(pady=(20, 5))
        
        label_valor = ctk.CTkLabel(
            tarjeta,
            text=str(valor),
            font=ctk.CTkFont(size=32, weight="bold")
        )
        label_valor.pack(pady=(5, 20))
    
    # ========== PANTALLA EVENTOS ==========
    
    def mostrar_eventos(self):
        """Muestra la pantalla de gestión de eventos"""
        self.limpiar_panel_principal()
        
        # Título
        titulo = ctk.CTkLabel(
            self.panel_principal,
            text="📅 Gestión de Eventos",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        titulo.pack(pady=20)
        
        # Botón crear evento
        btn_crear = ctk.CTkButton(
            self.panel_principal,
            text="➕ Crear Nuevo Evento",
            command=self.mostrar_dialogo_crear_evento,
            height=40,
            fg_color="green",
            hover_color="darkgreen"
        )
        btn_crear.pack(pady=10)
        
        # Frame para lista de eventos
        frame_lista = ctk.CTkScrollableFrame(self.panel_principal)
        frame_lista.pack(pady=10, padx=40, fill="both", expand=True)
        
        # Obtener eventos
        eventos = self.controlador.obtener_eventos(incluir_pasados=False)
        
        if eventos:
            for evento in eventos:
                self.crear_tarjeta_evento(frame_lista, evento)
        else:
            label_sin = ctk.CTkLabel(
                frame_lista,
                text="No hay eventos programados",
                font=ctk.CTkFont(size=16)
            )
            label_sin.pack(pady=50)
    
    def crear_tarjeta_evento(self, parent, evento):
        """Crea una tarjeta para mostrar un evento"""
        frame = ctk.CTkFrame(parent, corner_radius=10)
        frame.pack(pady=10, padx=10, fill="x")
        
        # Información del evento
        frame_info = ctk.CTkFrame(frame, fg_color="transparent")
        frame_info.pack(side="left", fill="both", expand=True, padx=20, pady=15)
        
        label_tipo = ctk.CTkLabel(
            frame_info,
            text=f"📌 {evento.tipo}",
            font=ctk.CTkFont(size=16, weight="bold"),
            anchor="w"
        )
        label_tipo.pack(anchor="w")
        
        fecha_texto = evento.inicio.strftime("%d/%m/%Y %H:%M")
        label_fecha = ctk.CTkLabel(
            frame_info,
            text=f"📅 {fecha_texto} ({evento.duracion_minutos()} min)",
            anchor="w"
        )
        label_fecha.pack(anchor="w", pady=2)
        
        # Recursos
        recursos_texto = ", ".join([
            self.controlador.obtener_recurso(rid).nombre 
            for rid in evento.recursos_ids 
            if self.controlador.obtener_recurso(rid)
        ])
        label_recursos = ctk.CTkLabel(
            frame_info,
            text=f"🔧 {recursos_texto}",
            anchor="w"
        )
        label_recursos.pack(anchor="w", pady=2)
        
        # Botón eliminar
        btn_eliminar = ctk.CTkButton(
            frame,
            text="❌ Eliminar",
            command=lambda e=evento: self.eliminar_evento(e.id),
            width=100,
            height=30,
            fg_color="red",
            hover_color="darkred"
        )
        btn_eliminar.pack(side="right", padx=20)
    
    def mostrar_dialogo_crear_evento(self):
        """Muestra el diálogo para crear un evento"""
        dialogo = ctk.CTkToplevel(self)
        dialogo.title("Crear Nuevo Evento")
        dialogo.geometry("600x700")
        dialogo.grab_set()
        
        # Título
        titulo = ctk.CTkLabel(
            dialogo,
            text="➕ Crear Nuevo Evento",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        titulo.pack(pady=20)
        
        # Frame formulario
        frame_form = ctk.CTkScrollableFrame(dialogo)
        frame_form.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Tipo de evento
        label_tipo = ctk.CTkLabel(frame_form, text="Tipo de Evento:", anchor="w")
        label_tipo.pack(pady=(10, 5), padx=10, fill="x")
        
        combo_tipo = ctk.CTkComboBox(
            frame_form,
            values=Evento.TIPOS_VALIDOS,
            width=400
        )
        combo_tipo.pack(pady=5, padx=10)
        combo_tipo.set(Evento.TIPOS_VALIDOS[0])
        
        # Fecha
        label_fecha = ctk.CTkLabel(frame_form, text="Fecha (DD/MM/YYYY):", anchor="w")
        label_fecha.pack(pady=(10, 5), padx=10, fill="x")
        
        entry_fecha = ctk.CTkEntry(frame_form, width=400, placeholder_text="Ej: 05/02/2026")
        entry_fecha.pack(pady=5, padx=10)
        entry_fecha.insert(0, datetime.now().strftime("%d/%m/%Y"))
        
        # Hora inicio
        label_hora = ctk.CTkLabel(frame_form, text="Hora de Inicio (HH:MM):", anchor="w")
        label_hora.pack(pady=(10, 5), padx=10, fill="x")
        
        entry_hora = ctk.CTkEntry(frame_form, width=400, placeholder_text="Ej: 10:00")
        entry_hora.pack(pady=5, padx=10)
        entry_hora.insert(0, "10:00")
        
        # Duración
        label_duracion = ctk.CTkLabel(frame_form, text="Duración (minutos):", anchor="w")
        label_duracion.pack(pady=(10, 5), padx=10, fill="x")
        
        entry_duracion = ctk.CTkEntry(frame_form, width=400, placeholder_text="Ej: 30")
        entry_duracion.pack(pady=5, padx=10)
        entry_duracion.insert(0, "30")
        
        # Recursos
        label_recursos = ctk.CTkLabel(frame_form, text="Seleccionar Recursos:", anchor="w")
        label_recursos.pack(pady=(20, 5), padx=10, fill="x")
        
        # Frame para checkboxes de recursos
        frame_checks = ctk.CTkFrame(frame_form)
        frame_checks.pack(pady=5, padx=10, fill="both", expand=True)
        
        # Variables para checkboxes
        vars_recursos = {}
        
        # Espacios
        label_espacios = ctk.CTkLabel(frame_checks, text="🏢 Espacios:", font=ctk.CTkFont(weight="bold"))
        label_espacios.pack(anchor="w", pady=5)
        
        for espacio in self.controlador.obtener_espacios():
            var = ctk.BooleanVar()
            check = ctk.CTkCheckBox(frame_checks, text=espacio.nombre, variable=var)
            check.pack(anchor="w", padx=20, pady=2)
            vars_recursos[espacio.id] = var
        
        # Personal
        label_personal = ctk.CTkLabel(frame_checks, text="👥 Personal:", font=ctk.CTkFont(weight="bold"))
        label_personal.pack(anchor="w", pady=5)
        
        for persona in self.controlador.obtener_personal():
            var = ctk.BooleanVar()
            check = ctk.CTkCheckBox(frame_checks, text=f"{persona.nombre} ({persona.rol})", variable=var)
            check.pack(anchor="w", padx=20, pady=2)
            vars_recursos[persona.id] = var
        
        # Perros
        label_perros = ctk.CTkLabel(frame_checks, text="🐕 Perros:", font=ctk.CTkFont(weight="bold"))
        label_perros.pack(anchor="w", pady=5)
        
        for perro in self.controlador.obtener_perros():
            var = ctk.BooleanVar()
            check = ctk.CTkCheckBox(
                frame_checks, 
                text=f"{perro.nombre} ({perro.temperamento})", 
                variable=var
            )
            check.pack(anchor="w", padx=20, pady=2)
            vars_recursos[perro.id] = var
        
        # Descripción
        label_desc = ctk.CTkLabel(frame_form, text="Descripción (opcional):", anchor="w")
        label_desc.pack(pady=(10, 5), padx=10, fill="x")
        
        entry_desc = ctk.CTkEntry(frame_form, width=400, placeholder_text="Descripción del evento")
        entry_desc.pack(pady=5, padx=10)
        
        # Botones
        frame_botones = ctk.CTkFrame(dialogo, fg_color="transparent")
        frame_botones.pack(pady=20)
        
        def crear():
            try:
                # Obtener valores
                tipo = combo_tipo.get()
                fecha_str = entry_fecha.get()
                hora_str = entry_hora.get()
                duracion = int(entry_duracion.get())
                descripcion = entry_desc.get()
                
                # Parsear fecha y hora
                fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()
                hora = datetime.strptime(hora_str, "%H:%M").time()
                inicio = datetime.combine(fecha, hora)
                fin = inicio + timedelta(minutes=duracion)
                
                # Obtener recursos seleccionados
                recursos_ids = [rid for rid, var in vars_recursos.items() if var.get()]
                
                if not recursos_ids:
                    messagebox.showwarning("Advertencia", "Debe seleccionar al menos un recurso")
                    return
                
                # Crear evento
                exito, mensaje, evento = self.controlador.crear_evento(
                    tipo, recursos_ids, inicio, fin, descripcion
                )
                
                if exito:
                    messagebox.showinfo("Éxito", mensaje)
                    dialogo.destroy()
                    self.mostrar_eventos()
                else:
                    messagebox.showerror("Error", mensaje)
            
            except ValueError as e:
                messagebox.showerror("Error", f"Datos inválidos: {str(e)}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al crear evento: {str(e)}")
        
        btn_crear = ctk.CTkButton(
            frame_botones,
            text="✅ Crear Evento",
            command=crear,
            width=150,
            height=35,
            fg_color="green",
            hover_color="darkgreen"
        )
        btn_crear.pack(side="left", padx=10)
        
        btn_cancelar = ctk.CTkButton(
            frame_botones,
            text="❌ Cancelar",
            command=dialogo.destroy,
            width=150,
            height=35
        )
        btn_cancelar.pack(side="left", padx=10)
    
    def eliminar_evento(self, evento_id):
        """Elimina un evento"""
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este evento?"):
            exito, mensaje = self.controlador.eliminar_evento(evento_id)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self.mostrar_eventos()
            else:
                messagebox.showerror("Error", mensaje)
    
    # ========== PANTALLA RECURSOS ==========
    
    def mostrar_recursos(self):
        """Muestra la pantalla de gestión de recursos"""
        self.limpiar_panel_principal()
        
        # Título
        titulo = ctk.CTkLabel(
            self.panel_principal,
            text="📦 Gestión de Recursos",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        titulo.pack(pady=20)
        
        # Botones para agregar
        frame_botones = ctk.CTkFrame(self.panel_principal, fg_color="transparent")
        frame_botones.pack(pady=10)
        
        btn_agregar_perro = ctk.CTkButton(
            frame_botones,
            text="➕ Agregar Perro",
            command=self.mostrar_dialogo_agregar_perro,
            width=150,
            height=35,
            fg_color="green"
        )
        btn_agregar_perro.pack(side="left", padx=5)
        
        btn_agregar_espacio = ctk.CTkButton(
            frame_botones,
            text="➕ Agregar Espacio",
            command=self.mostrar_dialogo_agregar_espacio,
            width=150,
            height=35,
            fg_color="green"
        )
        btn_agregar_espacio.pack(side="left", padx=5)
        
        btn_agregar_personal = ctk.CTkButton(
            frame_botones,
            text="➕ Agregar Personal",
            command=self.mostrar_dialogo_agregar_personal,
            width=150,
            height=35,
            fg_color="green"
        )
        btn_agregar_personal.pack(side="left", padx=5)
        
        # Tabs para cada tipo de recurso
        tabview = ctk.CTkTabview(self.panel_principal)
        tabview.pack(pady=10, padx=40, fill="both", expand=True)
        
        # Tab Perros
        tab_perros = tabview.add("🐕 Perros")
        self.mostrar_lista_perros(tab_perros)
        
        # Tab Espacios
        tab_espacios = tabview.add("🏢 Espacios")
        self.mostrar_lista_espacios(tab_espacios)
        
        # Tab Personal
        tab_personal = tabview.add("👥 Personal")
        self.mostrar_lista_personal(tab_personal)
    
    def mostrar_lista_perros(self, parent):
        """Muestra la lista de perros"""
        frame = ctk.CTkScrollableFrame(parent)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        perros = self.controlador.obtener_perros()
        
        if perros:
            for perro in perros:
                frame_perro = ctk.CTkFrame(frame, corner_radius=10)
                frame_perro.pack(pady=5, padx=5, fill="x")
                
                texto = f"🐕 {perro.nombre} - {perro.raza} ({perro.tamano}, {perro.temperamento})"
                if perro.edad:
                    texto += f" - {perro.edad} años"
                
                label = ctk.CTkLabel(frame_perro, text=texto, anchor="w")
                label.pack(side="left", padx=20, pady=15, fill="x", expand=True)
                
                btn_eliminar = ctk.CTkButton(
                    frame_perro,
                    text="🗑️",
                    command=lambda p=perro: self.eliminar_recurso(p.id),
                    width=50,
                    height=30,
                    fg_color="red"
                )
                btn_eliminar.pack(side="right", padx=10)
        else:
            label = ctk.CTkLabel(frame, text="No hay perros registrados")
            label.pack(pady=50)
    
    def mostrar_lista_espacios(self, parent):
        """Muestra la lista de espacios"""
        frame = ctk.CTkScrollableFrame(parent)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        espacios = self.controlador.obtener_espacios()
        
        if espacios:
            for espacio in espacios:
                frame_esp = ctk.CTkFrame(frame, corner_radius=10)
                frame_esp.pack(pady=5, padx=5, fill="x")
                
                texto = f"🏢 {espacio.nombre}"
                if espacio.descripcion:
                    texto += f" - {espacio.descripcion}"
                
                label = ctk.CTkLabel(frame_esp, text=texto, anchor="w")
                label.pack(side="left", padx=20, pady=15, fill="x", expand=True)
                
                btn_eliminar = ctk.CTkButton(
                    frame_esp,
                    text="🗑️",
                    command=lambda e=espacio: self.eliminar_recurso(e.id),
                    width=50,
                    height=30,
                    fg_color="red"
                )
                btn_eliminar.pack(side="right", padx=10)
        else:
            label = ctk.CTkLabel(frame, text="No hay espacios registrados")
            label.pack(pady=50)
    
    def mostrar_lista_personal(self, parent):
        """Muestra la lista de personal"""
        frame = ctk.CTkScrollableFrame(parent)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        personal = self.controlador.obtener_personal()
        
        if personal:
            for persona in personal:
                frame_per = ctk.CTkFrame(frame, corner_radius=10)
                frame_per.pack(pady=5, padx=5, fill="x")
                
                texto = f"👥 {persona.nombre} - {persona.rol.capitalize()}"
                if persona.telefono:
                    texto += f" - {persona.telefono}"
                
                label = ctk.CTkLabel(frame_per, text=texto, anchor="w")
                label.pack(side="left", padx=20, pady=15, fill="x", expand=True)
                
                btn_eliminar = ctk.CTkButton(
                    frame_per,
                    text="🗑️",
                    command=lambda p=persona: self.eliminar_recurso(p.id),
                    width=50,
                    height=30,
                    fg_color="red"
                )
                btn_eliminar.pack(side="right", padx=10)
        else:
            label = ctk.CTkLabel(frame, text="No hay personal registrado")
            label.pack(pady=50)
    
    def mostrar_dialogo_agregar_perro(self):
        """Muestra diálogo para agregar perro"""
        from perro import Perro
        
        dialogo = ctk.CTkToplevel(self)
        dialogo.title("Agregar Perro")
        dialogo.geometry("500x600")
        dialogo.grab_set()
        
        # Título
        titulo = ctk.CTkLabel(dialogo, text="🐕 Agregar Nuevo Perro", font=ctk.CTkFont(size=20, weight="bold"))
        titulo.pack(pady=20)
        
        # Formulario
        frame_form = ctk.CTkFrame(dialogo)
        frame_form.pack(pady=10, padx=30, fill="both", expand=True)
        
        # ID
        label_id = ctk.CTkLabel(frame_form, text="ID único:", anchor="w")
        label_id.pack(pady=(10, 5), padx=10, fill="x")
        entry_id = ctk.CTkEntry(frame_form, placeholder_text="Ej: perro_001")
        entry_id.pack(pady=5, padx=10, fill="x")
        
        # Nombre
        label_nombre = ctk.CTkLabel(frame_form, text="Nombre:", anchor="w")
        label_nombre.pack(pady=(10, 5), padx=10, fill="x")
        entry_nombre = ctk.CTkEntry(frame_form, placeholder_text="Ej: Max")
        entry_nombre.pack(pady=5, padx=10, fill="x")
        
        # Raza
        label_raza = ctk.CTkLabel(frame_form, text="Raza:", anchor="w")
        label_raza.pack(pady=(10, 5), padx=10, fill="x")
        entry_raza = ctk.CTkEntry(frame_form, placeholder_text="Ej: Pastor Alemán")
        entry_raza.pack(pady=5, padx=10, fill="x")
        entry_raza.insert(0, "Mestizo")
        
        # Tamaño
        label_tamano = ctk.CTkLabel(frame_form, text="Tamaño:", anchor="w")
        label_tamano.pack(pady=(10, 5), padx=10, fill="x")
        combo_tamano = ctk.CTkComboBox(frame_form, values=Perro.TAMANOS_VALIDOS)
        combo_tamano.pack(pady=5, padx=10, fill="x")
        combo_tamano.set("mediano")
        
        # Temperamento
        label_temp = ctk.CTkLabel(frame_form, text="Temperamento:", anchor="w")
        label_temp.pack(pady=(10, 5), padx=10, fill="x")
        combo_temp = ctk.CTkComboBox(frame_form, values=Perro.TEMPERAMENTOS_VALIDOS)
        combo_temp.pack(pady=5, padx=10, fill="x")
        combo_temp.set("social")
        
        # Edad
        label_edad = ctk.CTkLabel(frame_form, text="Edad (años, opcional):", anchor="w")
        label_edad.pack(pady=(10, 5), padx=10, fill="x")
        entry_edad = ctk.CTkEntry(frame_form, placeholder_text="Ej: 3")
        entry_edad.pack(pady=5, padx=10, fill="x")
        
        # Botones
        frame_botones = ctk.CTkFrame(dialogo, fg_color="transparent")
        frame_botones.pack(pady=20)
        
        def guardar():
            try:
                id_perro = entry_id.get().strip()
                nombre = entry_nombre.get().strip()
                raza = entry_raza.get().strip()
                tamano = combo_tamano.get()
                temp = combo_temp.get()
                edad_str = entry_edad.get().strip()
                edad = int(edad_str) if edad_str else None
                
                if not id_perro or not nombre:
                    messagebox.showwarning("Advertencia", "ID y Nombre son obligatorios")
                    return
                
                exito, mensaje = self.controlador.agregar_perro(id_perro, nombre, tamano, temp, raza, edad)
                
                if exito:
                    messagebox.showinfo("Éxito", mensaje)
                    dialogo.destroy()
                    self.mostrar_recursos()
                else:
                    messagebox.showerror("Error", mensaje)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        btn_guardar = ctk.CTkButton(frame_botones, text="✅ Guardar", command=guardar, width=120, fg_color="green")
        btn_guardar.pack(side="left", padx=10)
        
        btn_cancelar = ctk.CTkButton(frame_botones, text="❌ Cancelar", command=dialogo.destroy, width=120)
        btn_cancelar.pack(side="left", padx=10)
    
    def mostrar_dialogo_agregar_espacio(self):
        """Muestra diálogo para agregar espacio"""
        dialogo = ctk.CTkToplevel(self)
        dialogo.title("Agregar Espacio")
        dialogo.geometry("500x450")
        dialogo.grab_set()
        
        titulo = ctk.CTkLabel(dialogo, text="🏢 Agregar Nuevo Espacio", font=ctk.CTkFont(size=20, weight="bold"))
        titulo.pack(pady=20)
        
        frame_form = ctk.CTkFrame(dialogo)
        frame_form.pack(pady=10, padx=30, fill="both", expand=True)
        
        label_id = ctk.CTkLabel(frame_form, text="ID único:", anchor="w")
        label_id.pack(pady=(10, 5), padx=10, fill="x")
        entry_id = ctk.CTkEntry(frame_form, placeholder_text="Ej: sala_001")
        entry_id.pack(pady=5, padx=10, fill="x")
        
        label_nombre = ctk.CTkLabel(frame_form, text="Nombre:", anchor="w")
        label_nombre.pack(pady=(10, 5), padx=10, fill="x")
        entry_nombre = ctk.CTkEntry(frame_form, placeholder_text="Ej: Sala de Adopción 1")
        entry_nombre.pack(pady=5, padx=10, fill="x")
        
        label_desc = ctk.CTkLabel(frame_form, text="Descripción (opcional):", anchor="w")
        label_desc.pack(pady=(10, 5), padx=10, fill="x")
        entry_desc = ctk.CTkEntry(frame_form, placeholder_text="Descripción del espacio")
        entry_desc.pack(pady=5, padx=10, fill="x")
        
        frame_botones = ctk.CTkFrame(dialogo, fg_color="transparent")
        frame_botones.pack(pady=20)
        
        def guardar():
            try:
                id_esp = entry_id.get().strip()
                nombre = entry_nombre.get().strip()
                desc = entry_desc.get().strip()
                
                if not id_esp or not nombre:
                    messagebox.showwarning("Advertencia", "ID y Nombre son obligatorios")
                    return
                
                exito, mensaje = self.controlador.agregar_espacio(id_esp, nombre, 1, desc)
                
                if exito:
                    messagebox.showinfo("Éxito", mensaje)
                    dialogo.destroy()
                    self.mostrar_recursos()
                else:
                    messagebox.showerror("Error", mensaje)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        btn_guardar = ctk.CTkButton(frame_botones, text="✅ Guardar", command=guardar, width=120, fg_color="green")
        btn_guardar.pack(side="left", padx=10)
        
        btn_cancelar = ctk.CTkButton(frame_botones, text="❌ Cancelar", command=dialogo.destroy, width=120)
        btn_cancelar.pack(side="left", padx=10)
    
    def mostrar_dialogo_agregar_personal(self):
        """Muestra diálogo para agregar personal"""
        from recurso import Personal
        
        dialogo = ctk.CTkToplevel(self)
        dialogo.title("Agregar Personal")
        dialogo.geometry("500x550")
        dialogo.grab_set()
        
        titulo = ctk.CTkLabel(dialogo, text="👥 Agregar Nuevo Personal", font=ctk.CTkFont(size=20, weight="bold"))
        titulo.pack(pady=20)
        
        frame_form = ctk.CTkFrame(dialogo)
        frame_form.pack(pady=10, padx=30, fill="both", expand=True)
        
        label_id = ctk.CTkLabel(frame_form, text="ID único:", anchor="w")
        label_id.pack(pady=(10, 5), padx=10, fill="x")
        entry_id = ctk.CTkEntry(frame_form, placeholder_text="Ej: vet_001")
        entry_id.pack(pady=5, padx=10, fill="x")
        
        label_nombre = ctk.CTkLabel(frame_form, text="Nombre:", anchor="w")
        label_nombre.pack(pady=(10, 5), padx=10, fill="x")
        entry_nombre = ctk.CTkEntry(frame_form, placeholder_text="Ej: Dr. Juan Pérez")
        entry_nombre.pack(pady=5, padx=10, fill="x")
        
        label_rol = ctk.CTkLabel(frame_form, text="Rol:", anchor="w")
        label_rol.pack(pady=(10, 5), padx=10, fill="x")
        combo_rol = ctk.CTkComboBox(frame_form, values=Personal.ROLES_VALIDOS)
        combo_rol.pack(pady=5, padx=10, fill="x")
        combo_rol.set("veterinario")
        
        label_tel = ctk.CTkLabel(frame_form, text="Teléfono (opcional):", anchor="w")
        label_tel.pack(pady=(10, 5), padx=10, fill="x")
        entry_tel = ctk.CTkEntry(frame_form, placeholder_text="Ej: 555-1234")
        entry_tel.pack(pady=5, padx=10, fill="x")
        
        frame_botones = ctk.CTkFrame(dialogo, fg_color="transparent")
        frame_botones.pack(pady=20)
        
        def guardar():
            try:
                id_per = entry_id.get().strip()
                nombre = entry_nombre.get().strip()
                rol = combo_rol.get()
                tel = entry_tel.get().strip()
                
                if not id_per or not nombre:
                    messagebox.showwarning("Advertencia", "ID y Nombre son obligatorios")
                    return
                
                exito, mensaje = self.controlador.agregar_personal(id_per, nombre, rol, tel)
                
                if exito:
                    messagebox.showinfo("Éxito", mensaje)
                    dialogo.destroy()
                    self.mostrar_recursos()
                else:
                    messagebox.showerror("Error", mensaje)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        btn_guardar = ctk.CTkButton(frame_botones, text="✅ Guardar", command=guardar, width=120, fg_color="green")
        btn_guardar.pack(side="left", padx=10)
        
        btn_cancelar = ctk.CTkButton(frame_botones, text="❌ Cancelar", command=dialogo.destroy, width=120)
        btn_cancelar.pack(side="left", padx=10)
    
    def eliminar_recurso(self, recurso_id):
        """Elimina un recurso"""
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este recurso?"):
            exito, mensaje = self.controlador.eliminar_recurso(recurso_id)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self.mostrar_recursos()
            else:
                messagebox.showerror("Error", mensaje)
    
    # ========== PANTALLA BUSCAR HUECO ==========
    
    def mostrar_buscar_hueco(self):
        """Muestra la pantalla de búsqueda de huecos"""
        self.limpiar_panel_principal()
        
        titulo = ctk.CTkLabel(
            self.panel_principal,
            text="🔍 Buscar Hueco Disponible",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        titulo.pack(pady=20)
        
        frame_form = ctk.CTkFrame(self.panel_principal)
        frame_form.pack(pady=20, padx=100, fill="both", expand=True)
        
        # Duración
        label_duracion = ctk.CTkLabel(frame_form, text="Duración del evento (minutos):", anchor="w")
        label_duracion.pack(pady=(20, 5), padx=20, fill="x")
        
        entry_duracion = ctk.CTkEntry(frame_form, placeholder_text="Ej: 30")
        entry_duracion.pack(pady=5, padx=20, fill="x")
        entry_duracion.insert(0, "30")
        
        # Recursos
        label_recursos = ctk.CTkLabel(frame_form, text="Seleccionar Recursos:", anchor="w")
        label_recursos.pack(pady=(20, 10), padx=20, fill="x")
        
        frame_checks = ctk.CTkScrollableFrame(frame_form, height=300)
        frame_checks.pack(pady=5, padx=20, fill="both", expand=True)
        
        vars_recursos = {}
        
        # Espacios
        label_esp = ctk.CTkLabel(frame_checks, text="🏢 Espacios:", font=ctk.CTkFont(weight="bold"))
        label_esp.pack(anchor="w", pady=5)
        for espacio in self.controlador.obtener_espacios():
            var = ctk.BooleanVar()
            check = ctk.CTkCheckBox(frame_checks, text=espacio.nombre, variable=var)
            check.pack(anchor="w", padx=20, pady=2)
            vars_recursos[espacio.id] = var
        
        # Personal
        label_per = ctk.CTkLabel(frame_checks, text="👥 Personal:", font=ctk.CTkFont(weight="bold"))
        label_per.pack(anchor="w", pady=5)
        for persona in self.controlador.obtener_personal():
            var = ctk.BooleanVar()
            check = ctk.CTkCheckBox(frame_checks, text=f"{persona.nombre} ({persona.rol})", variable=var)
            check.pack(anchor="w", padx=20, pady=2)
            vars_recursos[persona.id] = var
        
        # Perros
        label_perro = ctk.CTkLabel(frame_checks, text="🐕 Perros:", font=ctk.CTkFont(weight="bold"))
        label_perro.pack(anchor="w", pady=5)
        for perro in self.controlador.obtener_perros():
            var = ctk.BooleanVar()
            check = ctk.CTkCheckBox(frame_checks, text=perro.nombre, variable=var)
            check.pack(anchor="w", padx=20, pady=2)
            vars_recursos[perro.id] = var
        
        # Resultado
        frame_resultado = ctk.CTkFrame(frame_form)
        frame_resultado.pack(pady=20, padx=20, fill="x")
        
        label_resultado = ctk.CTkLabel(
            frame_resultado, 
            text="", 
            font=ctk.CTkFont(size=14),
            wraplength=600
        )
        label_resultado.pack(pady=20)
        
        # Botón buscar
        def buscar():
            try:
                duracion = int(entry_duracion.get())
                recursos_ids = [rid for rid, var in vars_recursos.items() if var.get()]
                
                if not recursos_ids:
                    messagebox.showwarning("Advertencia", "Debe seleccionar al menos un recurso")
                    return
                
                inicio, fin = self.controlador.buscar_hueco_disponible(recursos_ids, duracion)
                
                if inicio:
                    texto = f"✅ Hueco encontrado!\n\n"
                    texto += f"📅 Fecha: {inicio.strftime('%d/%m/%Y')}\n"
                    texto += f"🕐 Horario: {inicio.strftime('%H:%M')} - {fin.strftime('%H:%M')}\n"
                    texto += f"⏱️ Duración: {duracion} minutos"
                    label_resultado.configure(text=texto, text_color="green")
                else:
                    texto = "❌ No se encontraron huecos disponibles\nen los próximos 7 días"
                    label_resultado.configure(text=texto, text_color="red")
            
            except ValueError:
                messagebox.showerror("Error", "Duración inválida")
            except Exception as e:
                messagebox.showerror("Error", f"Error al buscar: {str(e)}")
        
        btn_buscar = ctk.CTkButton(
            frame_form,
            text="🔍 Buscar Hueco",
            command=buscar,
            height=40,
            font=ctk.CTkFont(size=14),
            fg_color="green",
            hover_color="darkgreen"
        )
        btn_buscar.pack(pady=10, padx=20, fill="x")
    
    # ========== UTILIDADES ==========
    
    def cargar_datos_iniciales(self):
        """Carga los datos al iniciar"""
        exito, mensaje = self.controlador.cargar_datos()
        if not exito:
            # Si no hay datos, crear datos de ejemplo
            if messagebox.askyesno(
                "Datos no encontrados",
                "¿Desea crear datos de ejemplo para comenzar?"
            ):
                self.controlador.crear_datos_ejemplo()
                messagebox.showinfo("Éxito", "Datos de ejemplo creados")
    
    def guardar_datos(self):
        """Guarda los datos"""
        exito, mensaje = self.controlador.guardar_datos()
        if exito:
            messagebox.showinfo("Éxito", mensaje)
        else:
            messagebox.showerror("Error", mensaje)

    def salir(self):
        """Cierra la aplicación"""
        self.quit()