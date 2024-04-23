# import json
# import glob
# from django.core.management.base import BaseCommand
# from oracles.models import OracleQuestion, OracleAnswer

# json_file_path = 'oracles/repository/*.json'

# class Command(BaseCommand):
#     help = 'Import questions and answers from a JSON file'

#     def add_arguments(self, parser):
#         parser.add_argument('--json_file', type=str, help='Path to the JSON file containing the questions and answers', default=None)

#     def handle(self, **options):
#         json_files = glob.glob(options['json_file'] or 'oracles/repository/*.json')

#         for json_file in json_files:
#             with open(json_file, 'r') as file:
#                 questions = json.load(file)

#             for q in questions:
#                 existing_question = OracleQuestion.objects.filter(question_text=q['question']).first()
#                 if existing_question:
#                     continue

#                 question = OracleQuestion(
#                     question_text=q['question'],
#                     category=q['category'],
#                 )
#                 question.save()

#                 roll_value = 1
#                 for answer in q['answers']:
#                     OracleAnswer(oracle=question, choice_text=answer, roll_value=roll_value).save()
#                     roll_value += 1

#             self.stdout.write(self.style.SUCCESS(f'Successfully imported questions and answers from {json_file}'))


from django.core.management.base import BaseCommand
import json
import glob
from oracles.models import OracleQuestion, OracleAnswer

class Command(BaseCommand):
    help = 'Import questions and answers from JSON files in a specified directory'

    def add_arguments(self, parser):
        parser.add_argument('--json_file', type=str, nargs='?', default='oracles/repository/*.json', help='Path to the JSON file or pattern containing the questions and answers')

    def handle(self, *args, **options):
        json_files = glob.glob(options['json_file'])

        for json_file in json_files:
            with open(json_file, 'r') as file:
                questions = json.load(file)

            for q in questions:
                existing_question = OracleQuestion.objects.filter(question_text=q['question']).first()
                if existing_question:
                    continue

                question = OracleQuestion(
                    question_text=q['question'],
                    category=q['category']
                )
                question.save()

            roll_value = 1
            for answer in q['answers']:
                for choice_text in answer.split(', '):
                    OracleAnswer(oracle=question, choice_text=choice_text.strip(), roll_value=roll_value).save()
                    roll_value += 1

            self.stdout.write(self.style.SUCCESS(f'Successfully imported questions and answers from {json_file}'))
