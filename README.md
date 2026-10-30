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