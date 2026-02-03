import json
from datetime import datetime, timedelta
from perro import Perro
from recurso import Espacio, Personal, InventarioRecursos
from evento import Evento, ValidadorEventos, BuscadorHuecos

class ControladorRefugio:
    """Controlador principal del sistema"""
    
    def __init__(self):
        """Inicializa el controlador"""
        self.inventario = InventarioRecursos()
        self.eventos = []
        self.validador = ValidadorEventos(self.inventario)
        self.buscador = BuscadorHuecos(self.eventos, self.validador)
        self._contador_eventos = 1
        self.archivo_datos = "refugio_datos.json"
    
    # ========== GESTIÓN DE RECURSOS ==========
    
    def agregar_perro(self, id, nombre, tamano, temperamento, raza="Mestizo", edad=None):
        """ Agrega un perro al inventario"""
        
        try:
            # Validar que el ID no exista
            if self.inventario.obtener_recurso(id):
                return False, f"Ya existe un recurso con ID '{id}'"
            
            perro = Perro(id, nombre, tamano, temperamento, raza, edad)
            self.inventario.agregar_perro(perro)
            return True, f"Perro '{nombre}' agregado exitosamente"
        except ValueError as e:
            return False, str(e)
        except Exception as e:
            return False, f"Error al agregar perro: {str(e)}"
    
    def agregar_espacio(self, id, nombre, capacidad=1, descripcion=""):
        """Agrega un espacio al inventario """
        try:
            if self.inventario.obtener_recurso(id):
                return False, f"Ya existe un recurso con ID '{id}'"
            
            espacio = Espacio(id, nombre, capacidad, descripcion)
            self.inventario.agregar_espacio(espacio)
            return True, f"Espacio '{nombre}' agregado exitosamente"
        except Exception as e:
            return False, f"Error al agregar espacio: {str(e)}"
    
    def agregar_personal(self, id, nombre, rol, telefono="", email=""):
        """
        Agrega un personal al inventario
        
        Returns:
            tuple: (exito, mensaje)
        """
        try:
            if self.inventario.obtener_recurso(id):
                return False, f"Ya existe un recurso con ID '{id}'"
            
            persona = Personal(id, nombre, rol, telefono, email)
            self.inventario.agregar_personal(persona)
            return True, f"Personal '{nombre}' agregado exitosamente"
        except ValueError as e:
            return False, str(e)
        except Exception as e:
            return False, f"Error al agregar personal: {str(e)}"
    
    def eliminar_recurso(self, recurso_id):
        """ Elimina un recurso del inventario"""
        try:
            # Verificar que no esté en uso en eventos futuros
            ahora = datetime.now()
            for evento in self.eventos:
                if evento.inicio > ahora and recurso_id in evento.recursos_ids:
                    return False, f"No se puede eliminar: el recurso está asignado al evento '{evento.tipo}' el {evento.inicio.strftime('%d/%m/%Y')}"
            
            if self.inventario.eliminar_recurso(recurso_id):
                return True, "Recurso eliminado exitosamente"
            else:
                return False, "Recurso no encontrado"
        except Exception as e:
            return False, f"Error al eliminar: {str(e)}"
    
    def obtener_perros(self):
        """Retorna lista de todos los perros"""
        return self.inventario.listar_perros()
    
    def obtener_espacios(self):
        """Retorna lista de todos los espacios"""
        return self.inventario.listar_espacios()
    
    def obtener_personal(self):
        """Retorna lista de todo el personal"""
        return self.inventario.listar_personal()
    
    def obtener_recurso(self, recurso_id):
        """Obtiene un recurso por su ID"""
        return self.inventario.obtener_recurso(recurso_id)
    
    # ========== GESTIÓN DE EVENTOS ==========
    
    def crear_evento(self, tipo, recursos_ids, inicio, fin, descripcion=""):
        """Crea un nuevo evento"""
        try:
            evento_id = f"evt_{self._contador_eventos:03d}"
            evento = Evento(evento_id, tipo, recursos_ids, inicio, fin, descripcion)
            
            # Validar
            valido, mensaje = self.validador.validar_evento(evento, self.eventos)
            if not valido:
                return False, mensaje, None
            
            # Agregar
            self.eventos.append(evento)
            self._contador_eventos += 1
            
            # Actualizar buscador
            self.buscador = BuscadorHuecos(self.eventos, self.validador)
            
            return True, "Evento creado exitosamente", evento
        
        except ValueError as e:
            return False, str(e), None
        except Exception as e:
            return False, f"Error: {str(e)}", None
    
    def eliminar_evento(self, evento_id):
        """Elimina un evento"""
        try:
            for i, evento in enumerate(self.eventos):
                if evento.id == evento_id:
                    self.eventos.pop(i)
                    # Actualizar buscador
                    self.buscador = BuscadorHuecos(self.eventos, self.validador)
                    return True, "Evento eliminado exitosamente"
            
            return False, "Evento no encontrado"
        except Exception as e:
            return False, f"Error al eliminar: {str(e)}"
    
    def obtener_eventos(self, incluir_pasados=False):
        """
        Obtiene lista de eventos
        
        Args:
            incluir_pasados: Si True, incluye eventos pasados
        
        Returns:
            Lista de eventos ordenados por fecha
        """
        if incluir_pasados:
            return sorted(self.eventos, key=lambda e: e.inicio)
        else:
            ahora = datetime.now()
            eventos_futuros = [e for e in self.eventos if e.inicio >= ahora]
            return sorted(eventos_futuros, key=lambda e: e.inicio)
    
    def obtener_evento(self, evento_id):
        """Obtiene un evento por su ID"""
        for evento in self.eventos:
            if evento.id == evento_id:
                return evento
        return None
    
    def obtener_eventos_hoy(self):
        """Obtiene los eventos de hoy"""
        hoy = datetime.now().date()
        eventos_hoy = []
        for evento in self.eventos:
            if evento.inicio.date() == hoy:
                eventos_hoy.append(evento)
        return sorted(eventos_hoy, key=lambda e: e.inicio)
    
    def obtener_proximos_eventos(self, dias=7):
        """Obtiene los eventos de los próximos N días"""
        ahora = datetime.now()
        limite = ahora + timedelta(days=dias)
        eventos_proximos = []
        for evento in self.eventos:
            if ahora <= evento.inicio <= limite:
                eventos_proximos.append(evento)
        return sorted(eventos_proximos, key=lambda e: e.inicio)
    
    # ========== BÚSQUEDA DE HUECOS ==========
    
    def buscar_hueco_disponible(self, recursos_ids, duracion_minutos, dias_buscar=7):
        """
        Busca el primer hueco disponible
        
        Returns:
            tuple: (inicio, fin) o (None, None)
        """
        return self.buscador.buscar_primer_hueco(
            recursos_ids, 
            duracion_minutos, 
            dias_buscar=dias_buscar
        )
    
    # ========== ESTADÍSTICAS ==========
    
    def obtener_estadisticas(self):
        """
        Obtiene estadísticas del refugio
        
        Returns:
            dict con estadísticas
        """
        ahora = datetime.now()
        eventos_futuros = [e for e in self.eventos if e.inicio >= ahora]
        eventos_pasados = [e for e in self.eventos if e.inicio < ahora]
        
        # Contar eventos por tipo
        eventos_por_tipo = {}
        for evento in self.eventos:
            if evento.tipo not in eventos_por_tipo:
                eventos_por_tipo[evento.tipo] = 0
            eventos_por_tipo[evento.tipo] += 1
        
        return {
            'total_perros': len(self.inventario.listar_perros()),
            'total_espacios': len(self.inventario.listar_espacios()),
            'total_personal': len(self.inventario.listar_personal()),
            'total_eventos': len(self.eventos),
            'eventos_futuros': len(eventos_futuros),
            'eventos_pasados': len(eventos_pasados),
            'eventos_por_tipo': eventos_por_tipo
        }
    
    # ========== PERSISTENCIA ==========
    
    def guardar_datos(self, archivo=None):
        """Guarda los datos en archivo JSON """
        if archivo is None:
            archivo = self.archivo_datos
        
        try:
            datos = {
                'inventario': self.inventario.to_dict(),
                'eventos': [e.to_dict() for e in self.eventos],
                'contador_eventos': self._contador_eventos,
                'fecha_guardado': datetime.now().isoformat()
            }
            
            with open(archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
            
            return True, f"Datos guardados en {archivo}"
        
        except Exception as e:
            return False, f"Error al guardar: {str(e)}"
    
    def cargar_datos(self, archivo=None):
        """Carga los datos desde archivo JSON """
        if archivo is None:
            archivo = self.archivo_datos
        
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            # Cargar inventario
            self.inventario.from_dict(datos['inventario'])
            
            # Cargar eventos
            self.eventos = [Evento.from_dict(e) for e in datos['eventos']]
            
            # Cargar contador
            self._contador_eventos = datos.get('contador_eventos', 1)
            
            # Actualizar validador y buscador
            self.validador = ValidadorEventos(self.inventario)
            self.buscador = BuscadorHuecos(self.eventos, self.validador)
            
            return True, f"Datos cargados desde {archivo}"
        
        except FileNotFoundError:
            return False, f"Archivo '{archivo}' no encontrado"
        except json.JSONDecodeError:
            return False, "Error al leer el archivo JSON"
        except Exception as e:
            return False, f"Error al cargar: {str(e)}"
    