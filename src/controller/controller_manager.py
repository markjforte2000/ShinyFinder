from time import time

from .serial_controller import SerialController


class ControllerManager(object):

    def __init__(self, port):
        self.task_list = []
        self.serial_controller = SerialController(port)
        self.error_stream = []
        self.success_stream = []
        return

    def add_task(self, button, value, delay=0):
        self.task_list.append(Task(button=button, value=value, run_time=time() + delay))

    def clear_all_tasks(self):
        self.task_list = []

    def update(self):
        """Check if any tasks are set to run then update and delete"""
        executed_tasks = []
        for task in self.task_list:
            if time() >= task.run_time:
                executed_tasks.append(task)
                # Try to execute button command
                # If fail add to error stream
                response = self.serial_controller.write_command(task.button, task.value)
                if not response[0]:
                    self.error_stream.append(
                        'Failed to write button {0} with value {1} - Got Code: {2}'.
                            format(task.button, task.value, response[1])
                    )
                else:
                    self.success_stream.append(
                        'Wrote button {0} with value {1}'.format(task.button, task.value)
                    )
        # remove all executed tasks from list
        self.task_list = [x for x in self.task_list if x not in executed_tasks]

    def get_error_stream(self):
        temp = self.error_stream
        self.error_stream = []
        return temp

    def get_success_stream(self):
        temp = self.success_stream
        self.success_stream = []
        return temp


class Task(object):

    def __init__(self, button, run_time, value):
        self.button = button
        self.run_time = run_time
        self.value = value
