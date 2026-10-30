"""Laboratorio didáctico: contiene fallas INTENCIONALES que deben identificarse.

No se debe reutilizar este código en producción. No realiza autenticación real.
"""
from datetime import datetime, timezone

USUARIOS = {
    "ana": {"id": "ana", "rol": "estudiante", "sede": "Central"},
    "luis": {"id": "luis", "rol": "estudiante", "sede": "Pacifico"},
    "maria": {"id": "maria", "rol": "docente", "sede": "Central"},
    "pedro": {"id": "pedro", "rol": "docente", "sede": "Pacifico"},
    "admin": {"id": "admin", "rol": "administrador", "sede": None},
}


def estado_inicial():
    """Crea datos de laboratorio independientes para cada ejecución."""
    return {
        "expedientes": {
            "101": {"id": "101", "estudiante": "ana", "sede": "Central", "nota": 82},
            "202": {"id": "202", "estudiante": "luis", "sede": "Pacifico", "nota": 91},
        },
        "sesiones": {
            f"lab-{id_usuario}": {"usuario": id_usuario, "revocada": False, "expirada": False}
            for id_usuario in USUARIOS
        } | {"lab-vencida": {"usuario": "ana", "revocada": False, "expirada": True}},
        "auditoria": [],
    }


def autenticar(estado, token):
    """Recibe tokens SINTETICOS; no implementa autenticación de producción."""
    sesion = estado["sesiones"].get(token)
    if sesion is None:
        return None
    if sesion["revocada"] or sesion["expirada"]:
        return None
    return USUARIOS[sesion["usuario"]]


def registrar_auditoria(estado, accion, usuario, expediente_id):
    """Registra el evento sin persistir secretos de sesión."""
    estado["auditoria"].append(
        {
            "accion": accion,
            "actor": usuario["id"],
            "id": expediente_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    )


def leer_expediente(estado, token, expediente_id):
    usuario = autenticar(estado, token)
    if usuario is None:
        return 401, {"error": "No autenticado"}
    expediente = estado["expedientes"].get(expediente_id)
    if expediente is None:
        return 404, {"error": "No existe"}
    if (
        usuario["rol"] == "estudiante"
        and expediente["estudiante"] != usuario["id"]
    ):
        return 403, {"error": "Acceso denegado"}
    if usuario["rol"] == "docente" and usuario["sede"] != expediente["sede"]:
        return 403, {"error": "Acceso denegado"}
    registrar_auditoria(estado, "lectura", usuario, expediente_id)
    return 200, dict(expediente)


def actualizar_nota(estado, token, expediente_id, nota):
    usuario = autenticar(estado, token)
    if usuario is None:
        return 401, {"error": "No autenticado"}
    expediente = estado["expedientes"].get(expediente_id)
    if expediente is None:
        return 404, {"error": "No existe"}
    if usuario["rol"] != "docente":
        return 403, {"error": "Operación denegada"}
    if usuario["sede"] != expediente["sede"]:
        return 403, {"error": "Operación denegada"}
    if not isinstance(nota, (int, float)) or not 0 <= nota <= 100:
        return 400, {"error": "Nota inválida"}
    expediente["nota"] = nota
    registrar_auditoria(estado, "actualizacion", usuario, expediente_id)
    return 200, dict(expediente)


def revocar_sesion(estado, token):
    sesion = estado["sesiones"].get(token)
    if sesion is None:
        return 401, {"error": "No autenticado"}
    sesion["revocada"] = True
    return 200, {"mensaje": "Sesión revocada"}
