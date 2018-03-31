import unittest

from tests.markdown_builder import MarkdownBuilder
from tests.test_plantuml import PlantumlTest


class PlantumlTest_fenced(PlantumlTest):

    def setUp(self):
        super().setUp()
        # Setup testing with backticks fenced block delimiter
        self.text_builder = MarkdownBuilder()

    def test_tildes(self):
        """
        Test correct parsing with tilde fenced block delimiter
        """
        self.text_builder = MarkdownBuilder('~~~uml')
        text = self.text_builder.text('Paragraph before.\n\n')\
                                .diagram('A --> B')\
                                .text('\nParagraph after.')\
                                .build()
        self.assertEqual('<p>Paragraph before.</p>\n'
                         '<p><img alt="uml diagram" classes="uml" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAE8AAABwCAIAAADQerqpAAAANXRFWHRjb3B5bGVmdABHZW5lcmF0ZWQgYnkgaHR0cDovL3BsYW50dW1sLnNvdXJjZWZvcmdlLm5ldDpnVRsAAAC5elRYdHBsYW50dW1sAAB4nB2NywrCMBQF94H+w1m2i0pStT4W4oOiSAti1a2kNouAvZH0pvj5SrdnZjjbnrXn0L0jsUOabrCPRCS2htpxE5e3Jr5XJQbje+sISzmdxbVmnDVBrqDUWi7W8xUOxQ2ZVHki4uOlRO+Cfxm0tmdvm8D/NhFnPej4ViWoC1wDse0MChqsd9QZ4pHj5Lj+OB69fJbuLaM2/v+PRyXUZDmRT5VnaaMyUVoK3x+7CDnw3p6twQAABChJREFUeNrtm19IU1Ecx2+arTWMIB+kSER7CYUiIcvM8imKQhYRJmIhgx58FhUkjdCI5rKHwBq1TWO5ubg5EkdyUzBHW9nAoMagRpamLnH+ycYS7ac3wvyzO3fvzm3b78d5uAzO/Z7P+b97zpdaiKWgkHbBPzE12t0vSPJ7pzkLQUxubVrI1kodEiSN9fRz0hKTC0TrvK0c7W4NOTlVyg3REpALRAuvmJ9/G3IaedG6IVoCcmGntajUVqvV4XC4XK6hoaHJyUkR5cJOa6xtMJvNDMPY7XYogcfjEVEu7LQtVfV6vZ6maSgBVDnUt4hyYadtrqzTarVQAqhy6GNut1tEubDTGmqUIK/T6YxGI9Q39C4R5ZAWaVcktfoqRVGNjeXhpk1K2kEtRXx8XGKiTKGQj4/3kKbNzT1QWHgyK2sfAVqd7jr77HZ3ZGSkl5VdIErrcrUnJGyGOpZKJQMDRmK0kEpLC+TyfKK01dUKVrKk5Ex5+SVitE4nnZq6S6O5RpQ2JSXZYLgJDxbL3eTknWTGLRvFxadnZ1+Ro2WYezKZ1O9/Dc9zc2+gNMBMpm293l7oyTk5+8nRQu+l/o2iolPExu3U1EtQ7O19SIJ2ZsYK81Nfn/bvLzZbC/wChSBJC/2LBC0sszBoV/yYlra7qamaAC3UNay3UAAYQSRoYZmtqLi8eopecywJPktJJFsKCk7A+oc7R6RFWqRFWqRFWqSNAFqnSgmvCDmxBzPB0xKQC/sZX/C0BOTWOb/1To/19LPJolIbaxtaquqbK+vgXRtOmmZOWmJy3GfzVqvVbDbr9Xotjwh8VkBMjpvW4XBAJdE0Da/QhRSc50DE5LhpoTPY7XbIDLVlDCk4z/iIyXHTQvVANqgn6BjMqtBcqWK4gvP8lpgcNy1kgBqCnDAGXKviTsJBF1dARsgOL4FX+Xw+EeX43iCCSZ/kFSCeckiLtOvFu5r7JGl5yuHNP6RF2tijja1ZSpAV6MeX0Y/qpz+/fY+V9Xa407p4b09ydNDIxMTu4vPj5+z3B5PsuE1R5/NMRPleaqTLZkrMN0mPLWLHZXdmFq5o6mjbS7HAT7bn//nOtCl7eVOLPEuBPJSJLYRQz12HS5d/WDNty2MfBtuYaFtvv9LdhvgjLF7H3nPmPWefpcvf39CuOYwjm5ZFbZPmdWZehP7cd74SOvb8r7ko3Et9etDONqmAjfmfzlLsetu2NTdwY0bJXurDrUcz7mH8doG0SIv/+PDfPNIiLdLid6lIW4GCN7Iv3fwh55vnKYe+efTNo28effPom0ffvDhyeGMXadE3j7559M2jbz4UWvTNo28effOh0KJvHn3z6JvHfTLSIi3SIi3SIi3Som8effPom0ffPPrmycrx9c0HEwL65nnK8fXNBxMC+uZ5yuHtMKRF2siL3/yLy5JOUvXZAAAAAElFTkSuQmCC" title="" /></p>\n'
                         '<p>Paragraph after.</p>',
                         self.md.convert(text))

    def test_plantuml(self):
        """
        Test the support of 'plantuml' language
        """
        text = MarkdownBuilder('```plantuml').diagram('A --> B').build()
        self.assertEqual(self._load_file('png_diag.html'), self.md.convert(text))

    def test_extended_header(self):
        """
        Test the extended syntax header
        """
        text = self.text_builder.diagram('A --> B').extended_syntax().title('Diagram test').build()
        self.assertTrue('```{uml' in text) # Check the presence of extended syntax
        self.assertEqual(
            '<p><img alt="uml diagram" classes="uml" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAE8AAABwCAIAAADQerqpAAAANXRFWHRjb3B5bGVmdABHZW5lcmF0ZWQgYnkgaHR0cDovL3BsYW50dW1sLnNvdXJjZWZvcmdlLm5ldDpnVRsAAAC5elRYdHBsYW50dW1sAAB4nB2NywrCMBQF94H+w1m2i0pStT4W4oOiSAti1a2kNouAvZH0pvj5SrdnZjjbnrXn0L0jsUOabrCPRCS2htpxE5e3Jr5XJQbje+sISzmdxbVmnDVBrqDUWi7W8xUOxQ2ZVHki4uOlRO+Cfxm0tmdvm8D/NhFnPej4ViWoC1wDse0MChqsd9QZ4pHj5Lj+OB69fJbuLaM2/v+PRyXUZDmRT5VnaaMyUVoK3x+7CDnw3p6twQAABChJREFUeNrtm19IU1Ecx2+arTWMIB+kSER7CYUiIcvM8imKQhYRJmIhgx58FhUkjdCI5rKHwBq1TWO5ubg5EkdyUzBHW9nAoMagRpamLnH+ycYS7ac3wvyzO3fvzm3b78d5uAzO/Z7P+b97zpdaiKWgkHbBPzE12t0vSPJ7pzkLQUxubVrI1kodEiSN9fRz0hKTC0TrvK0c7W4NOTlVyg3REpALRAuvmJ9/G3IaedG6IVoCcmGntajUVqvV4XC4XK6hoaHJyUkR5cJOa6xtMJvNDMPY7XYogcfjEVEu7LQtVfV6vZ6maSgBVDnUt4hyYadtrqzTarVQAqhy6GNut1tEubDTGmqUIK/T6YxGI9Q39C4R5ZAWaVcktfoqRVGNjeXhpk1K2kEtRXx8XGKiTKGQj4/3kKbNzT1QWHgyK2sfAVqd7jr77HZ3ZGSkl5VdIErrcrUnJGyGOpZKJQMDRmK0kEpLC+TyfKK01dUKVrKk5Ex5+SVitE4nnZq6S6O5RpQ2JSXZYLgJDxbL3eTknWTGLRvFxadnZ1+Ro2WYezKZ1O9/Dc9zc2+gNMBMpm293l7oyTk5+8nRQu+l/o2iolPExu3U1EtQ7O19SIJ2ZsYK81Nfn/bvLzZbC/wChSBJC/2LBC0sszBoV/yYlra7qamaAC3UNay3UAAYQSRoYZmtqLi8eopecywJPktJJFsKCk7A+oc7R6RFWqRFWqRFWqSNAFqnSgmvCDmxBzPB0xKQC/sZX/C0BOTWOb/1To/19LPJolIbaxtaquqbK+vgXRtOmmZOWmJy3GfzVqvVbDbr9Xotjwh8VkBMjpvW4XBAJdE0Da/QhRSc50DE5LhpoTPY7XbIDLVlDCk4z/iIyXHTQvVANqgn6BjMqtBcqWK4gvP8lpgcNy1kgBqCnDAGXKviTsJBF1dARsgOL4FX+Xw+EeX43iCCSZ/kFSCeckiLtOvFu5r7JGl5yuHNP6RF2tijja1ZSpAV6MeX0Y/qpz+/fY+V9Xa407p4b09ydNDIxMTu4vPj5+z3B5PsuE1R5/NMRPleaqTLZkrMN0mPLWLHZXdmFq5o6mjbS7HAT7bn//nOtCl7eVOLPEuBPJSJLYRQz12HS5d/WDNty2MfBtuYaFtvv9LdhvgjLF7H3nPmPWefpcvf39CuOYwjm5ZFbZPmdWZehP7cd74SOvb8r7ko3Et9etDONqmAjfmfzlLsetu2NTdwY0bJXurDrUcz7mH8doG0SIv/+PDfPNIiLdLid6lIW4GCN7Iv3fwh55vnKYe+efTNo28effPom0ffvDhyeGMXadE3j7559M2jbz4UWvTNo28effOh0KJvHn3z6JvHfTLSIi3SIi3SIi3Som8effPom0ffPPrmycrx9c0HEwL65nnK8fXNBxMC+uZ5yuHtMKRF2siL3/yLy5JOUvXZAAAAAElFTkSuQmCC" title="Diagram test" /></p>',
            self.md.convert(text))


if __name__ == '__main__':
    unittest.main()