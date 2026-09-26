from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()


def show_banner() -> None:
    console.print(
        Panel.fit(
            "[bold]SocialEngineer Framework[/bold]\n"
            "Social Engineering Awareness & Simulation\n"
            "[dim]Version 2.0-dev[/dim]",
            title="SocialEngineer",
        )
    )


def show_menu() -> None:
    console.print()
    console.print("[bold]Main Menu[/bold]")
    console.print("1. Reconnaissance")
    console.print("2. Campaign Manager")
    console.print("3. Email Simulation")
    console.print("4. Training Landing Pages")
    console.print("5. Analytics & Reporting")
    console.print("6. Configuration")
    console.print("7. Legacy Tools")
    console.print("99. Exit")


def main() -> None:
    show_banner()

    while True:
        show_menu()

        choice = Prompt.ask(
            "\nSelect an option",
            choices=["1", "2", "3", "4", "5", "6", "7", "99"],
        )

        match choice:
            case "1":
                console.print("\n[yellow]Reconnaissance module coming next.[/yellow]")

            case "2":
                console.print("\n[yellow]Campaign Manager coming next.[/yellow]")

            case "3":
                console.print("\n[yellow]Email Simulation coming next.[/yellow]")

            case "4":
                console.print("\n[yellow]Training Landing Pages coming next.[/yellow]")

            case "5":
                console.print("\n[yellow]Analytics & Reporting coming next.[/yellow]")

            case "6":
                console.print("\n[yellow]Configuration module coming next.[/yellow]")

            case "7":
                console.print(
                    "\nLegacy tools remain available under "
                    "[bold]Social-Engineer/[/bold]."
                )

            case "99":
                console.print("\n[green]Exiting SocialEngineer.[/green]")
                break


if __name__ == "__main__":
    main()