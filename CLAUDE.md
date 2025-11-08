# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Toy Computer** is an educational assembly language simulator designed for teaching computer programming fundamentals. It implements a simplified CPU with registers, memory, and a custom assembly instruction set. The project includes both a console-based executor and a web-based interface.

The system is intentionally simplified to help students understand:
- How CPUs execute instructions
- Register and memory operations
- Stack-based function calls and frames
- The relationship between high-level code and assembly

## Build and Development Commands

### Environment Setup
```bash
# Install dependencies using uv (Python package manager)
uv sync

# Activate virtual environment
source .venv/bin/activate  # On macOS/Linux
```

### Running Programs

```bash
# Run an assembly program (console mode)
python src/console_executor/main.py <filename.asm>

# Run in step-by-step debug mode (executes one instruction at a time with dump)
python src/console_executor/main.py <filename.asm> --step
python src/console_executor/main.py <filename.asm> -s

# Run web server (for browser-based interface)
python src/web_backend/webserver.py
```

### Testing
Test assembly programs are located in:
- `src/tests/*.asm` - Basic test programs
- `src/tests/nj/*.asm` - More complex examples (fibonacci, prime numbers, sorting)

### Grammar Development

The assembly language grammar is defined using ANTLR4:
- Grammar file: `antlr/idl/toy_asm.g4`
- Generated parsers: `src/internal/grammar/toy_asmParser.py`, `toy_asmLexer.py`
- Visitor implementation: `src/internal/grammar/visitor_impl.py`

If you modify the grammar, regenerate parsers using ANTLR4 tools.

## Code Architecture

### Core Components

**1. Computer Simulator (`src/internal/computer/computer.py`)**
- `Computer` class: Main execution engine that simulates the CPU
- Registers: `ax`, `bx`, `cx`, `dx` (general purpose), `flg` (flags), `ip` (instruction pointer), `bp` (base pointer), `sp` (stack pointer)
- Memory: 1024 cells, divided into heap (grows up) and stack (grows down from address 1023)
- Execution loop: Fetches and executes instructions, manages program state

**2. Instruction Operations (`src/internal/computer/operations.py`)**
All assembly instructions are implemented as Python classes inheriting from `Op`:
- Arithmetic: `Move`, `Add`, `Sub`, `Mul`, `Div`
- Comparison and Control Flow: `Cmp`, `Jump` (jmp/je/jne/jg/jge/jl/jle)
- Function Calls: `Call`, `Ret`, `Push`, `Pop`
- I/O: `Input`, `Print`, `Rand`
- Debugging: `Dump`, `Pause`, `Halt`, `Nop`

Each operation's `execute()` method modifies the `Computer` state and advances `ip`.

**3. Parser and Visitor (`src/internal/grammar/`)**
- ANTLR4-generated lexer and parser process `.asm` files
- `VisitorImpl` converts parse tree to list of `Op` objects and labels
- Labels are mapped to instruction addresses for jump/call targets

**4. Execution Entry Point (`src/console_executor/main.py`)**
- Parses command-line arguments
- Loads and parses assembly file
- Creates `Computer` instance and runs program
- Supports step mode (`--step`) for debugging

**5. Web Interface (`src/web_backend/webserver.py`)**
- FastAPI-based web server on port 22000
- Serves static frontend from `src/web_frontend/`
- API endpoint `/sourcecode` for executing assembly code (implementation in progress)

### Key Design Patterns

**Stack Frame Convention**
The stack grows downward (from address 1023 toward 0). Function call convention:
```
[caller's stack]
parameter 2        <- sp before call
parameter 1
return value slot
saved ip           <- pushed by 'call'
saved bp           <- first instruction in function
local var 1        <- bp after 'mov bp, sp'
local var 2
...                <- sp during function execution
```

**Instruction Execution Cycle**
1. Load instruction at address `ip`
2. Execute instruction (modifies registers/memory)
3. Instruction updates `ip` (usually `ip += 1`, but jumps/calls change it directly)
4. If step mode, display dump and wait for user input
5. Repeat until `ip` exceeds instruction count or error occurs

**Memory Type Tracking**
Memory cells store `(value, MemType)` tuples to help with debugging:
- `MemType.Data`: Regular data
- `MemType.IP`: Saved instruction pointer (return address)
- `MemType.BP`: Saved base pointer

### Assembly Language Features

**Registers**
- General purpose: `ax`, `bx`, `cx`, `dx`
- Special: `flg` (comparison result: -1/0/1), `ip`, `bp`, `sp`

**Memory Addressing**
- Direct: `[ax+5]`, `[bp-2]`, `[sp]` (offset defaults to 0 if omitted)
- Offset can be positive or negative

**Labels and Comments**
- Labels: lowercase identifiers followed by `:` (e.g., `loop1:`, `_function:`)
- Comments: lines starting with `;`

**Key Instructions**
- `mov dst, src`: Move value to register or memory
- `call label`: Push return address and jump to label
- `ret`: Pop return address and jump back
- `push`/`pop`: Stack operations (auto-decrement/increment `sp`)
- `dump [reg,] count`: Display system state for debugging
- `halt`: Stop execution cleanly

## Important Implementation Notes

- Division (`div`) performs truncation toward zero (C-style), with remainder always having same sign as dividend
- Stack pointer `sp` is automatically modified by `push`, `pop`, `call`, `ret`
- The `ip` register cannot be modified with `mov` - only by jumps, calls, and rets
- Memory indexing is 0-based
- Step mode (`--step`) automatically executes `dump` after each instruction

## Educational Context

This project implements a pedagogical progression (see README.md lessons 1-7):
1. Register operations (mov, arithmetic)
2. Memory operations
3. Loops and conditionals (cmp, jumps)
4. Functions (call/ret basics)
5. Stack frames (parameters, locals, return values)
6. Complex algorithms (sorting)
7. Real-world assembly comparison

When modifying code, preserve the educational clarity - operations should remain simple and understandable for students learning computer architecture fundamentals.
