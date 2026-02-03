class Recurso:
    """Clase base para todos los recursos"""
    
    def __init__(self, id, nombre, tipo):
        """
        Inicializa un recurso
        
        Args:
            id (str): Identificador único
            nombre (str): Nombre del recurso
            tipo (str): Tipo de recurso
        """
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
    
    def __str__(self):
        return f"{self.nombre}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}(id='{self.id}', nombre='{self.nombre}')"
    
    def to_dict(self):
        """Convierte el recurso a diccionario para JSON"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo
        }


class Espacio(Recurso):
    """Representa un espacio físico del refugio"""
    
    def __init__(self, id, nombre, capacidad=1, descripcion=""):
        """
        Inicializa un espacio
        
        Args:
            id (str): Identificador único
            nombre (str): Nombre del espacio
            capacidad (int): Capacidad del espacio
            descripcion (str): Descripción del espacio
        """
        super().__init__(id, nombre, "espacio")
        self.capacidad = capacidad
        self.descripcion = descripcion
    
    def to_dict(self):
        data = super().to_dict()
        data['capacidad'] = self.capacidad
        data['descripcion'] = self.descripcion
        return data
    
    @classmethod
    def from_dict(cls, data):
        """Crea un espacio desde un diccionario"""
        return cls(
            id=data['id'],
            nombre=data['nombre'],
            capacidad=data.get('capacidad', 1),
            descripcion=data.get('descripcion', '')
        )


class Personal(Recurso):
    """Representa un miembro del personal del refugio"""
    
    # Roles válidos
    ROLES_VALIDOS = ["veterinario", "entrenador", "voluntario", "groomer"]
    
    def __init__(self, id, nombre, rol, telefono="", email=""):
        """
        Inicializa un miembro del personal
        
        Args:
            id (str): Identificador único
            nombre (str): Nombre completo
            rol (str): Rol del personal (veterinario, entrenador, voluntario, groomer)
            telefono (str): Número de teléfono
            email (str): Correo electrónico
        """
        super().__init__(id, nombre, "personal")
        
        # Validar rol
        if rol.lower() not in self.ROLES_VALIDOS:
            raise ValueError(f"Rol inválido. Debe ser: {', '.join(self.ROLES_VALIDOS)}")
        
        self.rol = rol.lower()
        self.telefono = telefono
        self.email = email
    
    def es_veterinario(self):
        """Retorna True si es veterinario"""
        return self.rol == "veterinario"
    
    def es_entrenador(self):
        """Retorna True si es entrenador"""
        return self.rol == "entrenador"
    
    def es_voluntario(self):
        """Retorna True si es voluntario"""
        return self.rol == "voluntario"
    
    def es_groomer(self):
        """Retorna True si es groomer"""
        return self.rol == "groomer"
    
    def puede_supervisar_socializacion(self):
        """Retorna True si puede supervisar socialización"""
        return self.rol in ["entrenador", "voluntario"]
    
    def __str__(self):
        return f"{self.nombre} ({self.rol.capitalize()})"
    
    def to_dict(self):
        data = super().to_dict()
        data['rol'] = self.rol
        data['telefono'] = self.telefono
        data['email'] = self.email
        return data
    
    @classmethod
    def from_dict(cls, data):
        """Crea un personal desde un diccionario"""
        return cls(
            id=data['id'],
            nombre=data['nombre'],
            rol=data['rol'],
            telefono=data.get('telefono', ''),
            email=data.get('email', '')
        )


class InventarioRecursos:
    """Gestiona el inventario de todos los recursos del refugio"""
    
    def __init__(self):
        """Inicializa el inventario vacío"""
        self.espacios = {}
        self.personal = {}
        self.perros = {}
    
    def agregar_espacio(self, espacio):
        """Agrega un espacio al inventario"""
        self.espacios[espacio.id] = espacio
    
    def agregar_personal(self, persona):
        """Agrega un personal al inventario"""
        self.personal[persona.id] = persona
    
    def agregar_perro(self, perro):
        """Agrega un perro al inventario"""
        self.perros[perro.id] = perro
    
    def obtener_recurso(self, recurso_id):
        """
        Obtiene un recurso por su ID
        
        Returns:
            Recurso o None si no existe
        """
        if recurso_id in self.espacios:
            return self.espacios[recurso_id]
        elif recurso_id in self.personal:
            return self.personal[recurso_id]
        elif recurso_id in self.perros:
            return self.perros[recurso_id]
        return None
    
    def eliminar_recurso(self, recurso_id):
        """Elimina un recurso del inventario"""
        if recurso_id in self.espacios:
            del self.espacios[recurso_id]
            return True
        elif recurso_id in self.personal:
            del self.personal[recurso_id]
            return True
        elif recurso_id in self.perros:
            del self.perros[recurso_id]
            return True
        return False
    
    def listar_espacios(self):
        """Retorna lista de todos los espacios"""
        return list(self.espacios.values())
    
    def listar_personal(self):
        """Retorna lista de todo el personal"""
        return list(self.personal.values())
    
    def listar_perros(self):
        """Retorna lista de todos los perros"""
        return list(self.perros.values())
    
    def listar_todos(self):
        """Retorna lista de todos los recursos"""
        return self.listar_espacios() + self.listar_personal() + self.listar_perros()
    
    def total_recursos(self):
        """Retorna el número total de recursos"""
        return len(self.espacios) + len(self.personal) + len(self.perros)
    
    def to_dict(self):
        """Convierte el inventario a diccionario para JSON"""
        return {
            'espacios': {id: esp.to_dict() for id, esp in self.espacios.items()},
            'personal': {id: per.to_dict() for id, per in self.personal.items()},
            'perros': {id: perro.to_dict() for id, perro in self.perros.items()}
        }
    
    def from_dict(self, data):
        """Carga el inventario desde un diccionario"""
        from perro import Perro
        
        # Limpiar inventario actual
        self.espacios = {}
        self.personal = {}
        self.perros = {}
        
        # Cargar espacios
        if 'espacios' in data:
            for id, esp_data in data['espacios'].items():
                espacio = Espacio.from_dict(esp_data)
                self.espacios[id] = espacio
        
        # Cargar personal
        if 'personal' in data:
            for id, per_data in data['personal'].items():
                persona = Personal.from_dict(per_data)
                self.personal[id] = persona
        
        # Cargar perros
        if 'perros' in data:
            for id, perro_data in data['perros'].items():
                perro = Perro.from_dict(perro_data)
                self.perros[id] = perro
