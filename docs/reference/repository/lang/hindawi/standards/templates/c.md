# {LANG} Programming Language Specification

## 1. Scope

This specification defines the syntax, semantics, and constraints of the {LANG} programming language.

## 2. Character set

Source files are encoded in Unicode.
The following characters have special meaning:
- Whitespace: space, tab, newline
- Comment start: //
- String delimiter: "
- Character delimiter: '

## 3. Lexical elements

### 3.1 Identifiers

An identifier is a sequence of letters, digits, and underscores.
The first character must be a letter or underscore.
Identifiers are case-sensitive.

### 3.2 Keywords

The following identifiers are reserved:

{KEYWORDS}

### 3.3 Literals

Integer literals: sequence of digits, optionally prefixed with 0x (hex) or 0 (octal).
Floating literals: digits with decimal point and optional exponent.
String literals: characters enclosed in double quotes.
Character literals: single character enclosed in single quotes.

### 3.4 Operators

Arithmetic: + - * / %
Comparison: == != < > <= >=
Logical: && || !
Bitwise: & | ^ ~ << >>
Assignment: = += -= *= /=

### 3.5 Delimiters

Block open: {BRACE_OPEN}
Block close: {BRACE_CLOSE}
Parentheses: ( )
Brackets: [ ]
Semicolon: ;
Comma: ,
Dot: .

## 4. Types

### 4.1 Basic types

{TYPE_INT}: integer values
{TYPE_FLOAT}: floating-point values
{TYPE_CHAR}: single characters
{TYPE_VOID}: no value

### 4.2 Derived types

Pointer: type followed by *
Array: type followed by [size]
Function: return type, name, parameter list

## 5. Declarations

### 5.1 Variable declaration

type identifier [= expression];

### 5.2 Function declaration

type identifier(parameter_list) block

### 5.3 Parameter list

Empty, or: type identifier [, type identifier]*

## 6. Statements

### 6.1 Expression statement

expression;

### 6.2 Block

{BRACE_OPEN} statement* {BRACE_CLOSE}

### 6.3 Conditional

{KW_IF} (expression) statement [{KW_ELSE} statement]

### 6.4 Loop

{KW_WHILE} (expression) statement
{KW_FOR} (init; condition; update) statement

### 6.5 Return

{KW_RETURN} [expression];

### 6.6 Break and continue

{KW_BREAK};
{KW_CONTINUE};

## 7. Expressions

### 7.1 Primary

literal | identifier | (expression)

### 7.2 Arithmetic

expression + expression
expression - expression
expression * expression
expression / expression

### 7.3 Comparison

expression == expression
expression != expression
expression < expression
expression > expression

### 7.4 Logical

expression && expression
expression || expression
! expression

### 7.5 Assignment

identifier = expression

## 8. Semantics

### 8.1 Evaluation

Expressions evaluate left to right.
Operators follow standard precedence.

### 8.2 Conditional execution

{KW_IF} evaluates the condition.
If non-zero, the first statement executes.
If zero and {KW_ELSE} present, the second statement executes.

### 8.3 Loop execution

{KW_WHILE} evaluates condition before each iteration.
Body executes while condition is non-zero.

### 8.4 Function calls

Arguments evaluate left to right.
Control transfers to function body.
{KW_RETURN} transfers control back with optional value.

## 9. Program execution

Execution begins at function {KW_MAIN}.
Program terminates when {KW_MAIN} returns.
Return value is the exit status.

## 10. Conformance

An implementation conforms if it accepts conforming programs
and produces results as specified.
