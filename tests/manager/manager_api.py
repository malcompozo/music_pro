from faker import Faker
from api.serializers import CategorySerializer

faker = Faker()

class TestApiCategory:

    def category_json(self):
        return {
            'id' : faker.random_number(digits=10),
            'nom_category' : faker.name(), 
            'description' : faker.paragraph(),
            'created' : faker.date_of_birth(),
            'updated' : faker.date_of_birth()
        }

    def create_category(self):
        return CategorySerializer.objects.create(**self.category_json())
    