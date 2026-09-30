"""Testes do Batch-Backdoor-Agent (estrutura e integridade — sem executar)."""
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)


def _read(rel):
    with open(os.path.join(HERE, rel), encoding="utf-8", errors="replace") as f:
        return f.read()


def test_victim_data_removed():
    assert not os.path.exists(os.path.join(HERE, "data", "ifos.txt"))
    assert os.path.exists(os.path.join(HERE, "data", ".gitkeep"))


def test_backdoor_loop_refs_exist():
    """Todos os scripts referenciados pelo loop DEVEM existir no repo."""
    t = _read("src/backdoor_loop.bat")
    refs = re.findall(r'start "" "%~dp0([^\s"]+)"', t)
    assert refs, "nenhuma referência encontrada no loop"
    for ref in refs:
        path = os.path.join(HERE, "src", ref.replace("\\", "/"))
        assert os.path.exists(path), f"ref quebrada: {ref}"


def test_no_broken_or_personal_refs():
    for rel in ("src/backdoor_loop.bat", "src/info_stealer.bat",
                "scripts/inicio2.bat", "iniciar.bat"):
        t = _read(rel)
        assert "pri.vbs" not in t, f"{rel} ainda referencia pri.vbs"
        assert "key.vbs" not in t, f"{rel} referencia key.vbs inexistente"
        assert "FTP-CONFIG" not in t, f"{rel} referencia FTP-CONFIG inexistente"
        personal = "fr" + "ant"   # fragmentado: o literal não pode existir no repo
        assert personal not in t, f"{rel} contém caminho pessoal"


def test_no_legacy_broken_files():
    for gone in ("src/op.bat", "src/varia.bat", "src/informa.bat"):
        assert not os.path.exists(os.path.join(HERE, gone)), f"{gone} deveria ser removido"


def test_entry_exists():
    assert os.path.exists(os.path.join(HERE, "iniciar.bat"))
    assert os.path.exists(os.path.join(HERE, "scripts", "launcher.vbs"))


def test_launcher_targets_loop():
    t = _read("scripts/launcher.vbs")
    assert "backdoor_loop.bat" in t


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"✅ {fn.__name__}")
    print(f"\n{len(fns)} testes passaram.")
