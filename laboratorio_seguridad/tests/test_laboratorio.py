"""Pruebas de ejemplo: algunas fallan INTENCIONALMENTE (fase roja de TDD)."""
import unittest
from src.lab import estado_inicial, leer_expediente, actualizar_nota, revocar_sesion


class SeguridadExpedientes(unittest.TestCase):
    def setUp(self):
        self.estado = estado_inicial()  # Un estado independiente por prueba.

    def test_estudiante_consulta_expediente_propio(self):
        codigo, datos = leer_expediente(self.estado, "lab-ana", "101")
        self.assertEqual(200, codigo)
        self.assertEqual("ana", datos.get("estudiante"))

    def test_docente_actualiza_nota_en_su_sede(self):
        codigo, datos = actualizar_nota(self.estado, "lab-maria", "101", 85)
        self.assertEqual(200, codigo)
        self.assertEqual(85, datos.get("nota"))

    def test_docente_consulta_expediente_de_su_sede(self):
        codigo, datos = leer_expediente(self.estado, "lab-maria", "101")

        self.assertEqual(200, codigo)
        self.assertEqual("Central", datos.get("sede"))

    def test_acepta_nota_en_limite_inferior_valido(self):
        codigo, datos = actualizar_nota(self.estado, "lab-maria", "101", 0)

        self.assertEqual(200, codigo)
        self.assertEqual(0, datos.get("nota"))

    def test_rechaza_nota_en_limite_superior_invalido(self):
        nota_original = self.estado["expedientes"]["101"]["nota"]

        codigo, _ = actualizar_nota(self.estado, "lab-maria", "101", 101)

        self.assertEqual(400, codigo)
        self.assertEqual(nota_original, self.estado["expedientes"]["101"]["nota"])

    def test_docente_no_actualiza_nota_de_otra_sede(self):
        nota_original = self.estado["expedientes"]["202"]["nota"]

        codigo, _ = actualizar_nota(self.estado, "lab-maria", "202", 85)

        self.assertEqual(403, codigo)
        self.assertEqual(nota_original, self.estado["expedientes"]["202"]["nota"])

    def test_rechaza_nota_fuera_de_rango(self):
        nota_original = self.estado["expedientes"]["101"]["nota"]

        codigo, _ = actualizar_nota(self.estado, "lab-maria", "101", -1)

        self.assertEqual(400, codigo)
        self.assertEqual(nota_original, self.estado["expedientes"]["101"]["nota"])

    def test_estudiante_no_consulta_expediente_ajeno(self):
        codigo, datos = leer_expediente(self.estado, "lab-ana", "202")
        self.assertEqual(403, codigo)
        self.assertNotIn("nota", datos)

    def test_sesion_revocada_no_permita_lecturas(self):
        codigo, _ = revocar_sesion(self.estado, "lab-ana")
        self.assertEqual(200, codigo)
        codigo, datos = leer_expediente(self.estado, "lab-ana", "101")
        self.assertEqual(401, codigo)
        self.assertNotIn("nota", datos)

    def test_sesion_expirada_no_permita_lecturas(self):
        codigo, datos = leer_expediente(self.estado, "lab-vencida", "101")

        self.assertEqual(401, codigo)
        self.assertNotIn("nota", datos)

    def test_administrador_no_actualiza_notas(self):
        nota_original = self.estado["expedientes"]["101"]["nota"]

        codigo, _ = actualizar_nota(self.estado, "lab-admin", "101", 90)

        self.assertEqual(403, codigo)
        self.assertEqual(nota_original, self.estado["expedientes"]["101"]["nota"])

    def test_auditoria_no_expone_token_y_registra_timestamp(self):
        codigo, _ = leer_expediente(self.estado, "lab-ana", "101")

        self.assertEqual(200, codigo)
        registro = self.estado["auditoria"][-1]
        self.assertEqual("lectura", registro["accion"])
        self.assertEqual("101", registro["id"])
        self.assertEqual("ana", registro["actor"])
        self.assertIn("timestamp", registro)
        self.assertNotIn("token", registro)


if __name__ == "__main__":
    unittest.main()
