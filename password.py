import secrets
import string
import math
import sys

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except Exception:
    CLIPBOARD_AVAILABLE = False


AMBIGUOUS = {'l', 'I', '1', 'O', '0', 'o'}


def build_charset(use_lower, use_upper, use_digits, use_symbols, remove_ambiguous):
    charset = ""
    if use_lower:
        charset += string.ascii_lowercase
    if use_upper:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += "!@#$%^&*()-_=+[]{};:,.<>/?"
    if remove_ambiguous:
        charset = ''.join(ch for ch in charset if ch not in AMBIGUOUS)
    return charset


def generate_password(length, charset):
    if not charset:
        raise ValueError("Character set is empty. Enable at least one charset option.")
    return ''.join(secrets.choice(charset) for _ in range(length))


def estimate_entropy(length, charset_size):
    """
    Entropy in bits: length * log2(charset_size)
    Return float entropy.
    """
    if charset_size <= 1:
        return 0.0
    return length * math.log2(charset_size)


def strength_label(entropy_bits):
    """
    Simple label based on entropy:
    <28 bits  -> Very weak
    28-35    -> Weak
    36-59    -> Reasonable
    60-127   -> Strong
    128+     -> Very strong
    """
    if entropy_bits < 28:
        return "Very weak"
    if entropy_bits < 36:
        return "Weak"
    if entropy_bits < 60:
        return "Reasonable"
    if entropy_bits < 128:
        return "Strong"
    return "Very strong"


def safe_int_input(prompt, min_val=None, max_val=None, default=None):
    while True:
        try:
            s = input(prompt).strip()
            if s == "" and default is not None:
                return default
            val = int(s)
            if min_val is not None and val < min_val:
                print(f"Please enter a number >= {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print(f"Please enter a number <= {max_val}.")
                continue
            return val
        except ValueError:
            print("Enter a valid integer.")


def ask_yes_no(prompt, default=False):
    suf = " [Y/n]: " if default else " [y/N]: "
    while True:
        ans = input(prompt + suf).strip().lower()
        if ans == "" and default is not None:
            return default
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please answer y (yes) or n (no).")


def main():
    print("\n✨ CodSoft — Password Generator (Day 2) ✨\n")
    print("Quick guide: choose policies, pick length, and generate secure passwords.\n")

    # Options
    use_lower = ask_yes_no("Include lowercase letters?", True)
    use_upper = ask_yes_no("Include uppercase letters?", True)
    use_digits = ask_yes_no("Include digits?", True)
    use_symbols = ask_yes_no("Include symbols (e.g. @#$)?", False)
    remove_ambiguous = ask_yes_no("Remove ambiguous characters (like I, l, 0, O)?", True)

    length = safe_int_input("Password length (recommended 12-20): ", min_val=4, max_val=128, default=12)
    count = safe_int_input("How many passwords to generate? ", min_val=1, max_val=50, default=3)

    charset = build_charset(use_lower, use_upper, use_digits, use_symbols, remove_ambiguous)
    if not charset:
        print("Error: No character categories selected. Exiting.")
        sys.exit(1)

    print("\nGenerating passwords...\n")
    results = []
    for i in range(count):
        pwd = generate_password(length, charset)
        entropy = estimate_entropy(length, len(charset))
        label = strength_label(entropy)
        results.append((pwd, entropy, label))
        print(f"[{i+1}] {pwd}")
        print(f"     Entropy: {entropy:.1f} bits  →  Strength: {label}\n")

    if CLIPBOARD_AVAILABLE:
        if ask_yes_no("Copy the first password to clipboard?", True):
            pyperclip.copy(results[0][0])
            print("First password copied to clipboard.")
    else:
        print("(Tip: Install 'pyperclip' to enable clipboard copy: pip install pyperclip)")

    if ask_yes_no("Save generated passwords to a file?", False):
        fname = input("Enter filename (default: passwords.txt): ").strip()
        if not fname:
            fname = "passwords.txt"
        try:
            with open(fname, "w", encoding="utf-8") as f:
                f.write("CodSoft Password Generator — Results\n")
                f.write("="*40 + "\n")
                for idx, (pwd, entropy, label) in enumerate(results, 1):
                    f.write(f"{idx}. {pwd}\n")
                    f.write(f"   Entropy: {entropy:.1f} bits  Strength: {label}\n\n")
            print(f"Saved to {fname}")
        except Exception as e:
            print("Error saving file:", e)

    print("\n🙏 Done. Use these passwords responsibly. Keep them private!\n")


if __name__ == "__main__":
    main()
