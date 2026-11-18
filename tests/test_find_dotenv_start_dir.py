from pathlib import Path

from dotenv import find_dotenv


def test_find_dotenv_from_start_dir(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / ".env").touch()

    project = tmp_path / "project"
    start_dir = project / "src"
    start_dir.mkdir(parents=True)
    expected = project / ".env"
    expected.touch()

    found = find_dotenv(dir=str(start_dir))

    assert found == str(expected)
    assert Path.cwd() == tmp_path
