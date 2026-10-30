"""Pruebas de integración HTTP contra el servidor local del laboratorio."""
import http.client
import json
import threading
import unittest

from servidor import ServidorLaboratorio, ThreadingHTTPServer
from src.lab import estado_inicial


class IntegracionApiSeguridad(unittest.TestCase):
    def setUp(self):
        ServidorLaboratorio.estado = estado_inicial()
        self.servidor = ThreadingHTTPServer(("127.0.0.1", 0), ServidorLaboratorio)
        self.hilo = threading.Thread(target=self.servidor.serve_forever, daemon=True)
        self.hilo.start()

    def tearDown(self):
        self.servidor.shutdown()
        self.servidor.server_close()
        self.hilo.join()

    def solicitar_actualizacion(self, expediente_id, nota):
        conexion = http.client.HTTPConnection("127.0.0.1", self.servidor.server_port)
        cuerpo = json.dumps({"nota": nota})
        conexion.request(
            "POST",
            f"/expedientes/{expediente_id}/nota",
            body=cuerpo,
            headers={
                "Authorization": "Bearer lab-maria",
                "Content-Type": "application/json",
            },
        )
        respuesta = conexion.getresponse()
        datos = json.loads(respuesta.read().decode("utf-8"))
        conexion.close()
        return respuesta.status, datos

    def test_api_docente_no_actualiza_nota_de_otra_sede(self):
        nota_original = ServidorLaboratorio.estado["expedientes"]["202"]["nota"]

        codigo, datos = self.solicitar_actualizacion("202", 85)

        self.assertEqual(403, codigo)
        self.assertNotIn("nota", datos)
        self.assertEqual(nota_original, ServidorLaboratorio.estado["expedientes"]["202"]["nota"])

    def test_api_rechaza_nota_fuera_de_rango(self):
        nota_original = ServidorLaboratorio.estado["expedientes"]["101"]["nota"]

        codigo, datos = self.solicitar_actualizacion("101", -1)

        self.assertEqual(400, codigo)
        self.assertNotIn("nota", datos)
        self.assertEqual(nota_original, ServidorLaboratorio.estado["expedientes"]["101"]["nota"])


if __name__ == "__main__":
    unittest.main()
