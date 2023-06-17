from tests.manager.manager_api import TestApiCategory

class CategoryTest():
    def test_category(self):
        category = TestApiCategory().create_category()
        response = self.client.get(category)