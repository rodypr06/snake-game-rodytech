"""
Test suite for Snake Game
Tests server functionality, file existence, and game components
"""
import unittest
import os
import sys
from pathlib import Path


class TestProjectStructure(unittest.TestCase):
    """Test project files and structure"""

    def test_required_files_exist(self):
        """Verify all required files are present"""
        required_files = [
            'server.py',
            'requirements.txt',
            'README.md',
            'static/game.html',
            'static/manifest.json'
        ]

        for file_path in required_files:
            with self.subTest(file=file_path):
                self.assertTrue(
                    os.path.exists(file_path),
                    f"Required file missing: {file_path}"
                )

    def test_python_files_are_valid(self):
        """Test that Python files have valid syntax"""
        python_files = ['server.py', 'crew.py', 'enhance_game.py']

        for py_file in python_files:
            with self.subTest(file=py_file):
                self.assertTrue(os.path.exists(py_file))
                # Try to compile the file to check syntax
                with open(py_file, 'r') as f:
                    code = f.read()
                    try:
                        compile(code, py_file, 'exec')
                    except SyntaxError as e:
                        self.fail(f"Syntax error in {py_file}: {e}")


class TestServerModule(unittest.TestCase):
    """Test Flask server functionality"""

    @classmethod
    def setUpClass(cls):
        """Import server module"""
        try:
            import server
            cls.server_module = server
        except ImportError as e:
            cls.server_module = None
            cls.import_error = str(e)

    def test_server_module_imports(self):
        """Test that server module can be imported"""
        self.assertIsNotNone(
            self.server_module,
            f"Failed to import server module: {getattr(self, 'import_error', 'Unknown error')}"
        )

    def test_flask_app_exists(self):
        """Test that Flask app is created"""
        if self.server_module is None:
            self.skipTest("Server module not available")

        self.assertTrue(
            hasattr(self.server_module, 'app'),
            "Flask app not found in server module"
        )

    def test_static_folder_configured(self):
        """Test that static folder is properly configured"""
        if self.server_module is None:
            self.skipTest("Server module not available")

        app = self.server_module.app
        # Flask returns absolute path, check that it ends with 'static'
        self.assertTrue(
            app.static_folder.endswith('static'),
            f"Static folder not configured correctly: {app.static_folder}"
        )


class TestGameHTML(unittest.TestCase):
    """Test game.html file"""

    def setUp(self):
        """Load game.html content"""
        self.html_path = 'static/game.html'
        if os.path.exists(self.html_path):
            with open(self.html_path, 'r', encoding='utf-8') as f:
                self.html_content = f.read()
        else:
            self.html_content = None

    def test_game_html_exists(self):
        """Test that game.html exists"""
        self.assertIsNotNone(
            self.html_content,
            "game.html file not found"
        )

    def test_html_has_canvas(self):
        """Test that HTML contains canvas element"""
        self.assertIn(
            '<canvas',
            self.html_content,
            "Canvas element not found in game.html"
        )

    def test_html_has_title(self):
        """Test that HTML has a title"""
        self.assertIn(
            '<title>',
            self.html_content,
            "Title tag not found in game.html"
        )

    def test_html_has_javascript(self):
        """Test that HTML contains JavaScript"""
        self.assertIn(
            '<script>',
            self.html_content,
            "Script tag not found in game.html"
        )

    def test_game_functions_exist(self):
        """Test that essential game functions are defined"""
        essential_functions = [
            'function draw(',
            'function generateFood(',
            'function restartGame(',
            'function startGame('
        ]

        for func in essential_functions:
            with self.subTest(function=func):
                self.assertIn(
                    func,
                    self.html_content,
                    f"Essential function not found: {func}"
                )

    def test_mobile_support(self):
        """Test that mobile features are present"""
        mobile_features = [
            'touchstart',
            'touchmove',
            'viewport',
            'mobile'
        ]

        for feature in mobile_features:
            with self.subTest(feature=feature):
                self.assertIn(
                    feature,
                    self.html_content.lower(),
                    f"Mobile feature not found: {feature}"
                )


class TestManifest(unittest.TestCase):
    """Test PWA manifest.json"""

    def test_manifest_exists(self):
        """Test that manifest.json exists"""
        self.assertTrue(
            os.path.exists('static/manifest.json'),
            "manifest.json not found"
        )

    def test_manifest_is_valid_json(self):
        """Test that manifest.json is valid JSON"""
        import json

        with open('static/manifest.json', 'r') as f:
            try:
                manifest = json.load(f)
                self.assertIsInstance(manifest, dict)
            except json.JSONDecodeError as e:
                self.fail(f"Invalid JSON in manifest.json: {e}")


class TestRequirements(unittest.TestCase):
    """Test requirements.txt"""

    def test_requirements_has_flask(self):
        """Test that Flask is in requirements"""
        with open('requirements.txt', 'r') as f:
            content = f.read().lower()

        self.assertIn(
            'flask',
            content,
            "Flask not found in requirements.txt"
        )

    def test_requirements_has_crewai(self):
        """Test that CrewAI is in requirements"""
        with open('requirements.txt', 'r') as f:
            content = f.read().lower()

        self.assertIn(
            'crewai',
            content,
            "CrewAI not found in requirements.txt"
        )


def run_tests():
    """Run all tests and return results"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestProjectStructure))
    suite.addTests(loader.loadTestsFromTestCase(TestServerModule))
    suite.addTests(loader.loadTestsFromTestCase(TestGameHTML))
    suite.addTests(loader.loadTestsFromTestCase(TestManifest))
    suite.addTests(loader.loadTestsFromTestCase(TestRequirements))

    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Return result
    return result


if __name__ == '__main__':
    print("=" * 70)
    print("SNAKE GAME TEST SUITE")
    print("=" * 70)
    print()

    result = run_tests()

    print()
    print("=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print()

    if result.wasSuccessful():
        print("✅ ALL TESTS PASSED!")
        sys.exit(0)
    else:
        print("❌ SOME TESTS FAILED")
        sys.exit(1)
