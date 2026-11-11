"""
Matriz de riesgos del Plan de Contingencia para infraestructura tecnológica
ÉTICA_SEGURIDAD DE DATOS_S11 - Carranza Jacinto Juan Diego

Calcula el nivel de riesgo (probabilidad x impacto) de cada escenario,
lo clasifica, ordena los escenarios por prioridad y verifica que cada
estrategia de respuesta esté vinculada al menos a un ODS y a una norma.

Uso:
    python src/matriz_riesgos.py
Salidas:
    salidas/matriz_riesgos.md   tabla priorizada
    salidas/mapa_calor.png      mapa de calor probabilidad x impacto
"""
from pathlib import Path
import csv

BASE = Path(__file__).resolve().parent.parent
DATOS = BASE / "datos" / "escenarios.csv"
SALIDAS = BASE / "salidas"


def clasificar(nivel: int) -> str:
    if nivel >= 15:
        return "Crítico"
    if nivel >= 10:
        return "Alto"
    if nivel >= 5:
        return "Medio"
    return "Bajo"


def cargar_escenarios(ruta: Path) -> list[dict]:
    with ruta.open(encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    for fila in filas:
        fila["P"] = int(fila["P"])
        fila["I"] = int(fila["I"])
        fila["nivel"] = fila["P"] * fila["I"]
        fila["clase"] = clasificar(fila["nivel"])
    return sorted(filas, key=lambda x: (-x["nivel"], -x["I"]))


def validar_alineamiento(filas: list[dict]) -> list[str]:
    """Devuelve los escenarios cuya estrategia no cita ODS o norma."""
    faltantes = []
    for f in filas:
        if not f["ods"].strip() or not f["normas"].strip():
            faltantes.append(f["id"])
    return faltantes


def escribir_tabla(filas: list[dict], destino: Path) -> None:
    lineas = [
        "| Prioridad | ID | Escenario | P | I | Nivel | Clase | RTO | RPO | ODS | Normas |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for n, f in enumerate(filas, 1):
        lineas.append(
            f"| {n} | {f['id']} | {f['escenario']} | {f['P']} | {f['I']} | "
            f"{f['nivel']} | {f['clase']} | {f['rto']} | {f['rpo']} | "
            f"{f['ods']} | {f['normas']} |"
        )
    destino.write_text("\n".join(lineas) + "\n", encoding="utf-8")


def dibujar_mapa(filas: list[dict], destino: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap

    plt.rcParams["font.family"] = ["Caladea", "DejaVu Serif"]
    colores = ListedColormap(["#DDEBD5", "#F6E7B4", "#F2C18D", "#E07A6B"])
    matriz = [[0] * 5 for _ in range(5)]
    for p in range(1, 6):
        for i in range(1, 6):
            v = p * i
            matriz[p - 1][i - 1] = 3 if v >= 15 else 2 if v >= 10 else 1 if v >= 5 else 0

    fig, ax = plt.subplots(figsize=(4.0, 3.4), dpi=220)
    ax.imshow(matriz, cmap=colores, origin="lower", vmin=0, vmax=3)
    celdas: dict[tuple, list[str]] = {}
    for f in filas:
        celdas.setdefault((f["P"], f["I"]), []).append(f["id"])
    for (p, i), ids in celdas.items():
        ax.text(i - 1, p - 1, "\n".join(ids), ha="center", va="center",
                fontsize=10, color="#1F2A44", fontweight="bold")
    ax.set_xticks(range(5), [str(n) for n in range(1, 6)])
    ax.set_yticks(range(5), [str(n) for n in range(1, 6)])
    ax.set_xlabel("Impacto")
    ax.set_ylabel("Probabilidad")
    ax.set_xticks([x + 0.5 for x in range(4)], minor=True)
    ax.set_yticks([y + 0.5 for y in range(4)], minor=True)
    ax.grid(which="minor", color="white", linewidth=1.5)
    ax.tick_params(which="minor", length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    fig.tight_layout()
    fig.savefig(destino)
    plt.close(fig)


def main() -> None:
    SALIDAS.mkdir(exist_ok=True)
    filas = cargar_escenarios(DATOS)
    faltantes = validar_alineamiento(filas)
    escribir_tabla(filas, SALIDAS / "matriz_riesgos.md")
    dibujar_mapa(filas, SALIDAS / "mapa_calor.png")

    print(f"{'#':<3}{'ID':<5}{'Nivel':<7}{'Clase':<9}Escenario")
    for n, f in enumerate(filas, 1):
        print(f"{n:<3}{f['id']:<5}{f['nivel']:<7}{f['clase']:<9}{f['escenario']}")
    resumen = {}
    for f in filas:
        resumen[f["clase"]] = resumen.get(f["clase"], 0) + 1
    print("\nResumen por clase:", resumen)
    print("Escenarios sin ODS o norma:", faltantes or "ninguno")


if __name__ == "__main__":
    main()
