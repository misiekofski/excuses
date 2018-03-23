from django.test import TestCase
from .models import RootCause
from django.urls import reverse

def create_excuse(cause_text):
    """
    Create an excuse with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    return RootCause.objects.create(cause_text=cause_text)

# Create your tests here.
class RootCauseModelTest(TestCase):
    
    def test_rootcause_has_no_actionplan(self):
        self.assertIs(True, False)

class QuestionIndexViewTests(TestCase):
    def test_no_excuses(self):
        """
        If no excuses exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No excuses are available.")
        self.assertQuerysetEqual(response.context['latest_excuses_list'], [])        
