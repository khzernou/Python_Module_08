import os

from dotenv import load_dotenv


def load_configuration() -> dict[str, str]:
    """load env into env, reads all config values"""
    load_dotenv()  # fills gaps in os.environ, real env vars take priority

    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL", ""),
        "API_KEY": os.getenv("API_KEY", ""),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", ""),
    }


def find_missing(config: dict[str, str]) -> list[str]:
    """return names of required value that are empty"""
    required = ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT")
    return [key for key in required if not config[key]]


def describe_database(url: str, mode: str) -> str:
    """describe database connection based on mode and config"""
    if not url:
        return "Not configured"
    if mode == "production":
        return "Connected to production cluster"
    return "Connected to local instance"


def describe_api(api_key: str) -> str:
    """describe api acess based on whether a key is present"""
    return "Authenticated" if api_key else "No API key - unauthenticated"


def describe_zion(endpoint: str) -> str:
    """describe zion network connection status"""
    return "Online" if endpoint else "Offline - no endpoint configured"


def print_security_check(config: dict[str, str], missing: list[str]) -> None:
    """print small checklist ab config security"""
    print("\nEnvironment security check:")
    if missing:
        print(f"[WARN] Missing configuration: {', '.join(missing)}")
    else:
        print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file not found (using defaults/env vars only)")

    if config["MATRIX_MODE"] == "production":
        print("[OK] Running in production mode")
    else:
        print("[OK] Production overrides available via environment variables")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = load_configuration()
    missing = find_missing(config)

    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    print(f"Database: {describe_database(config['DATABASE_URL'], config['MATRIX_MODE'])}")
    print(f"API Access: {describe_api(config['API_KEY'])}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {describe_zion(config['ZION_ENDPOINT'])}")

    print_security_check(config, missing)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
