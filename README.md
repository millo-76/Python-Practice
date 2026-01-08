# Python Workspace

This workspace contains personal Python projects and course materials for INFS 3070. Local environment files (executables, DLLs, and virtual environments) may be present in the workspace but are ignored by Git via `.gitignore`. Only project code and notebooks in tracked folders should be pushed to GitHub.

## Table of Contents

- [About](#about)
- [Folder Structure](#folder-structure)
- [Personal Programs](#personal-programs)
- [INFS 3070](#infs-3070)
- [How to Run](#how-to-run)
- [Contributing](#contributing)
- [License](#license)

## About

This repository stores two main categories of content:

- Personal projects under `Personal Programs/`
- Course materials for INFS 3070 under `INFS 3070/` (these are personal coursework and not for redistribution)

## Folder Structure

Snapshot of the main folders and representative files:

```text
Personal Programs/
├── baseball-program/
│   ├── .venv/
│   └── test4.py
├── games/
├── lol-probability/
├── wrestler-tracker/
└── wrestling-programs/

INFS 3070/
├── README.md
├── Assignments/
│   ├── homework2.ipynb
│   ├── homework3.ipynb
│   ├── MarlinJaramilloHW1.ipynb
│   ├── MarlinJaramilloProject1.ipynb
│   ├── MarlinJaramilloProject2.ipynb
│   ├── mjarami8_Final.py
│   ├── dbConfig.py
│   ├── question1.csv
│   └── question2.csv
├── DataFiles/
├── practice prgrams/
└── Weeks/
    ├── week 1/
    ├── week 2/
    ├── week 3/
    ├── week 4/
    ├── week 5/
    ├── week 6/
    ├── week 7/
    ├── week 8/
    ├── week 9/
    ├── week 10/
    └── week 11/
```

**Notes:**

- Put personal projects in `Personal Programs/` — use one subfolder per project
- Course materials are under `INFS 3070/` and represent personal coursework
- Local environment/runtime files (e.g., `python.exe`, `DLLs/`, `Lib/`, `include/`, `Scripts/`, `.venv/`) are local-only and ignored by Git

## Personal Programs

Store standalone projects here. Each project should include a README and any environment instructions.

Current projects:

- **baseball-program**: Baseball-related program
- **games**: Game-related projects
- **lol-probability**: League of Legends probability calculations
- **wrestler-tracker**: Wrestling tracker application
- **wrestling-programs**: Wrestling-related programs

## INFS 3070

Course materials, weekly exercises, and assignment notebooks. The course includes:

- **Assignments**: Homework assignments, projects, and final exam materials
- **DataFiles**: Data files used for coursework
- **practice prgrams**: Practice programs and exercises
- **Weeks**: Weekly course materials organized by week (weeks 1-11)

## How to Run

1. Select a Python interpreter in VS Code that has the necessary packages installed.
2. To run a script with the workspace Python executable on Windows:

    ```powershell
    "C:/Users/marja/OneDrive/Desktop/Code/Pyton Workspace/python.exe" path\to\script.py
    ```

3. To run notebooks, make sure `jupyter` and `ipykernel` are installed in the selected interpreter and choose that kernel in VS Code.

## Contributing

Contributions are welcome for general projects. Do not modify submitted coursework under `INFS 3070/`.

## License

Most repository content is released under the MIT License. Course assignment materials are not licensed for public reuse.
