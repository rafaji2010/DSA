"""
Contact Book CLI — Pydantic models, JSON/CSV persistence, interactive menu.

Run:
    python -m core.contact_book
    python core/contact_book.py
"""

from __future__ import annotations

import csv
import json
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from pydantic import BaseModel, ValidationError, field_validator

DEFAULT_DB = Path("contacts.json")
CSV_FIELDS = ("name", "phone", "email")


class Contact(BaseModel):
    name: str
    phone: str
    email: str

    @field_validator("name")
    @classmethod
    def name_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Name cannot be empty")
        return v.strip().title()

    @field_validator("phone")
    @classmethod
    def phone_digits_only(cls, v: str) -> str:
        cleaned = "".join(c for c in v if c.isdigit())
        if len(cleaned) < 7:
            raise ValueError("Phone must have at least 7 digits")
        return cleaned

    @field_validator("email")
    @classmethod
    def email_valid(cls, v: str) -> str:
        if v.count("@") != 1:
            raise ValueError("Email must contain exactly one @ symbol")

        local, domain = v.split("@")

        if not local:
            raise ValueError("Email local part cannot be empty")

        if "." not in domain:
            raise ValueError("Email domain must contain a dot")

        domain_parts = domain.split(".")
        if any(len(part) == 0 for part in domain_parts):
            raise ValueError("Email domain has empty parts")

        return v.lower().strip()


@dataclass
class ImportResult:
    added: int
    updated: int
    skipped: int
    errors: list[tuple[int, str]]


class ContactBook:
    def __init__(self, contacts: list[Contact] | None = None) -> None:
        self.contacts: list[Contact] = contacts or []

    def add(self, contact: Contact) -> None:
        if any(c.name.lower() == contact.name.lower() for c in self.contacts):
            raise ValueError(f"Contact '{contact.name}' already exists")
        self.contacts.append(contact)
        self.contacts.sort(key=lambda c: c.name.lower())

    def remove(self, name: str) -> Contact | None:
        for idx, contact in enumerate(self.contacts):
            if contact.name.lower() == name.strip().lower():
                return self.contacts.pop(idx)
        return None

    def find_by_name(self, name: str) -> Contact | None:
        key = name.strip().lower()
        for contact in self.contacts:
            if contact.name.lower() == key:
                return contact
        return None

    def search(self, query: str) -> list[Contact]:
        key = query.strip().lower()
        if not key:
            return list(self.contacts)
        return [
            c
            for c in self.contacts
            if key in c.name.lower() or key in c.email or key in c.phone
        ]

    def update(self, name: str, updated: Contact) -> Contact:
        idx = next(
            (i for i, c in enumerate(self.contacts) if c.name.lower() == name.strip().lower()),
            None,
        )
        if idx is None:
            raise ValueError(f"Contact '{name}' not found")

        if updated.name.lower() != name.strip().lower():
            if any(
                c.name.lower() == updated.name.lower()
                for i, c in enumerate(self.contacts)
                if i != idx
            ):
                raise ValueError(f"Contact '{updated.name}' already exists")

        self.contacts[idx] = updated
        self.contacts.sort(key=lambda c: c.name.lower())
        return updated

    def save(self, path: Path = DEFAULT_DB) -> None:
        payload = [c.model_dump() for c in self.contacts]
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    @classmethod
    def load(cls, path: Path = DEFAULT_DB) -> ContactBook:
        if not path.exists():
            return cls()
        raw = json.loads(path.read_text(encoding="utf-8"))
        contacts = [Contact.model_validate(item) for item in raw]
        return cls(contacts)

    def export_csv(self, path: Path) -> None:
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.model_dump())

    def import_csv(self, path: Path, *, replace: bool = False) -> ImportResult:
        if not path.exists():
            raise FileNotFoundError(f"CSV file not found: {path}")

        added = 0
        updated = 0
        skipped = 0
        errors: list[tuple[int, str]] = []
        imported: list[Contact] = []

        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None:
                raise ValueError("CSV file is empty or missing a header row")

            missing = [field for field in CSV_FIELDS if field not in reader.fieldnames]
            if missing:
                raise ValueError(f"CSV missing required columns: {', '.join(missing)}")

            for row_num, row in enumerate(reader, start=2):
                if not any((row.get(field) or "").strip() for field in CSV_FIELDS):
                    skipped += 1
                    continue

                try:
                    contact = Contact.model_validate(
                        {field: (row.get(field) or "").strip() for field in CSV_FIELDS}
                    )
                except ValidationError as exc:
                    message = "; ".join(
                        f"{err['loc'][0]}: {err['msg']}" for err in exc.errors()
                    )
                    errors.append((row_num, message))
                    continue

                imported.append(contact)

        if replace:
            self.contacts = imported
            self.contacts.sort(key=lambda c: c.name.lower())
            return ImportResult(added=len(imported), updated=0, skipped=skipped, errors=errors)

        for contact in imported:
            existing = self.find_by_name(contact.name)
            if existing is None:
                self.contacts.append(contact)
                added += 1
            else:
                self.update(existing.name, contact)
                updated += 1

        self.contacts.sort(key=lambda c: c.name.lower())
        return ImportResult(added=added, updated=updated, skipped=skipped, errors=errors)


def _prompt(label: str, *, required: bool = True, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    while True:
        value = input(f"{label}{suffix}: ").strip()
        if value:
            return value
        if default:
            return default
        if not required:
            return ""
        print("  This field is required.")


def _prompt_contact(*, defaults: Contact | None = None) -> Contact:
    name_default = defaults.name if defaults else ""
    phone_default = defaults.phone if defaults else ""
    email_default = defaults.email if defaults else ""

    while True:
        try:
            return Contact(
                name=_prompt("Name", default=name_default),
                phone=_prompt("Phone", default=phone_default),
                email=_prompt("Email", default=email_default),
            )
        except ValidationError as exc:
            print("\nValidation errors:")
            for err in exc.errors():
                field = err["loc"][0]
                print(f"  - {field}: {err['msg']}")
            print()


def _print_contact(contact: Contact) -> None:
    print(f"  Name:  {contact.name}")
    print(f"  Phone: {contact.phone}")
    print(f"  Email: {contact.email}")


def _print_contacts(contacts: list[Contact], *, title: str) -> None:
    if not contacts:
        print(f"\n{title}: none found.\n")
        return
    print(f"\n{title} ({len(contacts)}):")
    print("-" * 40)
    for contact in contacts:
        _print_contact(contact)
        print("-" * 40)
    print()


def _handle_add(book: ContactBook) -> None:
    print("\nAdd a new contact")
    contact = _prompt_contact()
    try:
        book.add(contact)
    except ValueError as exc:
        print(f"\nError: {exc}\n")
        return
    book.save()
    print(f"\nAdded {contact.name}.\n")


def _handle_list(book: ContactBook) -> None:
    _print_contacts(book.contacts, title="All contacts")


def _handle_search(book: ContactBook) -> None:
    query = input("\nSearch (name, email, or phone): ").strip()
    results = book.search(query)
    _print_contacts(results, title="Search results")


def _handle_update(book: ContactBook) -> None:
    name = _prompt("\nName of contact to update")
    existing = book.find_by_name(name)
    if existing is None:
        print(f"\nContact '{name}' not found.\n")
        return

    print("\nCurrent details:")
    _print_contact(existing)
    print("\nEnter new details (press Enter to keep current value):")
    updated = _prompt_contact(defaults=existing)

    try:
        book.update(existing.name, updated)
    except ValueError as exc:
        print(f"\nError: {exc}\n")
        return

    book.save()
    print(f"\nUpdated {updated.name}.\n")


def _handle_delete(book: ContactBook) -> None:
    name = _prompt("\nName of contact to delete")
    removed = book.remove(name)
    if removed is None:
        print(f"\nContact '{name}' not found.\n")
        return
    book.save()
    print(f"\nDeleted {removed.name}.\n")


def _handle_export_csv(book: ContactBook) -> None:
    path_str = _prompt("\nCSV file to export", default="contacts.csv")
    path = Path(path_str)
    try:
        book.export_csv(path)
    except OSError as exc:
        print(f"\nError exporting CSV: {exc}\n")
        return
    print(f"\nExported {len(book.contacts)} contact(s) to {path.resolve()}.\n")


def _handle_import_csv(book: ContactBook) -> None:
    path_str = _prompt("\nCSV file to import")
    path = Path(path_str)

    print("\nImport mode:")
    print("  1. Merge  — add new contacts, update existing by name")
    print("  2. Replace — replace all contacts with CSV contents")
    mode = input("Choose mode [1-2]: ").strip()
    replace = mode == "2"
    if mode not in {"1", "2"}:
        print("\nInvalid mode. Choose 1 (merge) or 2 (replace).\n")
        return

    try:
        result = book.import_csv(path, replace=replace)
    except (FileNotFoundError, ValueError, OSError) as exc:
        print(f"\nError importing CSV: {exc}\n")
        return

    book.save()
    action = "Replaced with" if replace else "Imported from"
    print(f"\n{action} {path.resolve()}:")
    print(f"  Added:   {result.added}")
    print(f"  Updated: {result.updated}")
    print(f"  Skipped: {result.skipped} empty row(s)")
    if result.errors:
        print(f"  Errors:  {len(result.errors)} row(s) failed validation")
        for row_num, message in result.errors:
            print(f"    - Row {row_num}: {message}")
    print()


def _print_menu() -> None:
    print(
        """
Contact Book
============
1. Add contact
2. List all contacts
3. Search contacts
4. Update contact
5. Delete contact
6. Export CSV
7. Import CSV
8. Save and exit
"""
    )


def main() -> None:
    db_path = DEFAULT_DB
    book = ContactBook.load(db_path)
    print(f"Loaded {len(book.contacts)} contact(s) from {db_path.resolve()}.")

    actions: dict[str, tuple[str, Callable[[ContactBook], None]]] = {
        "1": ("Add contact", _handle_add),
        "2": ("List all contacts", _handle_list),
        "3": ("Search contacts", _handle_search),
        "4": ("Update contact", _handle_update),
        "5": ("Delete contact", _handle_delete),
        "6": ("Export CSV", _handle_export_csv),
        "7": ("Import CSV", _handle_import_csv),
    }

    try:
        while True:
            _print_menu()
            choice = input("Choose an option [1-8]: ").strip()

            if choice == "8":
                book.save(db_path)
                print(f"\nSaved {len(book.contacts)} contact(s). Goodbye!\n")
                break

            action = actions.get(choice)
            if action is None:
                print("\nInvalid choice. Enter a number from 1 to 8.\n")
                continue

            _, handler = action
            handler(book)
    except (KeyboardInterrupt, EOFError):
        book.save(db_path)
        print(f"\n\nSaved {len(book.contacts)} contact(s). Goodbye!\n")


if __name__ == "__main__":
    main()
