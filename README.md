# 🧠 Automata Theory & Computation

<p align="center">

<img src="https://img.shields.io/badge/Automata-Theory-7C3AED?style=for-the-badge&logo=thealgorithms&logoColor=white" />

<img src="https://img.shields.io/badge/Theory%20of-Computation-2563EB?style=for-the-badge&logo=academia&logoColor=white" />

<img src="https://img.shields.io/badge/Graph-Theory-0891B2?style=for-the-badge&logo=graphql&logoColor=white" />
 
<img src="https://img.shields.io/badge/Academic-Project-F59E0B?style=for-the-badge&logo=bookstack&logoColor=white" />

</p>
 
<p align="center">
  <strong>⚙️ From Finite Automata to Directed Graphs — Exploring the Theory Behind Computation.</strong>
</p>

---

# 🚀  Overview

**Automata Theory & Computation (ATC)** is a foundational area of Computer Science that explores mathematical models of computation and the theoretical limits of machines.

This repository brings together my **ATC learning materials, practical assignments, implementations, test cases, screenshots, and documentation** in one place.

The repository also contains a practical assignment on:

> **Directed Graphs (Digraphs) and Their Real-World Applications**

The assignment explores graph concepts through multiple implementation levels, supported by test cases, outputs, screenshots, and a formal report.

---

# 🧩 What You'll Find Here

```text
                    🧠 ATC
                     │
          ┌──────────┼──────────┐
          │          │          │
          ▼          ▼          ▼
      📚 Theory    💻 Code    📊 Graphs
          │          │          │
          ▼          ▼          ▼
      Concepts    Levels     Digraphs
          │          │          │
          └──────────┼──────────┘
                     │
                     ▼
              📝 Documentation
                     │
                     ▼
              🎯 Practical Learning
```

### Repository includes:

* 📚 Automata Theory & Computation notes
* 🧮 Directed Graph assignment
* 💻 Multiple implementation levels
* 🧪 Test cases
* 📸 Execution screenshots
* 📄 Assignment report
* 📑 Output documentation
* 🗂️ Supporting academic material

---

# 📚 Automata Theory

Automata Theory provides mathematical models for understanding how machines process input and recognize languages.

The major concepts covered in ATC include:

### 🔹 Finite Automata

```text
Input String
     │
     ▼
┌─────────┐
│ Initial │
│  State  │
└────┬────┘
     │
     ▼
┌─────────┐
│ State   │
│Transition
└────┬────┘
     │
     ▼
┌─────────┐
│ Accept /│
│ Reject  │
└─────────┘
```
Topics include:

* DFA — Deterministic Finite Automata
* NFA — Non-Deterministic Finite Automata
* ε-NFA
* Regular Languages
* Regular Expressions
* State Transitions
* Automata Conversion

---

# 🔄 Automata Hierarchy

```text
               COMPUTATIONAL MODELS
                         │
                         ▼
               ┌──────────────────┐
               │ Finite Automata  │
               │       FA         │
               └────────┬─────────┘
                        │
                        ▼
               ┌──────────────────┐
               │ Pushdown Automata│
               │       PDA        │
               └────────┬─────────┘
                        │
                        ▼
               ┌──────────────────┐
               │ Turing Machine   │
               │       TM         │
               └────────┬─────────┘
                        │
                        ▼
                General Computation
```

---

# 🧠 Core ATC Concepts

| Concept                   | Description                                  |
| ------------------------- | -------------------------------------------- |
| 🔤 **Alphabet**           | Finite set of symbols                        |
| 🧵 **String**             | Sequence of symbols                          |
| 📖 **Language**           | Set of strings                               |
| ⚙️ **DFA**                | Deterministic finite automaton               |
| 🔀 **NFA**                | Non-deterministic finite automaton           |
| ε                         | Empty-string transition                      |
| 🧮 **Regular Expression** | Pattern representation of regular languages  |
| 🧱 **CFG**                | Context-Free Grammar                         |
| 📚 **PDA**                | Pushdown Automaton                           |
| 🧠 **TM**                 | Turing Machine                               |
| ♾️ **Decidability**       | Study of what can be algorithmically decided |

---

# 🕸️ Directed Graphs

One of the major practical components of this repository is the **Directed Graph / Digraph assignment**.

A directed graph consists of:

```text
G = (V, E)
```

where:

* `V` → Set of vertices
* `E` → Set of directed edges

Unlike an undirected graph, every edge has a **specific direction**.

---

# 🔗 Directed Graph Example

```text
        ┌───────┐
        │   A   │
        └───┬───┘
            │
            ▼
        ┌───────┐
        │   B   │
        └───┬───┘
            │
       ┌────┴────┐
       ▼         ▼
   ┌───────┐ ┌───────┐
   │   C   │ │   D   │
   └───────┘ └───┬───┘
                 │
                 ▼
             ┌───────┐
             │   E   │
             └───────┘
```

The arrows represent the direction of relationships between vertices.

---

# 🌍 Real-World Applications

Directed graphs are everywhere.

### 🌐 Computer Networks

```text
Router A → Router B → Router C
```

Used to represent packet-routing paths.

### 🗺️ Navigation

```text
City A → City B → City C
```

Used for one-way roads and route planning.

### 🔗 Web Pages

```text
Page A → Page B
Page A → Page C
Page C → Page D
```

Hyperlinks naturally form directed graphs.

### 👥 Social Networks

```text
User A → follows → User B
```

Useful for representing follower relationships.

### 📦 Dependency Systems

```text
Library A
    ↓
Library B
    ↓
Library C
```

Used in package managers and software dependency graphs.

### 📱 Recommendation Systems

```text
User
 ↓
Interaction
 ↓
Content
 ↓
Recommendation
```

---

# 💻 Implementation Levels

The Directed Graph assignment contains implementations organized across **three levels**, allowing the problem to be developed progressively.

```text
LEVEL 1
   │
   ▼
Basic Graph Representation
   │
   ▼
LEVEL 2
   │
   ▼
Graph Operations & Processing
   │
   ▼
LEVEL 3
   │
   ▼
Advanced / Application-Oriented Implementation
```

This progressive structure makes it easier to understand how graph-based solutions evolve from basic representation to more complete implementations.

---

# 🧪 Testing & Validation

The repository includes dedicated test-case documentation and execution evidence.

The testing workflow follows :

```text
        Input
          │
          ▼
   ┌──────────────┐
   │ Graph / Data │
   └──────┬───────┘
          │
          ▼
    Algorithm
          │
          ▼
    Processing
          │
          ▼
      Output
          │
          ▼
   ┌──────────────┐
   │ Test Result  │
   └──────────────┘
```

Test cases are included to verify the correctness of the implementation and expected outputs.

---

# 📸 Execution Evidence

The repository contains screenshots documenting the implementation and execution results.

These provide visual verification of:

* Program execution
* Input handling
* Output generation
* Assignment implementation
* Test-case results

---

# 📄 Documentation

The project includes a formal assignment report:

```text
Directed_Graphs_Assignment_Report.docx
```

The repository also contains supporting PDF documentation and test-case material.

---

# 📁 Repository Structure

```text
ATC-Auromata-theory-computaion/
│
├── 📁 .vscode/
│
├── 📁 assignment 1/
│   │
│   ├── 💻 Level 1
│   ├── 💻 Level 2
│   └── 💻 Level 3
│
├── 📄 Directed_Graphs_Assignment_Report.docx
│
├── 📄 OUTPUT FOR LEVEL.pdf
│
├── 📄 U24E01IY036_ATC_A1_Screenshot1.png
│
├── 📄 U24E01IY036_ATC_A1_Screenshot2.png
│
├── 📄 U24E01IY036_ATC_A1_Testcases..pdf
│
└── 📄 README.md
```

The current GitHub repository contains these folders and assignment artifacts.

---

# ⚡ Learning Roadmap

```text
                 START
                   │
                   ▼
          ┌────────────────┐
          │ Basic Concepts │
          └───────┬────────┘
                  ▼
          ┌────────────────┐
          │ Finite Automata│
          └───────┬────────┘
                  ▼
          ┌────────────────┐
          │ Regular        │
          │ Languages      │
          └───────┬────────┘
                  ▼
          ┌────────────────┐
          │ CFG & PDA      │
          └───────┬────────┘
                  ▼
          ┌────────────────┐
          │ Turing Machine │
          └───────┬────────┘
                  ▼
          ┌────────────────┐
          │ Graph Theory   │
          └───────┬────────┘
                  ▼
          ┌────────────────┐
          │ Practical Code │
          └───────┬────────┘
                  ▼
                🧠
         Computational Thinking
```

---

# 🛠️ Technologies & Concepts

<p align="center">

<img src="https://img.shields.io/badge/Automata%20Theory-7C3AED?style=flat-square" />
<img src="https://img.shields.io/badge/Graph%20Theory-0891B2?style=flat-square" />
<img src="https://img.shields.io/badge/Algorithms-F59E0B?style=flat-square" />
<img src="https://img.shields.io/badge/Data%20Structures-10B981?style=flat-square" />
<img src="https://img.shields.io/badge/Computation-2563EB?style=flat-square" />

</p>

---

# 🎯 Learning Outcomes

After working through this repository, you should have a stronger understanding of:

* 🧠 Computational models
* 🔤 Formal languages
* ⚙️ Finite automata
* 🔀 DFA/NFA behavior
* 🧱 Context-free grammars
* 📚 Pushdown automata
* 🖥️ Turing machines
* 🕸️ Directed graph structures
* 🔗 Graph relationships
* 🧪 Algorithm testing
* 💻 Translating theory into implementation

---

# 📌 Why This Repository?

Theory becomes much easier when it is connected to implementation.

This repository follows a simple philosophy:

```text
        THEORY
          │
          ▼
      UNDERSTAND
          │
          ▼
     IMPLEMENT
          │
          ▼
       TEST
          │
          ▼
      VISUALIZE
          │
          ▼
        LEARN
```

Instead of treating Automata Theory as purely mathematical, the project connects **concepts → algorithms → code → outputs → real-world applications**.

---

# 🔮 Future Improvements

Potential future additions include:

* 🧩 Interactive DFA/NFA simulator
* 🎨 Automata visualization
* 🕸️ Interactive directed graph visualizer
* 🔄 Step-by-step graph traversal
* 🧪 Automated test framework
* 📊 Algorithm complexity analysis
* 🧠 Turing Machine simulator
* 🌐 Web-based ATC learning platform
* 🤖 AI-powered ATC problem solver

---

# 🎓 Academic Information

**Course:** Automata Theory & Computation
**Project:** Directed Graphs & Real-World Applications
**Type:** Academic Assignment / Learning Repository
**Academic Year:** 2026–27

---

# 👨‍💻 Author

<p align="center">

<strong>ATHARVA KULKARNI</strong>

<br>

Computer Science • Cyber Security • AI/ML • Networking

<br><br>

<a href="https://github.com/Atharva-ark06">
<img src="https://img.shields.io/badge/GitHub-Atharva--ark06-181717?style=for-the-badge&logo=github" />
</a>

</p>

---



<p align="center">

## 🧠 Think Formally. Build Practically. Compute Infinitely.

<strong>Automata Theory & Computation</strong>

<br><br>

<sub>Turning computational theory into practical understanding.</sub>

</p>
