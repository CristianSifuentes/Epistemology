import cmath
from contextlib import contextmanager

#Base class for the knowLedge object
class KnowledgeObject:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return f"Knowledge object: {self._name}"
    
    def knowledge(self):
        pass


class ConcreteObject(KnowledgeObject):
    def knowledge(self):
        return "Concrete knowledge acquired."
    

class AbstractObject(KnowledgeObject):
    def knowledge(self):
        return "Abstract knowledge acquired."


# CognizantSubject class with magic methods and complex number
class CognizantSubject:
    def __init__(self, name, skill):
        self.name = name
        self._skill = skill #protected attribute
        self.knowledge_base  = []

    def __str__(self):
        return f"Cognizant subject:  {self.name} with skill {self._skill}"
    
    def learn(self, knowledge_object):
        knowledge = knowledge_object.knowledge()
        self.knowledge_base.append(knowledge)
        return knowledge

    # Magic method to combine skills
    def __add__(self, other):
        return CognizantSubject(f"{self.name} and {other.name}", self._skill + other._skill)

# Decorator to log learning process
def log_learning(func):
    def wrapper(*args, **kwargs):
        print(f"Starting learning process of {args[1]._name}...")
        result = func(*args, **kwargs)
        print(f"args[0].name learned: {result}")
        return result
    return wrapper

# Context manager for learning sessions
@contextmanager
def learning_session(subject):
    print(f"Starting session for {subject.name}")
    yield
    print(f"Ending session for {subject.name}")

# Generator to create new ideas
def idea_generator():
    concepts = ["Idea 1", "Idea 2", "Idea 3"]
    for concept in concepts:
        yield concept


# Execution of the project
subject = CognizantSubject("Analyzer", cmath.sqrt(1 + 2j))
concrete_object = ConcreteObject("Tree")
abstract_object = AbstractObject("Justice")

with learning_session(subject):
    subject.learn(concrete_object)
    subject.learn(abstract_object)

for idea in idea_generator():
    print(f"Generating new idea: {idea}")