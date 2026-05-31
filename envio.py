from enum import Enum


class Servicio(Enum):
    ESTANDAR = 500
    EXPRESS = 1200
    MISMO_DIA = 2500
    RETIRO_EN_SUCURSAL = 350


class Destino(Enum):
    CABA = 1.0
    GBA = 1.3
    INTERIOR = 1.8
    PATAGONIA = 2.2


class Paquete:
    def __init__(self, peso_real, largo, ancho, alto):
        self.peso_real = peso_real
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

    def peso_volumetrico(self):
        return (self.largo * self.ancho * self.alto) / 5000

    def peso_facturable(self):
        return max(self.peso_real, self.peso_volumetrico())


class CalculadoraEnvio:

    @staticmethod
    def calcular_recargo(peso_facturable):
        if peso_facturable <= 1:
            return 0

        if peso_facturable <= 5:
            return (peso_facturable - 1) * 200

        return 800 + ((peso_facturable - 5) * 350)

    @staticmethod
    def calcular_costo(servicio, destino, paquete):

        if (
            servicio == Servicio.MISMO_DIA
            and destino not in [Destino.CABA, Destino.GBA]
        ):
            raise ValueError(
                "El servicio Mismo Día solo está disponible en CABA y GBA"
            )

        peso = paquete.peso_facturable()

        costo_base = servicio.value
        recargo = CalculadoraEnvio.calcular_recargo(peso)

        subtotal = costo_base + recargo

        return subtotal * destino.value
