import json
import glob
from django.core.management.base import BaseCommand
from oracles.models import OracleQuestion, OracleAnswer

class Command(BaseCommand):
    help = 'Import questions and answers from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('--json_file', type=str, help='Path to the JSON file containing the questions and answers')

    def handle(self, **options):
        json_files = glob.glob(options['json_file'] or 'oracles/repository/*.json')
        for json_file in json_files:
            try:
                with open(json_file, 'r') as file:
                    questions = json.load(file)
                    
                for q in questions:
                    existing_question = OracleQuestion.objects.filter(question_text=q['question']).first()
                    if not existing_question:
                        question = OracleQuestion(
                            question_text=q['question'],
                            description=q.get('description', ''),
                            category=q.get('category', 'General'),
                            die=q.get('die', 'd20')
                        )
                        question.save()
                    else:
                        question = existing_question

                    for answer in q['oracle_answers']:
                        OracleAnswer.objects.update_or_create(
                            oracle=question,
                            choice_text=answer['answer'],
                            defaults={'roll_value': answer['roll_value']}
                        )
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error processing file {json_file}: {str(e)}'))

