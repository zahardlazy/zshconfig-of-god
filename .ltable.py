import os
import sys
import datetime
import stat
from rich.console import Console
from rich.table import Table
from rich import box
from rich.filesize import decimal

console = Console()

# --- THEME ARKNIGHTS ---
THEME = {
    "border": "bold cyan",
    "header": "bold white on #005f87",
    "dir": "bold bright_cyan",
    "file": "bold white",
    "symlink": "italic magenta",
    "size": "bold spring_green1",
    "user": "bold hot_pink",
    "date_day": "bold gold1",
    "date_time": "dim white",
}

def get_win_perms(path):
    try:
        st = os.stat(path)
        is_dir = stat.S_ISDIR(st.st_mode)
        is_write = (st.st_mode & stat.S_IWRITE)
        ext = os.path.splitext(path)[1].lower()
        is_exec = ext in ['.exe', '.bat', '.ps1', '.cmd', '.com', '.py']
        
        p = "d" if is_dir else "-"
        p += "r"
        p += "w" if is_write else "-"
        p += "x" if (is_dir or is_exec) else "-"
        p += "r-x"
        
        res = ""
        for char in p:
            if char == 'd': res += "[bold cyan]d[/]"
            elif char == 'r': res += "[bold green]r[/]"
            elif char == 'w': res += "[bold red on black]w[/]"
            elif char == 'x': res += "[bold yellow]x[/]"
            elif char == '-': res += "[dim grey30]-[/]"
            else: res += f"[bold white]{char}[/]"
        return res
    except:
        return "[dim]-[/]"

try:
    target_path = sys.argv[1] if len(sys.argv) > 1 else "."
    if not os.path.exists(target_path):
        console.print(f"[red]Error: Path '{target_path}' not found.[/]")
        sys.exit(1)

    abs_path = os.path.abspath(target_path)
    
    table = Table(
        title=f"[bold white]WIN_LOC: [/][bold cyan]{abs_path}[/]", 
        box=box.ROUNDED, 
        header_style=THEME["header"],
        border_style=THEME["border"],
        expand=True
    )

    table.add_column("PERMS", justify="left") 
    table.add_column("SIZE", justify="center", style=THEME["size"])
    table.add_column("OWNER", justify="center", style=THEME["user"])
    table.add_column("MODIFIED", justify="center")
    table.add_column("OBJECT NAME", style=THEME["file"])

    current_user = os.environ.get('USERNAME', 'User')

    with os.scandir(target_path) as entries:
        sorted_entries = sorted(entries, key=lambda e: e.name.lower())
        
        for entry in sorted_entries:
            if entry.name.startswith("."): continue
            try:
                st = entry.stat()
                perms = get_win_perms(entry.path)
                is_dir = entry.is_dir()
                size = "-" if is_dir else decimal(st.st_size)
                
                dt = datetime.datetime.fromtimestamp(st.st_mtime)
                date_str = f"[{THEME['date_day']}]{dt.strftime('%d %b')}[/] [{THEME['date_time']}]{dt.strftime('%H:%M')}[/]"

                if is_dir:
                    icon = "📂 "
                    name = f"{icon}[{THEME['dir']}]{entry.name}[/]"
                else:
                    ext = os.path.splitext(entry.name)[1].lower()
                    icon = " "
                    if ext in ['.py', '.c', '.cpp', '.js', '.ps1']: icon = " "
                    if ext in ['.zip', '.rar', '.7z']: icon = " "
                    if ext in ['.exe', '.msi']: 
                        icon = "🚀 "
                        name = f"{icon}[bold green]{entry.name}[/]"
                    else:
                        name = f"{icon}{entry.name}"

                table.add_row(perms, size, current_user, date_str, name)
            except: pass

    console.print(table)
except Exception as e:
    console.print(f"[red]Error: {e}[/]")