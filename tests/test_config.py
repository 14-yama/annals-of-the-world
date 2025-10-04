from annals.config import get_config


def test_get_config_has_attrs():
    cfg = get_config()
    assert hasattr(cfg, "NEO4J_URI")
    assert hasattr(cfg, "NEO4J_USER")
    assert hasattr(cfg, "NEO4J_PASSWORD")
    assert hasattr(cfg, "NEO4J_DATABASE")
