import unittest


class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False

"""
Create the following project_:
•	#Cat's size is increased after eating
•	#Cat is fed after eating
•	#Cat cannot eat if already fed, raises an error
•	#Cat cannot fall asleep if not fed, raises an error
•	Cat is not sleepy after sleeping
"""
import unittest

class CatTests(unittest.TestCase):
  name = "Deni"
  fed = False
  sleepy = False
  size = 0
  #Cat's size is increased after eating
  def test_cat_size__increaced_after_eating(self):
    cat= Cat("deni")
    cat.eat()
    self.assertEqual(self.size+1, cat.size)

  #Cat is fed after eating
  def test_cat_is_fed_after_eating_return_true(self):
    cat = Cat("deni")
    cat.eat()
    self.assertEqual(True, cat.fed)

  # Cat cannot eat if already fed, raises an error
  def test_fed_true_cant_eat_again_raise_exception(self):
    cat = Cat("deni")
    cat.fed=True
    with self.assertRaises(Exception) as context:
      cat.eat()
    self.assertEqual('Already fed.', str(context.exception))

  # Cat cannot fall asleep if not fed, raises an error
  def test_cat_sleep_cant__if_not_fed__raise_error(self):
    cat = Cat("deni")
    with self.assertRaises(Exception) as context:
      cat.sleep()
    self.assertEqual('Cannot sleep while hungry', str(context.exception))

  # Cat is not sleepy after sleeping
  def test_cat_cant_sleep_after_sleeping_raise_exception(self):
    cat = Cat("deni")
    cat.fed=True
    cat.sleep()
    self.assertEqual(False, cat.sleepy)



if __name__ == "__main__":
  unittest.main()

