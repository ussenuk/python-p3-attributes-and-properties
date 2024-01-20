#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="", job=""):
        self.name = name
        self.job = job

    @property    
    def name(self):
        return self._name
    
    @property
    def job(self):
        return self._job
    
    @name.setter
    def  name(self, name):
        if isinstance(name, str) and name == "":
            print("Name must be string under 25 characters.")
            self._name = None
        elif isinstance(name, str) and len(name) < 25:
            self._name = name.title()
            print(f"{self._name}")
        else:
            print("Name must be string under 25 characters.")
            self._name = None

    @job.setter
    def job(self, job):
        if job in APPROVED_JOBS:
            print(f"{job}")
            self._job = job

        else: 
            print("Job must be in list of approved jobs.")
            self._job = None

employee = Person(name="", job="")

# employee.name = ""
# employee.job = "Finance Director"


            

