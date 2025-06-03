from django.core.management.base import BaseCommand
from toys.models import Toy
from faker import Faker
import random

fake = Faker("pt_BR")

TOY_CATEGORIES = ["Ação", "Educativo", "Bonecas", "Veículos", "Tecnológico", "Construção"]

class Command(BaseCommand):
    help = "Popula o banco de dados com brinquedos aleatórios"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            type=int,
            default=20,
            help="Quantidade de brinquedos a serem criados (padrão: 20)"
        )

    def handle(self, *args, **kwargs):
        total = kwargs["total"]

        for _ in range(total):
            toy = Toy.objects.create(
                name=fake.unique.first_name() + " " + random.choice(["Turbo", "X", "Z", "Robo", "Jet"]),
                description=fake.sentence(nb_words=6),
                toy_category=random.choice(TOY_CATEGORIES),
                release_date=fake.date_time_between(start_date="-3y", end_date="now"),
                was_included_in_home=fake.boolean(chance_of_getting_true=60)
            )
            self.stdout.write(self.style.SUCCESS(f"✅ Criado: {toy.name} ({toy.toy_category})"))
