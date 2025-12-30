# Database Migration File Generator (Python)

A tool to create timestamped SQL migration files (.sql) to keep database changes organized.

## Features

-   **Timestamped Filenames**: Ensures migrations run in order (e.g., `20240101_120000_create_users.sql`).
-   **Template Generation**: Creates `UP` and `DOWN` (rollback) sections comments.
-   **CLI Command**: Easy creation via `python generate.py "description"`.

## Installation

1.  **Clone the repository**
2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
# Generate a new migration file
python run_generator.py "create users table"
```

Output:
`migrations/20241027_103000_create_users_table.sql` created.

## Contact

Developed for Anunzio International by Anzul Aqeel.
Contact +971545822608 or +971585515742.

## License

MIT


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
