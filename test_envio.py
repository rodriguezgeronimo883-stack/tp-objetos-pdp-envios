import unittest

from envio import (
    Servicio,
    Destino,
    Paquete,
    CalculadoraEnvio
)


class TestEnvios(unittest.TestCase):

    def test_paquete_liviano(self):
        paquete = Paquete(0.5, 20, 15, 5)

        costo = CalculadoraEnvio.calcular_costo(
            Servicio.ESTANDAR,
            Destino.CABA,
            paquete
        )

        self.assertEqual(costo, 500)

    def test_paquete_voluminoso(self):
        paquete = Paquete(3, 50, 50, 50)

        costo = CalculadoraEnvio.calcular_costo(
            Servicio.EXPRESS,
            Destino.INTERIOR,
            paquete
        )

        self.assertEqual(costo, 16200)

    def test_peso_volumetrico(self):
        paquete = Paquete(1, 50, 50, 50)

        self.assertEqual(
            paquete.peso_volumetrico(),
            25
        )

    def test_peso_facturable(self):
        paquete = Paquete(1, 50, 50, 50)

        self.assertEqual(
            paquete.peso_facturable(),
            25
        )

    def test_mismo_dia_fuera_de_zona(self):
        paquete = Paquete(1, 10, 10, 10)

        with self.assertRaises(ValueError):
            CalculadoraEnvio.calcular_costo(
                Servicio.MISMO_DIA,
                Destino.INTERIOR,
                paquete
            )


if __name__ == "__main__":
    unittest.main()
