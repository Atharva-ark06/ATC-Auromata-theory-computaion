# Automata Theory & Computation

**A practical learning repository for formal languages, automata, parsing, and graph theory.**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Course](https://img.shields.io/badge/Course-Automata%20Theory-7C3AED)
![CI](https://github.com/Atharva-ark06/ATC-Auromata-theory-computaion/actions/workflows/ci.yml/badge.svg)

## Overview

This repository contains coursework, practical implementations, test evidence, and supporting documentation for Automata Theory & Computation.

The practical assignment builds progressively from deterministic state-machine recognition to lexical analysis and syntax parsing.

## Implementations

### Level 1 — DFA identifier recognition

Recognizes identifiers using explicit start, accepting, and dead states. The accepted form starts with a letter or underscore and continues with letters, digits, or underscores.

### Level 2 — MiniATC lexical analyser

Tokenizes a small teaching language into keywords, identifiers, integer literals, operators, delimiters, and unknown tokens while tracking line numbers.

### Level 3 — Lexer and recursive-descent parser

Combines lexical analysis with a recursive-descent parser for declarations, assignments, print statements, and arithmetic expressions.

## MiniATC grammar

```text
Program   -> begin StmtList end
StmtList  -> Stmt StmtList | epsilon
Stmt      -> int identifier ;
           | print ( identifier ) ;
           | identifier = Expr ;
Expr      -> Term ((+ | -) Term)*
Term      -> Factor ((* | /) Factor)*
Factor    -> identifier | number | ( Expr )
```

## Directed graph assignment

The repository also includes a directed-graph assignment, three implementation levels, execution screenshots, test-case material, and a written report.

A directed graph is represented as `G = (V, E)`, where `V` is the vertex set and `E` contains ordered pairs of vertices.

## Repository layout

```text
assignment 1/       # Level 1, Level 2, and Level 3 Python programs
tests/              # Automated regression tests
.github/workflows/  # Continuous integration and CodeQL
*.pdf, *.docx       # Assignment evidence and reports
```

## Requirements

- Python 3.10 or newer; the programs use only the Python standard library.
- Git for cloning and version control.

## Run locally

```bash
python "assignment 1/Level1.py"
python "assignment 1/Level2.py"
python "assignment 1/Level3.py"
```

Each program includes an interactive mode. Level 2 and Level 3 accept a multi-line program terminated by a line containing `###`.

## Run automated checks

```bash
python -m unittest discover -s tests -v
```

CI runs regression tests on Python 3.10–3.13 and performs Ruff static analysis.

## Quality and security

- No third-party runtime packages are required.
- Automated tests cover identifier recognition, token classification, and parser acceptance/rejection.
- Ruff checks common Python errors and suspicious constructs.
- GitHub Actions validation jobs use read-only repository permissions.
- CodeQL performs scheduled and change-triggered static analysis.
- Dependabot checks GitHub Actions dependencies for updates.
- Do not commit credentials, access tokens, private keys, personal data, or local environment files.

See [SECURITY.md](SECURITY.md) for vulnerability reporting and [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidance.

## Learning outcomes

Use these examples to connect finite-state machines, tokenization, grammar rules, parsing, and graph representations with executable programs.