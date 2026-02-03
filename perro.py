from datetime import datetime

class Perro:
    """Representa un perro del refugio"""
    
    # Constantes para validación
    TAMANOS_VALIDOS = ["pequeño", "mediano", "grande"]
    TEMPERAMENTOS_VALIDOS = ["social", "timido", "dominante", "agresivo"]
    
    def __init__(self, id, nombre, tamano, temperamento, raza="Mestizo", edad=None):
        """
        Inicializa un perro
        
        Args:
            id (str): Identificador único del perro
            nombre (str): Nombre del perro
            tamano (str): Tamaño del perro (pequeño, mediano, grande)
            temperamento (str): Temperamento del perro
            raza (str): Raza del perro
            edad (int): Edad en años
        """
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        
        # Validar tamaño
        if tamano.lower() not in self.TAMANOS_VALIDOS:
            raise ValueError(f"Tamaño inválido. Debe ser: {', '.join(self.TAMANOS_VALIDOS)}")
        self.tamano = tamano.lower()
        
        # Validar temperamento
        if temperamento.lower() not in self.TEMPERAMENTOS_VALIDOS:
            raise ValueError(f"Temperamento inválido. Debe ser: {', '.join(self.TEMPERAMENTOS_VALIDOS)}")
        self.temperamento = temperamento.lower()
    

    
    def es_dominante(self):
        """Retorna True si el perro tiene temperamento dominante o agresivo"""
        return self.temperamento in ["dominante", "agresivo"]
    
    def __str__(self):
        return f"{self.nombre} ({self.tamano}, {self.temperamento})"
    
    def __repr__(self):
        return f"Perro(id='{self.id}', nombre='{self.nombre}', tamano='{self.tamano}', temperamento='{self.temperamento}')"
    
    def to_dict(self):
        """Convierte el perro a diccionario para JSON"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'raza': self.raza,
            'edad': self.edad,
            'tamano': self.tamano,
            'temperamento': self.temperamento
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea un perro desde un diccionario"""

        return cls(
            id=data['id'],
            nombre=data['nombre'],
            tamano=data['tamano'],
            temperamento=data['temperamento'],
            raza=data.get('raza', 'Mestizo'),
            edad=data.get('edad')
        )
