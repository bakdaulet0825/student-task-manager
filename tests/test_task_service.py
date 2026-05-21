import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from services.task_service import TaskService


class TestTaskService(unittest.TestCase):

    def setUp(self):

        self.service = TaskService()

        self.service.tasks = []

    def test_add_task(self):

        self.service.add_task(
            "Math",
            "Homework"
        )

        self.assertEqual(
            len(self.service.tasks),
            1
        )

    def test_delete_task(self):

        self.service.add_task(
            "Math",
            "Homework"
        )

        self.service.delete_task(0)

        self.assertEqual(
            len(self.service.tasks),
            0
        )

    def test_complete_task(self):

        self.service.add_task(
            "Math",
            "Homework"
        )

        self.service.complete_task(0)

        self.assertTrue(
            self.service.tasks[0]["completed"]
        )


if __name__ == "__main__":
    unittest.main()

print("TESTS WORKING")