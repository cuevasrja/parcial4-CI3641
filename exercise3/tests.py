import unittest
from simulator import Simulator, ClassType

class TestSimulator(unittest.TestCase):
    def setUp(self):
        """
        This method is called before each test.
        It sets up the test environment.
        Here, it creates a new instance of the Simulator class.
        """
        self.simulador = Simulator()

    def test_class_creation_with_valid_data(self):
        """
        This test checks if a class can be created with valid data.
        Adds a class with name "C" and methods "i" and "j".
        Then it checks if the class was created and if the methods are correct.
        """
        self.simulador.add_class("C", ["i", "j"])
        self.assertIsInstance(self.simulador.classes["C"], ClassType)
        self.assertEqual(self.simulador.classes["C"].get_method("i"), "C :: i")
        self.assertEqual(self.simulador.classes["C"].get_method("j"), "C :: j")

    def test_class_creation_with_existing_name(self):
        """
        This test checks if a class can be created with an existing name.
        First, it adds a class with name "J" and methods "k" and "l".
        Then it tries to add another class with the same name "J" and a different method "b".
        It checks if the number of classes is still 1, meaning the second class was not added.
        """
        self.simulador.add_class("J", ["k", "l"])
        self.simulador.add_class("J", ["b"])
        self.assertEqual(len(self.simulador.classes), 1)

    def test_class_creation_with_non_existing_superclass(self):
        """
        This test checks if a class can be created with a non-existing superclass.
        It tries to add a class with name "D", methods "m" and "n", and superclass "Z".
        It checks if the number of classes is still 0, meaning the class was not added.
        """
        self.simulador.add_class("D", ["m", "n"], "Z")
        self.assertEqual(len(self.simulador.classes), 0)

    def test_class_creation_with_duplicate_methods(self):
        """
        This test checks if a class can be created with duplicate methods.
        It tries to add a class with name "E" and duplicate methods "o".
        It checks if the number of classes is still 0, meaning the class was not added.
        """
        self.simulador.add_class("E", ["o", "o"])
        self.assertEqual(len(self.simulador.classes), 0)

    def test_class_creation_with_self_inheritance(self):
        """
        This test checks if a class can be created with self-inheritance.
        It tries to add a class with name "F", methods "p" and "q", and superclass "F" (the same class).
        It checks if the number of classes is still 0, meaning the class was not added.
        """
        self.simulador.add_class("F", ["p", "q"], "F")
        self.assertEqual(len(self.simulador.classes), 0)

    def test_describe_non_existing_class(self):
        """
        This test checks if a non-existing class can be described.
        It tries to describe a class with name "Z" that does not exist.
        It checks if the result is None, meaning the class does not exist.
        """
        self.assertIsNone(self.simulador.describe_class("Z"))

    def test_describe_class_without_methods(self):
        """
        This test checks if a class without methods can be described.
        Adds a class with name "G" without methods.
        Then it tries to describe the class.
        It checks if the result is "The class G has no methods.", meaning the class has no methods.
        """
        self.simulador.add_class("G", [])
        self.assertEqual(self.simulador.describe_class("G"), "The class G has no methods.")

    def test_describe_class_example_exam(self):
        """
        This test checks the behavior of describing a class with a superclass.
        First, it creates a class "A" with methods "f" and "g".
        Then it creates a class "B" with methods "f" and "h", and with "A" as superclass.
        It checks that the methods of "B" are correct and that it correctly inherits the methods of "A".
        Finally, it checks the description of classes "A" and "B".
        """
        self.simulador.add_class("A", ["f", "g"])
        self.assertIsInstance(self.simulador.classes["A"], ClassType)
        self.assertEqual(self.simulador.classes["A"].get_method("f"), "A :: f")
        self.assertEqual(self.simulador.classes["A"].get_method("g"), "A :: g")
        self.simulador.add_class("B", ["f", "h"], "A")
        self.assertIsInstance(self.simulador.classes["B"], ClassType)
        self.assertEqual(self.simulador.classes["B"].get_method("g"), "A :: g")
        self.assertEqual(self.simulador.classes["B"].get_method("h"), "B :: h")
        self.assertEqual(self.simulador.classes["B"].get_method("f"), "B :: f")
        self.assertEqual(self.simulador.describe_class("A"), "f -> A :: f\ng -> A :: g")
        self.assertEqual(self.simulador.describe_class("B"), "f -> B :: f\nh -> B :: h\ng -> A :: g")

    def test_class_creation_without_methods(self):
        """
        This test checks if a class can be created without methods.
        It creates a class "H" without methods and checks that it was created correctly.
        """
        self.simulador.add_class("H", [])
        self.assertIsInstance(self.simulador.classes["H"], ClassType)

    def test_class_creation_with_superclass_having_methods(self):
        """
        This test checks if a class can be created with a superclass that has methods.
        First, it creates a class "C" with methods "i" and "j".
        Then it creates a class "I" with methods "r" and "s", and with "C" as superclass.
        It checks that the methods of "I" are correct and that it correctly inherits the methods of "C".
        """
        self.simulador.add_class("C", ["i", "j"])
        self.simulador.add_class("I", ["r", "s"], "C")
        self.assertIsInstance(self.simulador.classes["I"], ClassType)
        self.assertEqual(self.simulador.classes["I"].get_method("r"), "I :: r")
        self.assertEqual(self.simulador.classes["I"].get_method("s"), "I :: s")

    def test_class_creation_with_superclass_without_methods(self):
        """
        This test checks if a class can be created with a superclass that has no methods.
        First, it creates a class "H" without methods.
        Then it creates a class "J" with methods "t" and "u", and with "H" as superclass.
        It checks that the methods of "J" are correct.
        """
        self.simulador.add_class("H", [])
        self.simulador.add_class("J", ["t", "u"], "H")
        self.assertIsInstance(self.simulador.classes["J"], ClassType)
        self.assertEqual(self.simulador.classes["J"].get_method("t"), "J :: t")
        self.assertEqual(self.simulador.classes["J"].get_method("u"), "J :: u")

    def test_describe_class_with_superclass_having_methods(self):
        """
        This test checks the description of a class with a superclass that has methods.
        First, it creates a class "C" with methods "i" and "j".
        Then it creates a class "M" with methods "y" and "z", and with "C" as superclass.
        Finally, it checks the description of the class "M".
        """
        self.simulador.add_class("C", ["i", "j"])
        self.simulador.add_class("M", ["y", "z"], "C")
        self.assertEqual(self.simulador.describe_class("M"), "y -> M :: y\nz -> M :: z\ni -> C :: i\nj -> C :: j")

    def test_describe_class_with_superclass_without_methods(self):
        """
        This test checks the description of a class with a superclass that has no methods.
        First, it creates a class "H" without methods.
        Then it creates a class "N" with methods "a" and "b", and with "H" as superclass.
        Finally, it checks the description of the class "N".
        """
        self.simulador.add_class("H", [])
        self.simulador.add_class("N", ["a", "b"], "H")
        self.assertEqual(self.simulador.describe_class("N"), "a -> N :: a\nb -> N :: b")

if __name__ == '__main__':
    unittest.main()