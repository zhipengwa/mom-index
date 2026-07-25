import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PublicFrameworkTests(unittest.TestCase):
    def test_demo_data_is_explicitly_synthetic(self):
        dashboard = json.loads((ROOT / "data" / "dashboard_data.json").read_text(encoding="utf-8"))
        self.assertIn("合成", dashboard["data_notice"])
        self.assertIn("脱敏", dashboard["data_notice"])
        self.assertEqual([], json.loads((ROOT / "data" / "xhs_posts.json").read_text(encoding="utf-8")))

    def test_frontend_uses_bundled_chart_library(self):
        html = (ROOT / "frontend" / "dashboard.html").read_text(encoding="utf-8")
        self.assertIn('src="chart.umd.min.js"', html)
        self.assertNotIn("cdn.jsdelivr.net", html)
        self.assertTrue((ROOT / "frontend" / "chart.umd.min.js").is_file())

    def test_private_artifacts_are_not_present(self):
        forbidden_names = {
            ".env", "xhs_auth.json", "raw_posts.json", "cookies.json",
            "llm_refiner.py", "calibrator.py", "market_calibrator.py",
        }
        present = {path.name for path in ROOT.rglob("*") if path.is_file()}
        self.assertTrue(forbidden_names.isdisjoint(present))


if __name__ == "__main__":
    unittest.main()
