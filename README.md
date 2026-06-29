# hands_on_pyspark

Local environment for **Apache Spark 4** (PySpark).

## What's installed

| Component | Version | Notes |
|-----------|---------|-------|
| PySpark   | 4.0.3   | installed in `.venv` via pip |
| Python    | 3.14.3  | Homebrew |
| Java      | OpenJDK 17 | `/opt/homebrew/opt/openjdk@17` (Spark 4 needs Java 17 or 21) |

## Daily use

```bash
source .venv/bin/activate   # also sets JAVA_HOME to OpenJDK 17
python smoke_test.py        # sanity check
```

Activating the venv sets `JAVA_HOME` automatically (an `export` was appended to
`.venv/bin/activate`). Start a REPL with `pyspark`, or run scripts with
`spark-submit your_script.py`.

## Recreating the environment from scratch

```bash
# 1. Java 17 (keg-only, not symlinked)
brew install openjdk@17

# 2. venv + deps
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # or: pip install "pyspark[sql]==4.0.*"

# 3. Point Spark at Java 17 (if you didn't re-add it to activate)
export JAVA_HOME="/opt/homebrew/opt/openjdk@17"
```

> Note: recreating `.venv` overwrites `.venv/bin/activate`, so re-append the
> `JAVA_HOME` export or set it in your shell profile.
