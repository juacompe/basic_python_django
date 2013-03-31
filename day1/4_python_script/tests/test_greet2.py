from unittest import TestCase
import greet2

echo_log = []

def mocked_echo(message):
    echo_log.append(message)

class TestMain(TestCase):
    def setUp(self):
        self.original_echo = greet2.echo
        greet2.echo = mocked_echo

    def tearDown(self):
        greet2.echo = self.original_echo

    def assertEcho(self, message):
        print echo_log
        self.assertEqual(message, echo_log.pop())

    def test_greet_john_with_argument(self):
        command = './greet2 John'
        argv = command.split()
        status_code = greet2.main(argv)
        self.assertEcho('Hi John!')
        self.assertEqual(0, status_code)

    def test_greet_with_no_arguments(self):
        command = './greet2'
        argv = command.split()
        status_code = greet2.main(argv)
        self.assertEcho(greet2.USAGE)
        self.assertEqual(1, status_code)

    def test_greet_jack_with_short_option(self):
        command = './greet2 -nJack'
        argv = command.split()
        status_code = greet2.main(argv)
        self.assertEcho('Hi Jack!')
        self.assertEqual(0, status_code)

    def test_greet_jim_with_short_option_with_space(self):
        command = './greet2 -n Jim'
        argv = command.split()
        status_code = greet2.main(argv)
        self.assertEcho('Hi Jim!')
        self.assertEqual(0, status_code)

    def test_greet_joe_with_long_option(self):
        command = './greet2 --name=Joe'
        argv = command.split()
        status_code = greet2.main(argv)
        self.assertEcho('Hi Joe!')
        self.assertEqual(0, status_code)

    def test_argument_has_priority_over_option(self):
        command = './greet2 -nJim --name=Joe Jack'
        argv = command.split()
        status_code = greet2.main(argv)
        self.assertEcho('Hi Jack!')
        self.assertEqual(0, status_code)

    def test_long_vs_short_options(self):
        command = './greet2 -nJim --name=Joe'
        argv = command.split()
        status_code = greet2.main(argv)
        self.assertEcho('Hi Joe!')
        self.assertEqual(0, status_code)

    def test_many_short_options(self):
        command = './greet2 -nJim -nJoe -nJua'
        argv = command.split()
        status_code = greet2.main(argv)
        self.assertEcho('Hi Jua!')
        self.assertEqual(0, status_code)

