import unittest


class StepCounter:
    """Class for counting steps"""

    def __init__(self):
        self.current_steps = 0
        self.step_goal = None
        self.goal_passed = False

    def add_step(self) -> None:
        self.current_steps += 1
        if self.current_steps == self.step_goal:
            self.goal_reached()

    def sub_step(self) -> None:
        self.current_steps -= 1

    def set_goal(self, goal: int) -> None:
        self.step_goal = goal

    def goal_reached(self) -> None:
        print("Good Job!")
        self.goal_passed = True


class TestStepCounter(unittest.TestCase):

    def test_init(self):
        """Confirm Step Counter initailiazes as expected"""
        step_counter = StepCounter()
        self.assertEqual(step_counter.current_steps, 0)
        self.assertIsNone(step_counter.step_goal)
        self.assertFalse(step_counter.goal_passed)

    def test_step_movement(self):
        """Confirm Step counter movement methods functionality"""
        step_counter = StepCounter()
        step_counter.add_step()
        self.assertEqual(step_counter.current_steps, 1)
        step_counter.sub_step()
        self.assertEqual(step_counter.current_steps, 0)

    def test_set_and_reach_goal(self):
        """Confirm goals can be set and class marks them as passed"""
        step_counter = StepCounter()
        step_counter.set_goal(2)
        step_counter.add_step()
        step_counter.add_step()
        self.assertTrue(step_counter.goal_passed)


if __name__ == "__main__":
    unittest.main()
