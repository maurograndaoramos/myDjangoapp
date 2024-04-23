from django.core.management.base import BaseCommand, CommandError
from oracles.models import OracleQuestion, OracleAnswer

class Command(BaseCommand):
    help = 'Adds a new question and its answers to the database'

    def add_arguments(self, parser):
        parser.add_argument('question_text', type=str, help='Text of the question')
        parser.add_argument('answers', nargs='+', type=str, help='List of answers')

    def handle(self, *args, **options):
        question_text = options['question_text']
        answers = options['answers']

        # Check if the question already exists to avoid duplicates
        if OracleQuestion.objects.filter(question_text=question_text).exists():
            raise CommandError('Question "{}" already exists'.format(question_text))

        # Create the new question
        question = OracleQuestion(question_text=question_text)
        question.save()

        # Add answers linked to this question
        for answer_text in answers:
            answer = OracleAnswer(question=question, answer_text=answer_text)
            answer.save()

        self.stdout.write(self.style.SUCCESS('Successfully added question and answers'))
