# Knowledge Representation using Predicate Logic and Rule-Based System

# Facts (Predicate Logic representation)
facts = {
    "student(Pavana)",
    "studies(Pavana, Python)",
    "studies(Pavana, AI)"
}

# Rules
rules = [
    ("studies(X, Python)", "knows(X, Programming)"),
    ("studies(X, AI)", "knows(X, Artificial_Intelligence)")
]

# Display facts
print("Knowledge Base:")
for fact in facts:
    print(" ", fact)

# Apply rules
print("\nDerived Knowledge:")

if "studies(Pavana, Python)" in facts:
    print("knows(Pavana, Programming)")

if "studies(Pavana, AI)" in facts:
    print("knows(Pavana, Artificial_Intelligence)")