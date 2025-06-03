from django.core.management.base import BaseCommand
from toys.models import Toy

class Command(BaseCommand):
    help = "Remove todos os brinquedos do banco de dados"

    def handle(self, *args, **kwargs):
        total = Toy.objects.count()
        if total == 0:
            self.stdout.write(self.style.WARNING("⚠️ Nenhum brinquedo encontrado."))
            return

        confirm = input(f"Tem certeza que deseja apagar TODOS os {total} brinquedos? [s/N]: ")
        if confirm.lower() == "s":
            Toy.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f"🗑️ {total} brinquedos removidos com sucesso!"))
        else:
            self.stdout.write(self.style.NOTICE("❌ Operação cancelada. Nenhum brinquedo foi removido."))
