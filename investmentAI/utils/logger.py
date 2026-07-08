from textwrap import fill


def print_header(title: str):
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80)


def print_success(message: str):
    print(f"✅ {message}")


def print_error(message: str):
    print(f"❌ {message}")


def print_info(message: str):
    print(f"ℹ️  {message}")


def print_block(title: str, content: str):

    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)

    print(fill(str(content), width=100))