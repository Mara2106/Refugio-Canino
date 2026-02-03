from datetime import datetime, timedelta

class Evento:
    """Representa un evento en el refugio"""
    
    # Tipos de eventos válidos
    TIPOS_VALIDOS = [
        "Chequeo Veterinario",
        "Vacunación",
        "Cirugía",
        "Sesión de Entrenamiento",
        "Socialización",
        "Baño y Aseo",
        "Adopción",
        "Paseo"
    ]
    
    def __init__(self, id, tipo, recursos_ids, inicio, fin, descripcion=""):
        """
        Inicializa un evento
        
        Args:
            id (str): Identificador único del evento
            tipo (str): Tipo de evento
            recursos_ids (list): Lista de IDs de recursos necesarios
            inicio (datetime): Fecha y hora de inicio
            fin (datetime): Fecha y hora de fin
            descripcion (str): Descripción opcional del evento
        """
        self.id = id
        self.tipo = tipo
        self.recursos_ids = recursos_ids
        self.inicio = inicio
        self.fin = fin
        self.descripcion = descripcion
        
        # Validar tipo
        if tipo not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo de evento inválido. Debe ser uno de: {', '.join(self.TIPOS_VALIDOS)}")
        
        # Validar fechas
        if inicio >= fin:
            raise ValueError("La fecha de inicio debe ser anterior a la fecha de fin")
    
    def duracion_minutos(self):
        """Retorna la duración del evento en minutos"""
        return int((self.fin - self.inicio).total_seconds() / 60)
    
    def __str__(self):
        return f"{self.tipo} - {self.inicio.strftime('%d/%m/%Y %H:%M')}"
    
    def __repr__(self):
        return f"Evento(id='{self.id}', tipo='{self.tipo}', inicio='{self.inicio}')"
    
    def to_dict(self):
        """Convierte el evento a diccionario para JSON"""
        return {
            'id': self.id,
            'tipo': self.tipo,
            'recursos_ids': self.recursos_ids,
            'inicio': self.inicio.isoformat(),
            'fin': self.fin.isoformat(),
            'descripcion': self.descripcion
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea un evento desde un diccionario"""
        return cls(
            id=data['id'],
            tipo=data['tipo'],
            recursos_ids=data['recursos_ids'],
            inicio=datetime.fromisoformat(data['inicio']),
            fin=datetime.fromisoformat(data['fin']),
            descripcion=data.get('descripcion', '')
        )


class ValidadorEventos:
    """Valida eventos según las restricciones del refugio"""
    
    def __init__(self, inventario):
        """
        Inicializa el validador
        
        Args:
            inventario: Instancia de InventarioRecursos
        """
        self.inventario = inventario
    
    def validar_evento(self, evento, eventos_existentes):
        """
        Valida un evento completo
        
        Args:
            evento: Evento a validar
            eventos_existentes: Lista de eventos ya planificados
        
        Returns:
            tuple: (es_valido, mensaje_error)
        """
        # 1. Validar que los recursos existan
        valido, mensaje = self._validar_recursos_existen(evento)
        if not valido:
            return False, mensaje
        
        # 2. Validar conflictos de horario
        valido, mensaje = self._validar_conflictos_horario(evento, eventos_existentes)
        if not valido:
            return False, mensaje
        
        # 3. Validar co-requisitos
        valido, mensaje = self._validar_co_requisitos(evento)
        if not valido:
            return False, mensaje
        
        # 4. Validar exclusiones mutuas
        valido, mensaje = self._validar_exclusiones_mutuas(evento)
        if not valido:
            return False, mensaje
        
        # 5. Validar restricciones de perros
        valido, mensaje = self._validar_restricciones_perros(evento)
        if not valido:
            return False, mensaje
        
        return True, "Evento válido"
    
    def _validar_recursos_existen(self, evento):
        """Verifica que todos los recursos existan"""
        for recurso_id in evento.recursos_ids:
            if self.inventario.obtener_recurso(recurso_id) is None:
                return False, f"El recurso '{recurso_id}' no existe en el inventario"
        return True, ""
    
    def _validar_conflictos_horario(self, evento, eventos_existentes):
        """Verifica que no haya conflictos de horario"""
        for evt_existente in eventos_existentes:
            # Ignorar el mismo evento (útil para actualizaciones)
            if evt_existente.id == evento.id:
                continue
            
            if self._intervalos_se_solapan(evento.inicio, evento.fin, evt_existente.inicio, evt_existente.fin):
                # Verificar si comparten recursos
                recursos_compartidos = set(evento.recursos_ids) & set(evt_existente.recursos_ids)
                if recursos_compartidos:
                    nombres = [self.inventario.obtener_recurso(r).nombre for r in recursos_compartidos]
                    return False, f"Conflicto: {', '.join(nombres)} ya ocupado(s) en ese horario"
        return True, ""
    
    def _validar_co_requisitos(self, evento):
        """Valida restricciones de co-requisitos"""
        recursos = [self.inventario.obtener_recurso(rid) for rid in evento.recursos_ids]
        
        # CO-REQUISITO 1: Eventos veterinarios requieren veterinario + sala médica
        if evento.tipo in ["Chequeo Veterinario", "Vacunación", "Cirugía"]:
            tiene_veterinario = any(hasattr(r, 'rol') and r.rol == "veterinario" for r in recursos)
            tiene_sala_medica = any(hasattr(r, 'nombre') and ("médica" in r.nombre.lower() or "medica" in r.nombre.lower()) 
                                   for r in recursos)
            
            if not tiene_veterinario:
                return False, f"'{evento.tipo}' requiere un veterinario"
            if not tiene_sala_medica:
                return False, f"'{evento.tipo}' requiere una sala médica"
        
        # CO-REQUISITO 2: Socialización requiere área + supervisor
        if evento.tipo == "Socialización":
            tiene_area = any(hasattr(r, 'nombre') and "socialización" in r.nombre.lower() for r in recursos)
            tiene_supervisor = any(hasattr(r, 'puede_supervisar_socializacion') and r.puede_supervisar_socializacion() for r in recursos)
            
            if not tiene_area:
                return False, "Socialización requiere un área de socialización"
            if not tiene_supervisor:
                return False, "Socialización requiere un supervisor (entrenador/voluntario)"
        
        # CO-REQUISITO 3: Adopción requiere sala + perro + voluntario
        if evento.tipo == "Adopción":
            tiene_sala = any(hasattr(r, 'nombre') and "adopción" in r.nombre.lower() for r in recursos)
            tiene_perro = any(hasattr(r, 'temperamento') for r in recursos)
            tiene_voluntario = any(hasattr(r, 'rol') and r.rol == "voluntario" for r in recursos)
            
            if not tiene_sala:
                return False, "Adopción requiere una sala de adopción"
            if not tiene_perro:
                return False, "Adopción requiere un perro"
            if not tiene_voluntario:
                return False, "Adopción requiere un voluntario coordinador"
        
        # CO-REQUISITO 4: Baño requiere sala + groomer
        if evento.tipo == "Baño y Aseo":
            tiene_sala = any(hasattr(r, 'nombre') and "aseo" in r.nombre.lower() for r in recursos)
            tiene_groomer = any(hasattr(r, 'rol') and r.rol == "groomer" for r in recursos)
            
            if not tiene_sala:
                return False, "Baño y Aseo requiere una sala de aseo"
            if not tiene_groomer:
                return False, "Baño y Aseo requiere un groomer"
        
        return True, ""
    
    def _validar_exclusiones_mutuas(self, evento):
        """Valida restricciones de exclusión mutua"""
        recursos = [self.inventario.obtener_recurso(rid) for rid in evento.recursos_ids]
        
        # EXCLUSIÓN 1: No múltiples perros dominantes en socialización
        if evento.tipo == "Socialización":
            perros = [r for r in recursos if hasattr(r, 'temperamento')]
            perros_dominantes = [p for p in perros if p.es_dominante()]
            
            if len(perros_dominantes) > 1:
                nombres = [p.nombre for p in perros_dominantes]
                return False, f"No se permiten múltiples perros dominantes/agresivos: {', '.join(nombres)}"
        
        # EXCLUSIÓN 2: Perros recién vacunados no pueden socializar (24h)
        if evento.tipo == "Socialización":
            perros = [r for r in recursos if hasattr(r, 'temperamento')]
            for perro in perros:
                if not perro.esta_disponible_para_socializacion():
                    horas = int((datetime.now() - perro.ultima_vacuna).total_seconds() / 3600)
                    return False, f"{perro.nombre} fue vacunado hace {horas}h. Debe esperar 24h"
        
        return True, ""
    
    def _validar_restricciones_perros(self, evento):
        """Validaciones específicas de perros"""
        recursos = [self.inventario.obtener_recurso(rid) for rid in evento.recursos_ids]
        perros = [r for r in recursos if hasattr(r, 'temperamento')]
        
        # Eventos que requieren perros
        eventos_con_perros = ["Chequeo Veterinario", "Vacunación", "Cirugía", "Socialización", "Baño y Aseo", "Adopción", "Paseo"]
        
        if evento.tipo in eventos_con_perros and len(perros) == 0:
            return False, f"'{evento.tipo}' requiere al menos un perro"
        
        # Socialización requiere al menos 2 perros
        if evento.tipo == "Socialización" and len(perros) < 2:
            return False, "Socialización requiere al menos 2 perros"
        
        return True, ""
    
    def _intervalos_se_solapan(self, inicio1, fin1, inicio2, fin2):
        """Verifica si dos intervalos se solapan"""
        return inicio1 < fin2 and inicio2 < fin1


class BuscadorHuecos:
    """Busca huecos disponibles en el calendario"""
    
    def __init__(self, eventos, validador):
        """
        Inicializa el buscador
        
        Args:
            eventos: Lista de eventos existentes
            validador: Instancia de ValidadorEventos
        """
        self.eventos = eventos
        self.validador = validador
    
    def buscar_primer_hueco(self, recursos_ids, duracion_minutos, desde=None, dias_buscar=7,hora_inicio="08:00", hora_fin="18:00"):
        """
        Busca el primer hueco disponible
        
        Args:
            recursos_ids: Lista de IDs de recursos necesarios
            duracion_minutos: Duración del evento
            desde: Fecha desde donde buscar (None = ahora)
            dias_buscar: Días hacia adelante
            hora_inicio: Hora inicio del día
            hora_fin: Hora fin del día
        
        Returns:
            tuple: (inicio, fin) o (None, None)
        """
        if desde is None:
            desde = datetime.now()
        
        # Redondear al siguiente intervalo de 30 min
        minutos = desde.minute
        if minutos % 30 != 0:
            desde = desde.replace(minute=(minutos // 30 + 1) * 30, second=0, microsecond=0)
        
        hasta = desde + timedelta(days=dias_buscar)
        duracion = timedelta(minutes=duracion_minutos)
        incremento = timedelta(minutes=30)
        
        # Parsear horas
        h_inicio = datetime.strptime(hora_inicio, "%H:%M").time()
        h_fin = datetime.strptime(hora_fin, "%H:%M").time()
        
        fecha_actual = desde.date()
        
        while fecha_actual <= hasta.date():
            hora_dia_inicio = datetime.combine(fecha_actual, h_inicio)
            hora_dia_fin = datetime.combine(fecha_actual, h_fin)
            
            # Ajustar si es el día actual
            if fecha_actual == desde.date() and desde > hora_dia_inicio:
                hora_busqueda = desde
            else:
                hora_busqueda = hora_dia_inicio
            
            # Buscar en este día
            while hora_busqueda + duracion <= hora_dia_fin:
                fin_propuesto = hora_busqueda + duracion
                
                if self._horario_esta_libre(recursos_ids, hora_busqueda, fin_propuesto):
                    return hora_busqueda, fin_propuesto
                
                hora_busqueda += incremento
            
            fecha_actual += timedelta(days=1)
        
        return None, None
    
    def _horario_esta_libre(self, recursos_ids, inicio, fin):
        """Verifica si los recursos están libres en el horario"""
        for evento in self.eventos:
            # Verificar solapamiento
            if inicio < evento.fin and evento.inicio < fin:
                # Verificar si hay recursos compartidos
                if set(recursos_ids) & set(evento.recursos_ids):
                    return False
        return True
