import os
import unittest

import pq


def silent_output(output):
    pass


pq.print_output = silent_output


class ExampleTests(unittest.TestCase):
    def setUp(self):
        self.examples = {}
        current_path = os.path.dirname(os.path.realpath(__file__))
        example_dirs_path = current_path + '/examples/'
        examples = os.listdir(example_dirs_path)
        self.parse_examples(examples, example_dirs_path)

    def parse_examples(self, examples, example_dirs_path):
        for filename in examples:
            if '_formatted' in filename:
                continue
            period = filename.find('.')
            formatted_filename = filename[:period] + \
                '_formatted' + \
                filename[period:]
            if formatted_filename in examples:
                filename = example_dirs_path + filename
                formatted_filename = example_dirs_path + formatted_filename
                self.examples[filename] = formatted_filename

    @staticmethod
    def read_file(filename):
        with open(filename, 'r') as handle:
            return handle.read()

    def test_example(self):
        for case, answer in self.examples.items():
            case_data = ExampleTests.read_file(case)
            answer_data = ExampleTests.read_file(answer)
            pq_output = pq.format_parens(case_data)
            self.assertEqual(pq_output, answer_data)
