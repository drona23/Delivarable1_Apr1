from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld

# Persona 1: Strict Professor
drona = TinyPerson("Drona")
drona.define("age", 25)
drona.define("nationality", "Indian")
drona.define("occupation", "A no-nonsense professor who hates excuses.")

# Persona 2: Lazy Student
reddy = TinyPerson("Reddy")
reddy.define("age", 20)
reddy.define("nationality", "American")
reddy.define("occupation", "A student who always procrastinates.")

# Create a world (e.g., "Office Hours" scenario)
world = TinyWorld("Office Hours", [drona, reddy])
world.make_everyone_accessible()

# Trigger conflict: Reddy asks for a favor
reddy.listen("Can you raise my grade? I partied all semester but need a B to keep my scholarship.")
world.run(10)  